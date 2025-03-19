
# Import os for clearing the console.
import os
# Function to clear the console.
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# List to store student data.
students = []
year_level = []
credits_achieved = []
credits_merit = []
credits_excellence = []
# Function to get an integer input from the user, protects from crashes with try, expect.
def get_int(prompt):
    while True:
        try:
            return int(input("Enter " + prompt + ": "))
        except ValueError:
            print("Invalid input. Please enter a number.")
# Function to display the menu and call the appropriate function based on user input.
def menu():
    while True:
        clear()
        print("1. Show summary of all student data")
        print("2. Show students who passed NCEA")
        print("3. Show students eligible for an endorsement")
        print("4. Show summary by year level")
        print("5. Add credits to students")
        print("6. Add new students")

        option = input("Enter a number: ")
        if option == "1":
            summary_data_all_years()
        elif option == "2":
            pass_ncea()
        elif option == "3":
            endorsement()
        elif option == "4":
            summary_data_year()
        elif option == "5":
            add_credits()
        elif option == "6":
            add_new_students()
        else:
            print("Invalid option. Try again.")
        repeat = input("Press Enter to return to the menu or type 'no' to exit: ")
        if repeat.lower() == "no":
            print("Program finished.")
            break
# Function to display a summary of all student data.
def summary_data_all_years():
    clear()
    print("Summary of all student data:")
    for i in range(len(students)):
        print("Student name: " + [students[i]])
        print("Year level: " + (str[year_level[i]]))
        print("Achieved credits: " + (str[credits_achieved[i]]))
        print("Merit credits: " + (str[credits_merit[i]]))
        print("Excellence credits: " + (str[credits_excellence[i]]))
# Function to display students who have passed NCEA.
def pass_ncea():
    clear()
    print("Students who passed NCEA:")
    for i in range(len(students)):
        total_credits = credits_achieved[i] + credits_merit[i] + credits_excellence[i]
        if total_credits >= 60:
            print(f"{students[i]} - Total Credits: {total_credits}")
# Function to display students eligible for an endorsement.
def endorsement():
    clear()
    print("Students eligible for a Merit endorsement:")
    for i in range(len(students)):
        if credits_merit[i] + credits_excellence[i] >= 50:
            print(f"{students[i]} - Merit & Excellence Credits: {credits_merit[i] + credits_excellence[i]}")
    
    print("\nStudents eligible for an Excellence endorsement:")
    for i in range(len(students)):
        if credits_excellence[i] >= 50:
            print(f"{students[i]} - Excellence Credits: {credits_excellence[i]}")
# Function to display a summary of students by year level.
def summary_data_year():
    clear()
    year = get_int("the year level you want to see")
    print(f"\nSummary of students in Year {year}:")
    for i in range(len(students)):
        if year_level[i] == year:
            print(f"{students[i]} - Achieved: {credits_achieved[i]}, Merit: {credits_merit[i]}, Excellence: {credits_excellence[i]}")
# Function to add credits to existing students.
def add_credits():
    if students:
        clear()
        print("Add credits to existing students:")
        for i in range(len(students)):
            print(f"{i+1}. {students[i]}")

        student_name = input("Enter the student's name: ")
        if student_name in students:
            index = students.index(student_name)
            credits_achieved[index] += get_int("Achieved credits to add")
            credits_merit[index] += get_int("Merit credits to add")
            credits_excellence[index] += get_int("Excellence credits to add")
            print("\nCredits updated successfully.")
        else:
            print("Student not found.")
    else:
        print("No student data exists.")
# Function to add new students and their credit data.
def add_new_students():
    clear()
    print("Add new students and credit data:")
    student = input("Enter the student's name: ")
    students.append(student)
    year_level.append(get_int("year level"))
    credits_achieved.append(get_int("Achieved credits"))
    credits_merit.append(get_int("Merit credits"))
    credits_excellence.append(get_int("Excellence credits"))
    print("Student data added successfully.")
# Call the menu function to start the program.
menu()