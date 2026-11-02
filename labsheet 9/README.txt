MCA101P-AS12 - Lab Sheet 09
CRUD Operations with Python

Each of the 20 assignment questions has its own Python program. The programs use
Python's standard library; database exercises use the built-in SQLite module.

Run an individual exercise from this folder, for example:

    python Q01_create_student_list.py
    python Q11_create_students_table.py
    python Q20_student_database_crud_menu.py

Questions 1-8 use example records in memory. Questions 9-10 use their own text
or JSON data files. Questions 11-20 use a SQLite database named
student_crud.sqlite in this folder. Set LABSHEET9_DB_PATH to use another
database file. The database table is created by question 11; question 20 creates
the table when it starts.

Question 9 creates a new CSV-formatted text file and reads it back. Its default
filename is students.txt. If the file already exists, choose another name rather
than overwriting it.

Question 10 saves file-based student records as JSON in student_records.json.
Set LABSHEET9_RECORDS_PATH to choose a different data file. This file is created
when records are added; the original Python program files are never modified.

Questions 16, 20, and the menu deletion actions ask for confirmation before
removing a database or file record. Those actions affect only the selected data
record, not the source-code files. Question 6 drops only an in-memory dictionary
entry and question 5 removes only an in-memory list entry.

The database schema stores id, roll_no, name, age, and marks. roll_no is unique
and is used by the assignment questions that search/update/delete by roll
number. SQL values are passed as parameters.

Question map
------------
Q01 create a list of student records
Q02 display all records from a list
Q03 search a list by student name
Q04 update marks in a list
Q05 delete a list record by roll number
Q06 employee dictionary CRUD
Q07 menu-driven book list CRUD
Q08 product CRUD menu
Q09 save student data to text and read it back
Q10 file-based add/view/modify/delete using JSON
Q11 connect to SQLite and create the students table
Q12 insert one student record
Q13 display all database records
Q14 search by roll number
Q15 update marks using roll number
Q16 delete a record using roll number
Q17 count the database records
Q18 sort records by student name
Q19 find the highest mark, including ties
Q20 database-backed Add/View/Update/Delete menu

Execution report
----------------
All 20 programs were run using Python 3.14.6. File and menu exercises used
temporary test data. Database questions used a separate temporary SQLite
database for each program. Checks covered the selected student and updated
values, delete results, persistent JSON changes, database row counts, sorting,
highest-score ties, and the complete database menu. The tests did not modify
existing files or create a database in this assignment folder.
