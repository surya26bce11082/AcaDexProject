from storage import subjectlist, attendance_data

def attendance():
    while True:
        print("\n================================")
        print("          Attendance")
        print("================================")
        print("1. Add/Update Attendance")
        print("2. View Attendance")
        print("3. Back")
        print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            if len(subjectlist) == 0:
                print("\nPlease add subjects first.")
                continue

            print("\nYour Subjects:")
            number = 1
            for subject in subjectlist:
                print(f"{number}. {subject}")
                number += 1

            number = int(input("\nSelect a subject: "))

            if 1 <= number <= len(subjectlist):
                subject = subjectlist[number - 1]

                attended = int(input("Classes attended: "))
                total = int(input("Total classes: "))

                if attended > total:
                    print("Classes attended cannot be greater than total classes.")
                elif total <= 0:
                    print("Total classes must be greater than zero.")
                else:
                    attendance_data[subject] = {
                        "attended": attended,
                        "total": total
                    }

                    print(f"Attendance for {subject} updated.")
            else:
                print("Invalid subject number.")

        elif choice == "2":
            if len(attendance_data) == 0:
                print("\nNo attendance records yet.")
            else:
                print("\nYour Attendance:")

                for subject, data in attendance_data.items():
                    percentage = (data["attended"] / data["total"]) * 100

                    print(
                        f"{subject}: "
                        f"{data['attended']}/{data['total']} "
                        f"({percentage:.2f}%)"
                    )

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")

