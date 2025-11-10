
# Retrieves and displays all records from the students table
def getAllStudents(database):

    try:
        cur = database.cursor()
        cur.execute("SELECT * FROM students;") #Executes command from pgAdmin
        for row in cur.fetchall():
            print(row)
        cur.close()
    
    # In case function fails
    except Exception as e:
        print(" Error retrieving students:", e)

# Inserts a new student record into the students table
def addStudent(database,first_name, last_name, email, enrollment_date):

    try:
        cur = database.cursor()
        #Executes command from pgAdmin
        cur.execute(""" 
                    INSERT INTO students (first_name, last_name, email, enrollment_date) 
                    VALUES (%s, %s, %s, %s);""",
                     (first_name, last_name, email, enrollment_date))   
        database.commit()
        cur.close()
        # Confirmation message
        print(f" Added student: {first_name} {last_name}")
    
    # In case function fails
    except Exception as e:
        print(" Error adding student record:", e)

# Updates the email address for a student with the specified student_id
def updateStudentEmail(database, student_id, new_email):

    try:
        cur = database.cursor()
        #Executes command from pgAdmin
        cur.execute("""
                    UPDATE students SET email = %s WHERE student_id = %s;
                    """, (new_email, student_id))
        database.commit()
        cur.close()
        # Confirmation message
        print(f" Updated student: SID[{student_id}] email to {new_email}")

    # In case function fails
    except Exception as e:
        print(" Error updating email", e)

# Deletes the record of the student with the specified student_id
def deleteStudent(database, student_id):

    try:

        cur = database.cursor()
        #Executes command from pgAdmin
        cur.execute("""
                    DELETE FROM students WHERE student_id = %s;
                    """, (student_id,))
        database.commit()
        cur.close()
        # Confirmation message
        print(f" Deleted Student: SID[{student_id}]")

    # In case function fails
    except Exception as e:
        print(" Error deleting record", e)