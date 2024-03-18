# Define data structures to store users and their attributes
students = []
teachers = []
homeroom_teachers = []
database = {
    "students": [
        {"first_name": "John", "last_name": "Smith", "class": "3C"},
        {"first_name": "Anna", "last_name": "Purple", "class": "3C"},
        {"first_name": "Jan", "last_name": "Kowalski", "class": "4E"},
    ],
    "teachers": [
        {"first_name": "John", "last_name": "Smith", "subject": "math", "classes": ["3C", "4E"]},
    ],
    "homeroom_teachers": [
        {"first_name": "Jan", "last_name": "Kowalski", "class": "3C"},
    ]
}

# Function to create a student
def create_student():
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    class_name = input("Enter student's class name: ")
    students.append({"first_name": first_name, "last_name": last_name, "class_name": class_name})

# Function to create a teacher
def create_teacher():
    first_name = input("Enter teacher's first name: ")
    last_name = input("Enter teacher's last name: ")
    subjects = []
    while True:
        subject = input("Enter subject taught by the teacher (or leave blank to finish): ")
        if subject:
            subjects.append(subject)
        else:
            break
    teachers.append({"first_name": first_name, "last_name": last_name, "subjects": subjects})

# Function to create a homeroom teacher
def create_homeroom_teacher():
    first_name = input("Enter homeroom teacher's first name: ")
    last_name = input("Enter homeroom teacher's last name: ")
    class_name = input("Enter the class name the teacher leads: ")
    homeroom_teachers.append({"first_name": first_name, "last_name": last_name, "class_name": class_name})

# Function to manage classes
def manage_class():
    class_name = input("Enter class name to display: ")
    print("Students in class {}:".format(class_name))
    for student in students:
        if student["class_name"] == class_name:
            print("{} {}".format(student["first_name"], student["last_name"]))
    print("Homeroom teacher:")
    for teacher in homeroom_teachers:
        if teacher["class_name"] == class_name:
            print("{} {}".format(teacher["first_name"], teacher["last_name"]))

# Function to manage students
def manage_student():
    student_name = input("Enter student's first and last name: ")
    for student in students:
        if student["first_name"] + " " + student["last_name"] == student_name:
            print("Classes attended by {}: {}".format(student_name, student["class_name"]))
            print("Teachers:")
            for teacher in teachers:
                if student["class_name"] in teacher["subjects"]:
                    print("{} {}".format(teacher["first_name"], teacher["last_name"]))
            return
    print("Student not found.")

# Function to manage teachers
def manage_teacher():
    teacher_name = input("Enter teacher's first and last name: ")
    for teacher in teachers:
        if teacher["first_name"] + " " + teacher["last_name"] == teacher_name:
            print("Classes taught by {}: {}".format(teacher_name, ", ".join(teacher["subjects"])))
            return
    print("Teacher not found.")

# Function to manage homeroom teachers
def manage_homeroom_teacher():
    teacher_name = input("Enter homeroom teacher's first and last name: ")
    for teacher in homeroom_teachers:
        if teacher["first_name"] + " " + teacher["last_name"] == teacher_name:
            print("Students led by {}: {}".format(teacher_name, teacher["class_name"]))
            return
    print("Homeroom teacher not found.")

# Main function
def main():
    while True:
        print("Available commands: create, manage, end")
        command = input("Enter a command: ")

        if command == "create":
            print("Available user types: student, teacher, homeroom teacher, end")
            user_type = input("Enter a user type to create: ")

            if user_type == "student":
                create_student()
            elif user_type == "teacher":
                create_teacher()
            elif user_type == "homeroom teacher":
                create_homeroom_teacher()
            elif user_type == "end":
                continue
            else:
                print("Invalid user type.")

        elif command == "manage":
            print("Available options: class, student, teacher, homeroom teacher, end")
            option = input("Enter an option to manage: ")

            if option == "class":
                manage_class()
            elif option == "student":
                manage_student()
            elif option == "teacher":
                manage_teacher()
            elif option == "homeroom teacher":
                manage_homeroom_teacher()
            elif option == "end":
                continue
            else:
                print("Invalid option.")

        elif command == "end":
            print("Exiting program...")
            break

        else:
            print("Invalid command.")

# Call the main function to start the program
main()