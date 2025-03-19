def display_menu():
    print("\nNCEA Student Data System")
    print("1. Show all student data")
    print("2. Show students who have passed NCEA")
    print("3. Show students eligible for an endorsement")
    print("4. Show students by year level")
    print("5. Add credits to a student")
    print("6. Add a new student")
    print("7. Exit")

def show_all_students(students):
    print("\nAll Student Data:")
    for student in students:
        print(f"{student[0]} (Year {student[1]}): A{student[2]} M{student[3]} E{student[4]}")

def show_passed_students(students):
    print("\nStudents who have passed NCEA:")
    for student in students:
        if sum(student[2:]) >= 80:
            print(f"{student[0]} (Year {student[1]})")

def show_endorsed_students(students):
    print("\nStudents eligible for an endorsement:")
    for student in students:
        if student[4] >= 50:
            print(f"{student[0]} (Year {student[1]} is eligible for an Excellence endorsement)")
        elif student[3] + student[4] >= 50:
            print(f"{student[0]} (Year {student[1]} is eligible for a Merit endorsement)")
        else:
            print(f"{student[0]} (Year {student[1]} is not eligible for an endorsement)")

def show_students_by_year(students, year):
    print(f"\nStudents in Year {year}:")
    for student in students:
        if student[1] == year:
            print(f"{student[0]}: A{student[2]} M{student[3]} E{student[4]}")

def add_credits(students):
    name = input("Enter student name: ")
    for student in students:
        if student[0].lower() == name.lower():
            a = int(input("Enter additional Achieved credits: "))
            m = int(input("Enter additional Merit credits: "))
            e = int(input("Enter additional Excellence credits: "))
            student[2] += a
            student[3] += m
            student[4] += e
            print("Credits added successfully.")
            return
    print("Student not found.")

def add_student(students):
    name = input("Enter student name: ")
    year = int(input("Enter year level: "))
    a = int(input("Enter Achieved credits: "))
    m = int(input("Enter Merit credits: "))
    e = int(input("Enter Excellence credits: "))
    students.append([name, year, a, m, e])
    print("Student added successfully.")

def main():
    students = [
        ["Alice Brown", 11, 30, 20, 10],
        ["Bob Smith", 12, 40, 25, 15],
        ["Charlie Doe", 13, 50, 30, 20]
    ]
    
    while True:
        display_menu()
        choice = input("Select an option (1-7): ")
        
        if choice == "1":
            show_all_students(students)
        elif choice == "2":
            show_passed_students(students)
        elif choice == "3":
            show_endorsed_students(students)
        elif choice == "4":
            year = int(input("Enter year level: "))
            show_students_by_year(students, year)
        elif choice == "5":
            add_credits(students)
        elif choice == "6":
            add_student(students)
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid option, please try again.")

main()