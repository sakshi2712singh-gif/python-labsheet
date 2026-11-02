MCA101P-AS10 - Lab Sheet 07
Python File Handling: Read and Write Operations

This folder contains a separate Python program for each of the 30 questions in
the assignment. The scripts use Python's standard library only.

Run a program
-------------
Open a terminal in this folder and run an individual script, for example:

    python Q01_create_write_text.py
    python Q22_read_csv.py

Most programs use the included sample file when you press Enter at the filename
prompt. Relative filenames are resolved from this folder. Programs that create
output files use exclusive creation so they do not overwrite existing work;
choose another filename if the default output already exists.

Question map
------------
Q01 create and write a text file
Q02 read all text
Q03 read text line by line
Q04 count words
Q05 count lines and characters
Q06 display even-numbered lines
Q07 write multiple entered lines
Q08 append to an existing text file
Q09 copy a text file
Q10 display uppercase text
Q11 search for a word
Q12 count whole-word occurrences
Q13 sum and average numbers in a file
Q14 display the longest line
Q15 replace a word and save to a new file
Q16 display the first and last lines
Q17 remove blank lines into a new file
Q18 save unique words to a new file
Q19 sort words into a new file
Q20 merge two text files into a new file
Q21 create a CSV file with student records
Q22 read and display a CSV file
Q23 calculate averages for numeric CSV columns
Q24 count CSV data rows and columns
Q25 append a student record to a CSV file
Q26 copy a CSV file
Q27 display Name and Marks columns
Q28 find the highest mark, including ties
Q29 search a CSV record by student name
Q30 combine CSV files with matching headers

Included sample data
--------------------
sample_text.txt, second_text.txt, sample_numbers.txt,
sample_students.csv, sample_students_2.csv, append_target.txt, and
appendable_students.csv.

Q08 appends to append_target.txt and Q25 appends to appendable_students.csv.
Those two sample files are intentionally changed when their exercises are run.
Q15 and the other copy/clean/sort exercises write to separate output files,
leaving their source files unchanged.

Execution report
----------------
All 30 programs were run with sample inputs under Python 3.14.6. They each
produced the expected output. Additional checks confirmed that text copying
preserved the source contents, word replacement left its source unchanged,
merging included both source files, CSV copying preserved the records, CSV
combining produced six data rows, and CSV appending added the requested record.
Tests ran from an isolated temporary copy, so the sample data in this folder
was not changed during verification.
