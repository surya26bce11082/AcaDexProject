from storage import subjectlist





def subjects():
    while True:
        print("-------------------------------")
        print("Subjects Menu")
        print("->1. Add Subject")
        print("->2. View Subjects")
        print("->3. Back to Main Menu")
        print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            subject_name = input("Enter subject name: ")
            subjectlist.append(subject_name)
            print(f"Subject '{subject_name}' added successfully.")
        elif choice == "2":
            if len(subjectlist) == 0:
                print("No subjects found.")
            else:
                print("Subjects:")
                print(subjectlist)

        elif choice == "3":
            return
        else:
            print("invalid choice, try again!")
    
