from storage import assignment_data
def assignments():
    
    while True:
        print("\n================================")
        print("         Assignments")
        print("================================")
        print("1. Add Assignment")
        print("2. View Assignments")
        print("3. Mark as Completed")
        print("4. Back")
        print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter assignment name: ")
            subject = input("Enter subject: ")
            due_date = input("Enter due date (DD-MM-YYYY): ")

            assignment = {
                "name": name,
                "subject": subject,
                "due_date": due_date,
                "completed": False
            }

            assignment_data.append(assignment)

            print("\nAssignment added successfully.")

        elif choice == "2":
            if len(assignment_data) == 0:
                print("\nNo assignments added yet.")

            else:
                print("\nYour Assignments:")

                number = 1

                for assignment in assignment_data:
                    if assignment["completed"]:
                        status = "Completed"
                    else:
                        status = "Pending"

                    print(f"\n{number}. {assignment['name']}")
                    print(f"   Subject: {assignment['subject']}")
                    print(f"   Due: {assignment['due_date']}")
                    print(f"   Status: {status}")

                    number += 1

        elif choice == "3":
            if len(assignment_data) == 0:
                print("\nNo assignments available.")

            else:
                print("\nYour Assignments:")

                number = 1

                for assignment in assignment_data:
                    print(f"{number}. {assignment['name']}")
                    number += 1

                selected = int(input("\nEnter assignment number: "))

                if 1 <= selected <= len(assignment_data):
                    assignment_data[selected - 1]["completed"] = True
                    print("\nAssignment marked as completed.")

                else:
                    print("Invalid assignment number.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")