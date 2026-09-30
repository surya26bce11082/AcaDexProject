from storage import subjectlist, attendance_data, assignment_data
def dashboard():
    
    print("\n================================")
    print("           Dashboard")
    print("================================")

    print(f"\nTotal Subjects: {len(subjectlist)}")

    if len(attendance_data) == 0:
        print("Attendance: No records yet")
    else:
        total_attended = 0
        total_classes = 0

        for subject in attendance_data:
            attended = int(attendance_data[subject]["attended"])
            total = int(attendance_data[subject]["total"])

            total_attended += attended
            total_classes += total

        overall_percentage = (total_attended / total_classes) * 100

        print(f"Overall Attendance: {overall_percentage:.2f}%")

    pending = 0
    completed = 0

    for assignment in assignment_data:
        if assignment["completed"]:
            completed += 1
        else:
            pending += 1

    print(f"Assignments Pending: {pending}")
    print(f"Assignments Completed: {completed}")
    input("\nPress Enter to return to the main menu...")