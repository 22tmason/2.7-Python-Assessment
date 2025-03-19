import os

heights = []
names = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_points():
    clear()
    name = input("Enter the name of the individual: ")
    height = int(input("Enter the height of the individual in cm: "))
    names.append(name)
    heights.append(height)

def calculate_statistics():
    clear()
    global heights, names
    avg_height = sum(heights) / len(heights)
    max_height = max(heights)        
    min_height = min(heights)
    print(f"The average height is: {avg_height:.2f} cm")
    print(f"The maximum height is: {max_height} cm")
    print(f"The minimum height is: {min_height} cm")
    input("Press enter to continue: ")

def project_heights():
    clear()
    for name, height in zip(names, heights):
        print(f"{name} will be {height + 5} cm tall next year")
    input("Press enter to continue: ")

def current_heights():
    clear()
    for name, height in zip(names, heights):
        print(f"{name} is {height} cm tall")
    input("Press enter to continue: ")

def main():
    while True:
        clear()
        print("Welcome to the Height Statistics Program")
        print("1. Add new data points")
        print("2. Calculate key statistics")
        print("3. Project future heights")
        print("4. Current heights")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_points()
            elif choice == 2:
                calculate_statistics()
            elif choice == 3:
                project_heights()
            elif choice == 4:
                current_heights()
            elif choice == 5:
                print("Thank you for using the Height Statistics Program")
                break
            else:
                print("Invalid choice, please try again")
        except ValueError:
            print("Invalid choice, please try again")

main()