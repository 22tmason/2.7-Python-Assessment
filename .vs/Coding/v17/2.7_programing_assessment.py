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

delivery_address = {}

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

def input_string(prompt):
    """Prompt the user for a string input.

    This function will continue to prompt the user until a valid string is entered.
    """
    # This loop will continue to run until the user enters a valid string.
    while True:
        try:
            return str(input(prompt)).strip()
        except ValueError:
            print("Invalid input. Please enter a string.")

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
    print("5. Cart")
    print("6. Exit\n")
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
    elif number == 6:
        exit()
    else:
        print("Invalid input. Please enter a number between 1 and 6")
        input("Press enter to continue.")


def department_menu(department, name):
    """Display following products in a certain department and allow the user to choose a product to the cart."""
    cls()
    while True:
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
            print(department[number - 1][0] + " has been added to your cart.")
            input("Press enter to continue.")
        else:
            # If the user enters an invalid number, the following print statement is displayed.
            print("Invalid input. Please enter a number between 1 and " + str(len(department)))
            print("Press enter to return to the department menu.")


def create_delivery_address():
    global delivery_address
    delivery_address = {}
    """Prompt the user to enter their delivery address."""
    # This function will prompt the user to enter their delivery address.
    # The while loop will continue to run until the user enters a valid address.
    while True:
        cls()
        print("Please enter your delivery information:")
        delivery_address["Full Name"] = input_string("Enter your full name: ")
        delivery_address["Street"] = input_string("Enter your street: ")
        delivery_address["Suburb"] = input_string("Enter your suburb: ")
        delivery_address["City"] = input_string("Enter your city: ")
        delivery_address["Postcode"] = input_int("Enter your postcode: ")
        delivery_address["Country"] = input_string("Enter your country: ")
        delivery_address["Phone"] = input_int("Enter your phone number: ")
    
        cls()
        print("Delivery Address:")
        for key, value in delivery_address.items():
            print(f"{key}: {value}")
        print("Confirm the address?")
        print("1. Yes")
        print("2. No")
        number = input_int("> ")
        if number == 1:
            break
        elif number == 2:
            continue
        else:
            input("Invalid input. Press enter to return to address delivery menu.")

    return delivery_address
    

def cart_menu():
    """Display the cart and allow the user to check out or continue shopping."""
    global delivery_address
    delivery_cost = 0.00
    delivery_method = "N/A"

    cls()
    if len(cart) == 0:
        print("Your cart is empty.")
        input("Press enter to continue shopping.")
    else:
        order_details(delivery_cost, delivery_method, delivery_address)
        print("Please select an option:")
        print("1. Check out")
        print("2. Continue Shopping")
        number = input_int("> ")
        if number == 1:
            while True:
                cls()
                print("Select a delivery option:")
                print("1. Standard Delivery")
                print("2. Express Delivery")
                print("3. Pickup")
                number = input_int("> ")
                if number == 1:
                    delivery_cost = 5 + len(cart) * 2
                    delivery_method = "Standard Delivery"
                    create_delivery_address()
                elif number == 2:
                    delivery_cost = 10 + len(cart) * 3
                    delivery_method = "Express Delivery"
                    create_delivery_address()
                elif number == 3:
                    delivery_cost = 0
                    delivery_method = "Pickup"
                else:
                    input("Invalid input. Press enter to return to delivery method menu.")
                    
                cls()
                order_details(delivery_cost, delivery_method, delivery_address)
                print("Please select an option:")
                print("1. Confirm Order")
                print("2. Change Delivery Method and Address")
                print("3. Cancel Order")
                number = input_int("> ")
                cls()
                if number == 1:
                    print("Thank you for your order!")
                    order_details(delivery_cost, delivery_method, delivery_address)
                    input("Press enter to continue.")
                    break
                elif number == 2:
                    continue
                elif number == 3:
                    print("Order cancelled.")
                    input("Press enter to continue.")
                    return
                else:
                    input("Invalid input. Press enter to return to delivery method menu.")

        elif number == 2:
            return
        else:
            input("Invalid input. Please enter to return to delivery method menu.")


def order_details(delivery_cost, delivery_method, delivery_address):
    """Display the order details."""
    # This function is not used in the program, but it can be used to display the order details.
    total = 0.00
    gross_total = 0.00
    
    print("Order Details:")
    print(" - Delivery Method: " + delivery_method)
    print(" - Delivery Address:")
    for key, value in delivery_address.items():
        print(f"   * {key}: {value}")
    print(" - Products in your cart:")
    for i in cart:
        print("   * " + i[0] + " - $" + str(i[1]))
    for i in cart:
        total = total + i[1]
    print()
    gross_total = total + delivery_cost
    print(" - Total cost of products: $" + str(total))
    print(" - Delivery cost: $" + str(delivery_cost))
    print(" - Gross total: $" + str(gross_total))


while True:
    menu()
