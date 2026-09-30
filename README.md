# AcaDex

A simple academic management system built using Python.

## Overview

AcaDex is a command-line application designed to help students manage basic academic information such as subjects, attendance, and assignments.

The application provides a simple menu-based interface through which users can record and view their academic information and check a summary through the dashboard.

## Features

### Subjects

* Add subjects
* View subjects

### Attendance

* Add or update attendance
* View attendance percentage for each subject
* Calculate overall attendance

### Assignments

* Add assignments
* View assignments
* Add subject and due-date information
* Mark assignments as completed

### Dashboard

* View total subjects
* View overall attendance
* View pending assignments
* View completed assignments

## Technologies Used

* Python 3
* Python Lists
* Python Dictionaries
* Functions
* Loops
* Conditional Statements
* Command Line Interface
* Modular Python Programming

## Project Structure

```text
AcaDex/
│
├── main.py
├── subjects.py
├── attendance.py
├── assignments.py
├── dashboard.py
├── data.py
│
├── README.md
├── statement.md
├── requirements.txt
└── .gitignore
```

## Requirements

* Python 3.x
* No external Python libraries are required.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AcaDex.git
```

### 2. Open the project directory

```bash
cd AcaDex
```

### 3. Run the program

```bash
python main.py
```

## How to Use

After starting the program, the main menu provides the following options:

```text
1. Subjects
2. Attendance
3. Assignments
4. Dashboard
5. Exit
```

Enter the number corresponding to the required option and follow the instructions displayed by the program.

## Testing

The application can be tested manually by running `main.py` and checking each module.

### Subject Testing

* Add one or more subjects.
* View the subject list.
* Try selecting an invalid menu option.

### Attendance Testing

* Add attendance for a subject.
* Check the calculated percentage.
* Test invalid attendance values such as attended classes being greater than total classes.

### Assignment Testing

* Add an assignment.
* View the assignment.
* Mark the assignment as completed.

### Dashboard Testing

* Check the total number of subjects.
* Check overall attendance.
* Check pending and completed assignment counts.

## Data Storage

The current version stores data temporarily in Python lists and dictionaries.

The data is not permanently saved after the program is closed.

## Future Enhancements

Possible future improvements include:

* Permanent data storage
* Database integration
* Assignment reminders
* Automatic due-date tracking
* Graphical user interface
* User login system
* More detailed academic statistics

## Author

**Your Name**

## Project Purpose

This project was developed as a beginner-level Python project to apply programming concepts such as functions, lists, dictionaries, loops, conditional statements, input handling, and modular programming.
