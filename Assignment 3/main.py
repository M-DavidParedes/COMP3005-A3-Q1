import psycopg2
from A3_Q1_functions import getAllStudents, addStudent, updateStudentEmail, deleteStudent

def connect():
    try:
        #pgAdmin username and password
        database = psycopg2.connect(
            host="localhost",
            database="Assignment3-Q1",   
            user="postgres",           
            password="postgres"   
        )
        #Succesful connection
        print("Successfully connected to the database.")
        return database
    except Exception as e:
        #Unsuccesful connection
        print("Connection error:", e)
        return None

def menu(database):
    while True:
        print("\n--- MENU ---")
        print("1. View all students")
        print("2. Add a new student")
        print("3. Update a student's email")
        print("4. Delete a student")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '1':
            getAllStudents(database)
        elif choice == '2':
            first_name = input("First name: ")
            last_name = input("Last name: ")
            email = input("Email: ")
            enrollment_date = input("Enrollment date (YYYY-MM-DD): ")
            addStudent(database, first_name, last_name, email, enrollment_date)
        elif choice == '3':
            student_id = input("Student ID: ")
            new_email = input("New email: ")
            updateStudentEmail(database, student_id, new_email)
        elif choice == '4':
            student_id = input("Student ID to delete: ")
            deleteStudent(database, student_id)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

def main():
    database = connect()
    if database:
       menu(database)
       database.close()
       print("\n Database connection closed.")


if __name__ == "__main__":
    main()
