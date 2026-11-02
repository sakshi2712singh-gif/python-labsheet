MCA101P-AS11 - Lab Sheet 08
Database Management with Python

The 30 questions are implemented as separate Python files and use SQLite,
Python's built-in database library. No packages or MySQL server are required.

Getting started
---------------
Open a terminal in this folder and run:

    python Q02_create_database.py
    python Q03_create_students_table.py
    python Q09_insert_multiple_students.py

Enter sample records, for example:

    Asha
    20
    88
    Ravi
    21
    76
    Mina
    19
    38
    Noor
    20
    92
    [blank name to finish]

Run Q21_create_courses_and_insert.py after adding students to create sample
course records. Run other Q*.py programs individually. Q30 provides its own
interactive menu. All programs use student_db.sqlite in this folder by default.
Set LABSHEET8_DB_PATH to a different SQLite filename to use another database.

SQLite-specific notes
---------------------
SQLite creates a database file when the program connects to it; it does not use
the MySQL CREATE DATABASE statement. Q02 demonstrates creating that file.
Q03 creates the students table with id, name, age, and marks. Courses are linked
to students by courses.student_id, since the assignment's students schema does
not include a course column. Run Q21 before Q22 or Q23.

Q06 drops the students table only after you type DROP STUDENTS.
Q18 and Q30 require DELETE confirmation. Q19 shows how many marks below 40 match
before requiring DELETE. Q20 shows the row count and requires EMPTY STUDENTS;
it removes rows but keeps the table. These operations intentionally modify the
database, not the source-code files.

Q26 creates a new CSV export and will not replace an existing file. Q27 imports
sample_students_import.csv, whose sample IDs start at 101. Do not import it
twice into the same database because student IDs must be unique.

Question map
------------
Q01 connect to SQLite
Q02 create a database file
Q03 create the students table
Q04 describe the table structure
Q05 list database tables
Q06 drop the students table with confirmation
Q07 check whether a table exists
Q08 insert one student
Q09 insert multiple students
Q10 display all student records
Q11 display student names and marks
Q12 find marks above 80
Q13 sort by descending marks
Q14 count students
Q15 display the top three students
Q16 update marks using student ID
Q17 update a student name
Q18 delete one student by ID with confirmation
Q19 delete students with marks below 40 after confirmation
Q20 empty the students table and keep its structure
Q21 create courses and insert sample linked course records
Q22 perform an INNER JOIN
Q23 perform a LEFT JOIN
Q24 calculate the average marks
Q25 group students by age
Q26 export student data to CSV
Q27 import validated CSV data
Q28 demonstrate handling a database error
Q29 insert and fetch using reusable functions
Q30 run an Add/View/Update/Delete menu

Execution report
----------------
The programs were syntax checked and run individually with Python 3.14 using
disposable SQLite database files and temporary output files. Tests exercise
regular database reads/writes, both joins, CSV export/import, the interactive
menu, and each guarded destructive operation. The databases and output files
used for testing are separate from this folder's source and samples.
