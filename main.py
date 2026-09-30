# print("__________________________________________________")
# print("..................................................")
# print("             Welcome to AcaDex!")
# print(" This is a simple academic management system.")
# print("__________________________________________________")

# print("=>1. Subjects")
# print("=>2. Attendance")
# print("=>3. Assignments")
# #print("4. Tasks")
# print("=>4. Dashboard")
# print("=>5. Exit")
# print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^")

from subjects import subjects
from assisgnments import assignments
from attendance import attendance
from dashboard import dashboard

    



while True:
    print("__________________________________________________")
    print("..................................................")
    print("             Welcome to AcaDex!")
    print(" This is a simple academic management system.")
    print("__________________________________________________")

    print("=>1. Subjects")
    print("=>2. Attendance")
    print("=>3. Assignments")
    #print("4. Tasks")
    print("=>4. Dashboard")
    print("=>5. Exit")
    print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^")

    choice = input("Please select an option (1-5): ")
    if choice == "1":
        subjects()
    elif choice == "2":
        attendance()
    elif choice == "3":
        assignments()
    elif choice == "4":
        dashboard()
    elif choice == "5":
        print("Exiting AcaDex. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
        input("\nPress Enter to return to the main menu...")
        
    

