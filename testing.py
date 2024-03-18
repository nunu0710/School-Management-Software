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



while True:

    #  Functions to create Users:

    def students_create():

        first_name = input("Enter student's first name? ")
        last_name = input("what's student last name? ")
        class_name = input("what is the student class? ")
        students_dict = {"first_name" : first_name , "last_name" : last_name, "class" : class_name }
        database["students"].append(students_dict)
        #print(database)

    def teachers_create():
        first_name = input("what is the teacher's first name? ")
        last_name = input("what's the teacher's last name? ")
        class_name = input (f"what does {first_name} teaches? ")
        subject_name = input(f"what subject does {first_name} {last_name} teaches?")
        teachers_dict = {"first_name" : first_name, "last_name": last_name, "subject": subject_name, "class_name": class_name}
        database["teachers"].append(teachers_dict)
        print(database)

    def home_room_teachers():
        first_name = input("what is the teacher's first name? ")
        last_name = input("what's the teacher's last name? ")
        class_name = input("what class does he teach? ")
        home_room_teach_dict = {"first_name": first_name, "last_name": last_name, "class_name":class_name}
        database["homeroom_teachers"].append(home_room_teach_dict)
        print(database)
        


    # Functions to manage the Users:
    
    def class_mgmt():
           class_name = input("What class do you want to display?\n")
           print("Students in this class are:")
           for student in database["students"]:
               if student["class"] == class_name:  
                  print(f"{student["first_name"]} {student["last_name"]}")

           for home_room_tech in database["homeroom_teachers"]:
               if home_room_tech["class"] == class_name:
                    print(f"Home room teacher for this class is: {home_room_tech["first_name"]} {home_room_tech["last_name"]}")


    def student_mgmt():
        student_first_name = input("enter the student first name please > ")
        student_last_name = input("enter the student last name please >")
        for student in database["students"]:
            if student["first_name"] == student_first_name and student["last_name"] == student_last_name:
                print(f"{student_first_name} {student_last_name} attends {student["class"]} class")

                for teacher in database["teachers"]:
                    if student["class"] in teacher["classes"]:
                        print(f"Teachers in this class is: {teacher["first_name"]} { teacher["last_name"]}")
                        


    def teachers_mgmt():
        teachers_first_name = input("enter teacher first name> ")
        teachers_last_name = input("enter teacher last name > ")
        for teacher in database["teachers"]:
            if teacher["first_name"] == teachers_first_name and teacher["last_name"] == teachers_last_name:
                print(teacher["classes"])


    

    def homeroom_teacher_mgmt():
        homeroomTeacher_first_name = input("Enter the home room teacher first name> ")
        homeroomTeacher_last_name = input("Enter the home room teacher last name> ")
        for homeRoomTeacher in database["homeroom_teachers"]:
           if homeRoomTeacher["first_name"] == homeroomTeacher_first_name and homeRoomTeacher["last_name"] == homeroomTeacher_last_name:
                    print (f"Students led by {homeRoomTeacher["first_name"]} {homeRoomTeacher["last_name"]} are :") 
        for student in database["students"]:
           if student["class"] == homeRoomTeacher["class"]:
                print(student["first_name"], student["last_name"])
                
                


    option = input("please choose one of the following options\n1. Create\n2. Manage\n3. End\n ")
    if option == "1" or option == "Create".lower():
        user = input("please chose one of the following users\n1. Students\n2. Teachers\n3. homeroom teachers\n")
        if user == "1" or option == "Students".lower():
            students_create()
        elif user == "2" or option == "teachers".lower():
            teachers_create()
        elif user == "3" or option == "homeroom teachers".lower():
            home_room_teachers()
        else:
            print("Invalid input, please choose the mentioned users")
            continue
    elif option == "2" or option == "manage".lower():
        option = input("Please pick which User do you want to manage (type in the number)\n1. class\n2. student\n3. teacher\n4. homeroom teacher\n ")
        if option == "1" or option == "class".lower():
            class_mgmt()
        elif option == "2" or option == "student".lower():
            student_mgmt()
            pass
        elif option == "3" or option == "teacher".lower():
            teachers_mgmt()
        elif option == "4" or option == "homeroom teacher".lower():
            homeroom_teacher_mgmt()
        else:
            print("Invalid input, please choose the mentioned users")
            
    elif option == "3" or option == "End".lower():
        break
    else:
        print("Invalid option")
        continue