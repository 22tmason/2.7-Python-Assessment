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

# A list to store the items in the cart.
# Each item is a dictionary with the product name, price, and quantity.
cart = []
# A dictionary to store the delivery address information.
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
        # The try block attempts to convert the user input to an integer.
        try:
            return int(input(prompt))
        # If a ValueError occurs (e.g., if the input is not a number), the except block will execute.
        except ValueError:
            print("Invalid input. Please enter a number.")


def input_string(prompt):
    """Prompt the user for a string input.

    This function will continue to prompt the user until a valid string is entered.
    """
    # This loop will continue to run until the user enters a valid string.
    while True:
        # The try block attempts to convert the user input to a string.
        try:
            return str(input(prompt)).strip()
        # If a ValueError occurs (e.g., if the input is not a string), the except block will execute.
        # strip() is used to remove any leading or trailing whitespace from the input.
        except ValueError:
            print("Invalid input. Please enter a string.")


def verify_phone_number(phone_number):
    """Verify phone number."""
    # Check if the phone number is a digit and its length is between 8 and 15.
    if phone_number.isdigit() and 8 <= len(phone_number) <= 15:
        # Check if the first digit is not 0.
        return True
    # If the phone number is not valid, an error message will be shown to the user.
    else:
        print("Invalid phone number. Please enter a valid phone number (8-15 digits).")
        return False


def verify_postcode(postcode):
    """Verify postcode."""
    # Check if the postcode is a digit and its length is between 4 and 6.

    if postcode.isdigit() and 4 <= len(postcode) <= 6:
        return True
    else:
        # If the postcode is not valid, an error message will be shown to the user.
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
    # The following line prompts the user for input and stores it in the variable 'number'.
    # The input is expected to be an integer, the input_int function stops the program from crashing if the user enters a string.
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
    """Display the department menu and allow the user to select an item to add to their cart."""
    # This function clears the console and displays the department menu.
    while True:
        # The cls function is called to clear the console.
        cls()
        print(f"{name} Department\n")
        print("0. Return to Main Menu")
        # The for loop is used to display the items in the department and their prices.
        # The enumerate function is used to get the index and item from the department list.
        # The index is used to display the item number.
        # The item is a list containing the product name and price.
        for index, item in enumerate(department, 1):
            # The print statement displays the item number, product name, and price.
            # The price is formatted to 2 decimal places using the :.2f format specifier.
            print(f"{index}. {item[0]} - ${item[1]:.2f}")
        # The following print statement prompts the user to select an item or return to the main menu.
        print("\nPlease select an item to add to your cart, or press 0 to return to the main menu.")
        # The following line prompts the user for input and stores it in the interger variable, choice.
        choice = input_int("> ")
        if choice == 0:
            # If the user selects 0, the function will break out of the loop and return to the main menu.
            break
        # If the user selects a valid item number, the product and price are retrieved from the department list.
        elif 1 <= choice <= len(department):
            # The product and price are retrieved from the department list using the choice - 1 index, this is because lists start at 0.
            product, price = department[choice - 1]
            while True:
                cls()
                print(f"Product Selected: {product} - ${price:.2f}")
                print("Enter quantity (must be greater than 0):")
                quantity = input_int("> ")
                # if statement checks if the quantity is greater than 0.
                if quantity > 0:
                    break
                # If the quantity is not greater than 0, there will be an error message is displayed and the user is prompted to enter a valid quantity.
                input("Quantity must be greater than 0, press enter to continue.")
            # for loop checks if the product is already in the cart.
            for item in cart:
                # If the product is already in the cart, the quantity is updated.
                if item["name"] == product:
                    # The quantity is updated by adding the new quantity to the existing quantity.
                    item["quantity"] += quantity
                    break
            else:
                # If the product is not in the cart, it is added to the cart as a dictionary with the product name, price, and quantity.
                cart.append({"name": product, "price": price, "quantity": quantity})
            input("Item added to cart. Press Enter to continue.")
        else:
            input("Invalid choice. Press Enter to try again.")


def create_delivery_address():
    """Create a delivery address for the user."""
    # Global variable so that the delivery address can be accessed in other functions.
    global delivery_address
    # The delivery address is a dictionary that will store the user's delivery information.
    delivery_address = {}

    while True:
        cls()
        print("Please enter your delivery information:")
        # The input_string function is used to get the user's full name, street, suburb, city, and country.
        delivery_address["Full Name"] = input_string("Enter your full name: ")
        delivery_address["Street"] = input_string("Enter your street: ")
        delivery_address["Suburb"] = input_string("Enter your suburb: ")
        delivery_address["City"] = input_string("Enter your city: ")

        # Verifies the user's postcode
        while True:
            # The input_int function is used to get the user's postcode as an integer.
            postcode = input_int("Enter your postcode: ")
            # The verify_postcode function checks if the postcode is valid.
            if verify_postcode(str(postcode)):
                delivery_address["Postcode"] = postcode
                break
            else:
                input("Invalid postcode. Press Enter to try again.")

        # Verifys the user's phone number, simlar to the postcode verification.
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
        # The following print statement displays the delivery address information.
        for key, value in delivery_address.items():
            # The for loop iterates over the delivery address dictionary and prints each key-value pair.
            # The key is the field name (e.g., "Full Name", "Street", etc.) and the value is the user's input.
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
    # The delivery address is returned as a dictionary.
    # This allows the delivery address to be accessed in other functions.
    return delivery_address


def cart_menu():
    """Display the cart menu and allow the user to check out or edit their cart."""
    # This function clears the console and displays the cart menu.
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
    """Checkout process for the cart."""
    # This function handles the checkout process for the cart.
    global delivery_address

    while True:
        cls()
        print("Select a delivery option:")
        print("1. Standard Delivery (3-5 days - $5.00 + $2.00 per item)")
        print("2. Express Delivery (1-2 days - $10.00 + $3.00 per item)")
        print("3. Pickup (Free)")	
        number = input_int("> ")

        if number == 1:
            # Calculate the delivery cost based on the number of items in the cart.
            # Sums the quantity of all items in the cart and multiply by $2.00.
            delivery_cost = 5 + sum(item["quantity"] for item in cart) * 2
            delivery_method = "Standard Delivery"
            print(f"Delivery cost: ${delivery_cost:.2f}")	
            print("Would you like to proceed with this delivery method?")
            print("1. Yes")
            print("2. No")
            number = input_int("> ")
            if number == 1:
                # Calls the create_delivery_address function to get the user's delivery address.
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
    """Edit the items in the cart."""
    # This function allows the user to edit the items in their cart.
    while True:
        cls()
        print("0. Return")
        for index, item in enumerate(cart, 1):
            print(f"{index}. {item['name']} - Quantity: {item['quantity']}")

        choice = input_int("Select item to edit or 0 to return to cart menu: ")

        if choice == 0:
            break
        # Checks if the choice is a valid index in the cart.
        elif 1 <= choice <= len(cart):
            # The item is retrieved from the cart using the choice - 1 index.
            item = cart[choice - 1]
            while True:
                # The user is prompted to enter a new quantity for the selected item.
                new_quantity = input_int(f"Enter new quantity for {item['name']} (0 to remove): ")
                if new_quantity >= 0:
                    break
                print("Quantity must be greater than or equal to 0.")
            if new_quantity == 0:
                # If the new quantity is 0, the item is removed from the cart.
                cart.pop(choice - 1)
            else:
                # If the new quantity is valid, the item's quantity is updated to the new quantity.
                item['quantity'] = new_quantity
            input("Cart updated. Press Enter to continue.")
        else:
            input("Invalid option. Press Enter to try again.")


def order_details(delivery_cost, delivery_method, delivery_address):
    """Display the order details."""
    # This function displays the order details, including the delivery method, delivery address, products in the cart, and total cost.
    total = 0.00
    gross_total = 0.00
    
    print("Order Details:")
    print(" - Delivery Method: " + delivery_method)
    print(" - Delivery Address:")
    for key, value in delivery_address.items():
        print(f"   * {key}: {value}")
    
    print(" - Products in your cart:")
    for item in cart:
        # The subtotal is calculated by multiplying the price by the quantity for each different product in the cart.
        subtotal = item["price"] * item["quantity"]
        print(f"   * {item['name']} x{item['quantity']} - ${item['price']} each | Subtotal: ${subtotal:.2f}")
        total += subtotal

    print()
    gross_total = total + delivery_cost
    print(" - Total cost of products: $" + f"{total:.2f}")
    print(" - Delivery cost: $" + f"{delivery_cost:.2f}")
    print(" - Gross total: $" + f"{gross_total:.2f}")
 
def main():
    """Main function to run the program."""
    while True:
        main_menu()

if __name__ == "__main__":
    main()