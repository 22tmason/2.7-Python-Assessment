"""This is a program for a hardware store that allows users to order products from different departments."""

import os
"""The following 2d lists contain the products
and their prices for each department.
"""
hardware = [
    ["Hammer", 10.00],
    ["Screwdriver", 5.00],
    ["Nails", 3.00],
    ["Screws", 2.00],
    ["Drill", 50.00],
    ["Saw", 20.00],
    ["Measuring Tape", 5.00],
    ["Pliers", 7.00],
    ["Wrench", 8.00],
    ["Glue", 4.00]
]
homeware = [
    ["Mop", 10.00],
    ["Broom", 5.00],
    ["Dustpan", 3.00],
    ["Bucket", 2.00],
    ["Dish Rack", 10.00],
    ["Dish Cloth", 5.00],
    ["Dish Brush", 3.00],
    ["Sponge", 2.00],
    ["Trash Can", 20.00],
    ["Trash Bags", 5.00]
]
electrical = [
    ["Lightbulb", 5.00],
    ["Extension Cord", 10.00],
    ["Power Strip", 15.00],
    ["Batteries", 5.00],
    ["Flashlight", 10.00],
    ["Light Switch", 5.00],
    ["Outlet Cover", 2.00],
    ["Surge Protector", 20.00],
    ["Smoke Detector", 15.00],
    ["Carbon Monoxide Detector", 15.00]
]
paint = [
    ["Paintbrush", 5.00],
    ["Paint Roller", 10.00],
    ["Paint Tray", 5.00],
    ["Paint", 20.00],
    ["Primer", 10.00],
    ["Painter's Tape", 5.00],
    ["Drop Cloth", 5.00],
    ["Paint Thinner", 5.00],
    ["Paint Can Opener", 2.00],
    ["Sandpaper", 3.00]
]
# An empty list to store the user's cart.
cart = []


def cls():
    """Clear the console screen.

    This function uses the os module to clear the console screen.
    """
    # Check if the operating system is windows or not.
    os.system('cls' if os.name == 'nt' else 'clear')


def input_int(prompt):
    """Prompt the user for an integer input, with error handling with the try, except statements.

    This function will continue to prompt the user until a valid integer is entered.
    """
    # This loop will continue to run until the user enters a valid integer.
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def order_details():
    """Display the order details."""
    # This function is not used in the program, but it can be used to display the order details.
    print("Order Details:")
    for i in cart:
        print(i[0] + " - $" + str(i[1]))
    total = 0
    for i in cart:
        total += i[1]
    return total
    print("Your total is $" + str(total))
    input("Press enter to exit.")


def menu():
    """Display the main menu and allow the user to select a department or their cart."""
    # This function clears the console and displays the main menu.
    cls()
    # The following print statements display the main menu and the departments.
    print("Super Hardware Store\n")
    print("1. Hardware")
    print("2. Homeware")
    print("3. Paint")
    print("4. Electrical")
    print("5. Cart\n")
    print("Please select a department")
    number = input_int("> ")
    if number == 1:
        department_menu(hardware, "Hardware Department")
    elif number == 2:
        department_menu(homeware, "Homeware Department")
    elif number == 3:
        department_menu(paint, "Paint Department")
    elif number == 4:
        department_menu(electrical, "Electrical Department")
    elif number == 5:
        cart_menu()
    else:
        print("Invalid input. Please enter a number between 1 and 5")
        input("Press enter to continue.")


def department_menu(department, name):
    """Display following products in a certain department and allow the user to choose a product to the cart."""
    cls()
    print(name + "\n")
    counter = 0
    # The for loop prints each product in a new line.
    for i in department:
        # The counter variable is used to number the products.
        counter += 1
        # The following print statement displays the product name and price.
        print(str(counter) + ". " + i[0] + " - $" + str(i[1]))
    print("Enter the number of the product you would like to add to your cart:\n")
    # The input_int function is used to get the user's input and check if it is a valid number.
    number = input_int("> ")
    if number > 0 and number <= len(department):
        # The following print statement displays the product name and price.
        cart.append(department[number - 1])
    else:
        # If the user enters an invalid number, the following print statement is displayed.
        print("Invalid input. Please enter a number between 1 and " + str(len(department)))


def cart_menu():
    """Display the cart and allow the user to check out or continue shopping."""
    cls()
    if len(cart) == 0:
        print("Your cart is empty.")
    else:
        order_details()
    print("1. Check out")
    print("2. Continue Shopping")
    print("Would you like to check out or continue shopping?")
    number = input_int("> ")
    if number == 1:
        print("Thank you for shopping at Super Hardware Store!")
        order_details()
        input("Press enter to exit.")
    elif number == 2:
        return
    else:
        print("Invalid input. Please enter 1 or 2.")


while True:
    menu()
