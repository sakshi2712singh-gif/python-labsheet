"""Shared SQLite connection and input helpers for Lab Sheet 09."""

import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def database_path():
    """Return a configured database path or the local default path."""
    configured = os.environ.get("LABSHEET9_DB_PATH")
    if configured:
        return Path(configured).expanduser().resolve()
    return BASE_DIR / "student_crud.sqlite"


@contextmanager
def database():
    """Yield a SQLite connection and close it even when an operation fails."""
    path = database_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        with connection:
            yield connection
    finally:
        connection.close()


def create_students_table(connection):
    """Create the shared table while retaining existing records."""
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            roll_no INTEGER NOT NULL UNIQUE,
            name TEXT NOT NULL,
            age INTEGER NOT NULL CHECK (age >= 0),
            marks REAL NOT NULL CHECK (marks >= 0 AND marks <= 100)
        )
        """
    )


def prompt_int(message, minimum=None):
    """Read an integer value, repeating until the input is valid."""
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
    """Read a non-empty name."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Name cannot be empty.")
