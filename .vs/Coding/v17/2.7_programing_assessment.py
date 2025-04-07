"""This is a program for a hardware store that allows users to order products from different departments."""

import os
import sys
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
        sys.exit()
    else:
        print("Invalid input. Please enter a number between 1 and 6")
        input("Press enter to continue.")


def department_menu(department, name):
    """Display following products in a certain department and allow the user to choose a product to the cart."""
    while True:
        cls()
        print(name + "\n")
        for index, item in enumerate(department, 1):
            print(f"{index}. {item[0]} - ${item[1]}")
        print("\nEnter the number of the product you would like to add to your cart:")
        number = input_int("> ")

        if 1 <= number <= len(department):
            selected_product = department[number - 1]
            cls()
            print(f"Product Selected: {selected_product[0]}")
            print("Enter the quantity you would like to add to your cart: ")
            quantity = input_int(">")

            # Check if the item is already in the cart, if so, update the quantity instead of adding a new item.
            for item in cart:
                if item["name"] == selected_product[0]:
                    item["quantity"] += quantity
                    break
            else:
                # Add new item
                cart.append({
                    "name": selected_product[0],
                    "price": selected_product[1],
                    "quantity": quantity
                })
            print("Product added to cart.")
            print(f"Name: {selected_product[0]}")
            print(f"Price: ${selected_product[1]}")
            print(f"Quantity: {quantity}")
            print("Please select an option:")
            print("1. Return to department menu")
            print("2. Return to main menu")
            number = input_int("> ")
            if number == 1:
                continue
            elif number == 2:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 2.")
                input("Press enter to return to department menu.")
        else:
            print("Invalid input. Please enter a valid product number.")
            input("Press enter to continue.")



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
    global delivery_address
    delivery_cost = 0.00
    delivery_method = "N/A"

    cls()
    if len(cart) == 0:
        print("Your cart is empty.")
        input("Press enter to continue shopping.")
        return
    else:
        while True:
            cls()
            order_details(delivery_cost, delivery_method, delivery_address)
            print("\nCart Menu:")
            print("1. Check out")
            print("2. Edit Cart")
            print("3. Continue Shopping")
            number = input_int("> ")
            if number == 1:
                checkout(delivery_cost, delivery_method)
                return
            elif number == 2:
                edit_cart()
            elif number == 3:
                return
            else:
                input("Invalid input. Press enter to try again.")


def checkout(delivery_cost, delivery_method):
    global delivery_address

    while True:
        cls()
        print("Select a delivery option:")
        print("1. Standard Delivery")
        print("2. Express Delivery")
        print("3. Pickup")
        number = input_int("> ")

        if number == 1:
            delivery_cost = 5 + sum(item["quantity"] for item in cart) * 2
            delivery_method = "Standard Delivery"
            create_delivery_address()
        elif number == 2:
            delivery_cost = 10 + sum(item["quantity"] for item in cart) * 3
            delivery_method = "Express Delivery"
            create_delivery_address()
        elif number == 3:
            delivery_cost = 0
            delivery_method = "Pickup"
        else:
            input("Invalid input. Press enter to return to delivery method menu.")
            continue

        cls()
        order_details(delivery_cost, delivery_method, delivery_address)
        print("\nPlease select an option:")
        print("1. Confirm Order")
        print("2. Change Delivery Method and Address")
        print("3. Cancel Order")
        number = input_int("> ")

        if number == 1:
            print("Thank you for your order!")
            input("Press enter to return to main menu.")
            cart.clear()
            break
        elif number == 2:
            continue
        elif number == 3:
            print("Order cancelled.")
            input("Press enter to return.")
            break
        else:
            input("Invalid input. Press enter to return to delivery menu.")



def edit_cart():
    while True:
        cls()
        print("Edit Cart\n")
        if not cart:
            print("Your cart is empty.")
            input("Press enter to return.")
            return

        for idx, item in enumerate(cart, 1):
            print(f"{idx}. {item['name']} - Quantity: {item['quantity']} - ${item['price']} each")

        print("\nSelect an option:")
        print("1. Change item quantity")
        print("2. Remove an item")
        print("3. Return to previous menu")
        choice = input_int("> ")

        if choice == 1:
            item_num = input_int("Enter the item number to change quantity: ")
            if 1 <= item_num <= len(cart):
                new_qty = input_int("Enter the new quantity (0 to remove): ")
                if new_qty <= 0:
                    cart.pop(item_num - 1)
                    print("Item removed.")
                else:
                    cart[item_num - 1]["quantity"] = new_qty
                    print("Quantity updated.")
            else:
                print("Invalid item number.")
            input("Press enter to continue.")
        elif choice == 2:
            item_num = input_int("Enter the item number to remove: ")
            if 1 <= item_num <= len(cart):
                cart.pop(item_num - 1)
                print("Item removed from cart.")
            else:
                print("Invalid item number.")
            input("Press enter to continue.")
        elif choice == 3:
            return
        else:
            input("Invalid input. Press enter to try again.")


def order_details(delivery_cost, delivery_method, delivery_address):
    total = 0.00
    gross_total = 0.00
    
    print("Order Details:")
    print(" - Delivery Method: " + delivery_method)
    print(" - Delivery Address:")
    for key, value in delivery_address.items():
        print(f"   * {key}: {value}")
    
    print(" - Products in your cart:")
    for item in cart:
        subtotal = item["price"] * item["quantity"]
        print(f"   * {item['name']} x{item['quantity']} - ${item['price']} each | Subtotal: ${subtotal:.2f}")
        total += subtotal

    print()
    gross_total = total + delivery_cost
    print(" - Total cost of products: $" + f"{total:.2f}")
    print(" - Delivery cost: $" + f"{delivery_cost:.2f}")
    print(" - Gross total: $" + f"{gross_total:.2f}")



while True:
    menu()
