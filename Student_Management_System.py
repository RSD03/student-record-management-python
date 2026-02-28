"""
Project: Student Record Management System
Description:
This is a menu-driven Python program that allows users to:
1. Add student records
2. View all student records
3. Search a student by roll number
4. Delete a student record

Data is stored persistently in a text file (students.txt).
Concepts used:
- Lists
- Loops
- Conditional statements
- File handling (read/write)
- String manipulation
"""

FILE_NAME = "students.txt"


# Function to add a student record
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{marks}\n")

    print("Student added successfully.\n")


# Function to view all students
def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

            if not records:
                print("No records found.\n")
                return

            print("\nStudent Records:")
            for record in records:
                roll, name, marks = record.strip().split(",")
                print(f"Roll: {roll}, Name: {name}, Marks: {marks}")
            print()

    except FileNotFoundError:
        print("No records found.\n")


# Function to search student by roll number
def search_student():
    roll_search = input("Enter roll number to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            for record in file:
                roll, name, marks = record.strip().split(",")
                if roll == roll_search:
                    print(f"Found: Roll: {roll}, Name: {name}, Marks: {marks}\n")
                    return

        print("Student not found.\n")

    except FileNotFoundError:
        print("No records found.\n")


# Function to delete student record
def delete_student():
    roll_delete = input("Enter roll number to delete: ")
    updated_records = []

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        found = False
        for record in records:
            roll, name, marks = record.strip().split(",")
            if roll != roll_delete:
                updated_records.append(record)
            else:
                found = True

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_records)

        if found:
            print("Student deleted successfully.\n")
        else:
            print("Student not found.\n")

    except FileNotFoundError:
        print("No records found.\n")


# Main Menu
while True:
    print("===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.\n")