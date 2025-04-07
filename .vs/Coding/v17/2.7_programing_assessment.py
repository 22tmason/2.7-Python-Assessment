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


def verify_phone_number(phone_number):
    """Verify phone number."""
    if phone_number.isdigit() and 8 <= len(phone_number) <= 15:
        return True
    else:
        print("Invalid phone number. Please enter a valid phone number (8-15 digits).")
        return False


def verify_postcode(postcode):
    """Verify postcode."""
    if postcode.isdigit() and 4 <= len(postcode) <= 6:
        return True
    else:
        print("Invalid postcode. Please enter a valid postcode (4-6 digits).")
        return False


def main_menu():
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
    while True:
        cls()
        print(f"{name} Department\n")
        print("0. Return to Main Menu")
        for index, item in enumerate(department, 1):
            print(f"{index}. {item[0]} - ${item[1]:.2f}")
        print("\nPlease select an item to add to your cart, or press 0 to return to the main menu.")
        choice = input_int("> ")

        if choice == 0:
            break
        elif 1 <= choice <= len(department):
            product, price = department[choice - 1]
            while True:
                cls()
                print(f"Product Selected: {product} - ${price:.2f}")
                print("Enter quantity (must be greater than 0):")
                quantity = input_int("> ")
                if quantity > 0:
                    break
                input("Quantity must be greater than 0, press enter to continue.")
            for item in cart:
                if item["name"] == product:
                    item["quantity"] += quantity
                    break
            else:
                cart.append({"name": product, "price": price, "quantity": quantity})
            input("Item added to cart. Press Enter to continue.")
        else:
            input("Invalid choice. Press Enter to try again.")




def create_delivery_address():
    global delivery_address
    delivery_address = {}

    while True:
        cls()
        print("Please enter your delivery information:")
        delivery_address["Full Name"] = input_string("Enter your full name: ")
        delivery_address["Street"] = input_string("Enter your street: ")
        delivery_address["Suburb"] = input_string("Enter your suburb: ")
        delivery_address["City"] = input_string("Enter your city: ")

        # Validate postcode
        while True:
            postcode = input_int("Enter your postcode: ")
            if verify_postcode(str(postcode)):
                delivery_address["Postcode"] = postcode
                break
            else:
                input("Invalid postcode. Press Enter to try again.")

        # Validate phone number
        while True:
            phone_number = input_string("Enter your phone number: ")
            if verify_phone_number(phone_number):
                delivery_address["Phone"] = phone_number
                break
            else:
                input("Invalid phone number. Press Enter to try again.")
        
        delivery_address["Country"] = input_string("Enter your country: ")

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
        print("1. Standard Delivery (3-5 days - $5 + $2 per item)")
        print("2. Express Delivery (1-2 days - $10 + $3 per item)")
        print("3. Pickup (Free)")	
        number = input_int("> ")

        if number == 1:
            delivery_cost = 5 + sum(item["quantity"] for item in cart) * 2
            delivery_method = "Standard Delivery"
            print(f"Delivery cost: ${delivery_cost:.2f}")	
            print("Would you like to proceed with this delivery method?")
            print("1. Yes")
            print("2. No")
            number = input_int("> ")
            if number == 1:
                create_delivery_address()
            else:
                continue
        elif number == 2:
            delivery_cost = 10 + sum(item["quantity"] for item in cart) * 3
            delivery_method = "Express Delivery"
            print(f"Delivery cost: ${delivery_cost:.2f}")	
            print("Would you like to proceed with this delivery method?")
            print("1. Yes")
            print("2. No")
            number = input_int("> ")
            if number == 1:
                create_delivery_address()
            else:
                continue
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
        print("0. Return")
        for index, item in enumerate(cart, 1):
            print(f"{index}. {item['name']} - Quantity: {item['quantity']}")

        choice = input_int("Select item to edit or 0 to return to cart menu: ")

        if choice == 0:
            break
        elif 1 <= choice <= len(cart):
            item = cart[choice - 1]
            while True:
                new_quantity = input_int(f"Enter new quantity for {item['name']} (0 to remove, must be >= 0): ")
                if new_quantity >= 0:
                    break
                print("Quantity must be greater than or equal to 0.")
            if new_quantity == 0:
                cart.pop(choice - 1)
            else:
                item['quantity'] = new_quantity
            input("Cart updated. Press Enter to continue.")
        else:
            input("Invalid option. Press Enter to try again.")



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



def main():
    while True:
        main_menu()

if __name__ == "__main__":
    main()