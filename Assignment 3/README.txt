# Assignment 3 - Question 1

# Setup Instructions

1. Create a PostgreSQL database named 'Assignment3-Q1'

2. Run the Database Schema, and the Initial Data onto pgAdmin

3. Created python code with all required functions:
- getAllStudents()
- addStudent(first_name, last_name, email, enrollment_date)
- updateStudentEmail(student_id, new_email)
- deleteStudent(student_id)

4. Install psycopg2

5. main.py contains the necesarry code to connect to pgAdmin including username and password

6. main.py contains def(menu) which is the menu to select from and use any of the 4 functions made. 
Typing a choice from (1-5) will select the function. Adding a new student will prompt you with the first name, last name, email, and enrollment date
which will be taken as parameters for addStudent(). Similiar functionality will occur with updateStudentEmail (prompt user for parameters).
deleteStudent() prompts the user for the SID (student ID of the desired student) and will delete the student based on the SID accordingly.
When done with adding, updating, and deleting data from the database, '5' will exit the program.

7. Vimeo Video Link: https://vimeo.com/1135239914?fl=ip&fe=ec 