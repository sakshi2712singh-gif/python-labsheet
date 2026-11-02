"""Shared SQLite connection and input helpers for Lab Sheet 08."""

import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def database_path():
    """Return the configured database file, defaulting to this folder."""
    configured = os.environ.get("LABSHEET8_DB_PATH")
    if configured:
        return Path(configured).expanduser().resolve()
    return BASE_DIR / "student_db.sqlite"


def ensure_database():
    """Create the SQLite database file if it does not exist yet."""
    path = database_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.close()
    return path


@contextmanager
def database():
    """Open one database connection, commit successful work, and always close."""
    path = ensure_database()
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    try:
        with connection:
            yield connection
    finally:
        connection.close()


def create_students_table(connection):
    """Create the shared student schema without replacing existing records."""
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL CHECK (age >= 0),
            marks REAL NOT NULL CHECK (marks >= 0 AND marks <= 100)
        )
        """
    )


def prompt_int(message, minimum=None):
    """Read an integer and repeat the prompt until it meets the minimum."""
    while True:
        try:
            value = int(input(message))
            if minimum is not None and value < minimum:
                print(f"Enter a value of at least {minimum}.")
                continue
            return value
        except ValueError:
            print("Enter a whole number.")


def prompt_marks(message):
    """Read a numeric mark in the inclusive 0–100 range."""
    while True:
        try:
            value = float(input(message))
            if 0 <= value <= 100:
                return value
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Enter a valid number.")


def prompt_name(message):
    """Read a non-empty student name."""
    while True:
        name = input(message).strip()
        if name:
            return name
        print("Name cannot be empty.")
