import os

hardware = [["Hammer", 10.00], ["Screwdriver", 5.00], ["Nails", 3.00], ["Screws", 2.00], ["Drill", 50.00], ["Saw", 20.00], ["Measuring Tape", 5.00], ["Pliers", 7.00], ["Wrench", 8.00], ["Glue", 4.00]]
homeware = [["Mop", 10.00], ["Broom", 5.00], ["Dustpan", 3.00], ["Bucket", 2.00], ["Dish Rack", 10.00], ["Dish Cloth", 5.00], ["Dish Brush", 3.00], ["Sponge", 2.00], ["Trash Can", 20.00], ["Trash Bags", 5.00]]
electrical = [["Lightbulb", 5.00], ["Extension Cord", 10.00], ["Power Strip", 15.00], ["Batteries", 5.00], ["Flashlight", 10.00], ["Light Switch", 5.00], ["Outlet Cover", 2.00], ["Surge Protector", 20.00], ["Smoke Detector", 15.00], ["Carbon Monoxide Detector", 15.00]]
paint = [["Paintbrush", 5.00], ["Paint Roller", 10.00], ["Paint Tray", 5.00], ["Paint", 20.00], ["Primer", 10.00], ["Painter's Tape", 5.00], ["Drop Cloth", 5.00], ["Paint Thinner", 5.00], ["Paint Can Opener", 2.00], ["Sandpaper", 3.00]]
cart = []

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def menu():
    cls()
    print("Super Hardware Store\n")
    print("1. Hardware")
    print("2. Homeware")
    print("3. Paint")
    print("4. Electrical")
    print("5. Cart\n")
    print("Please select a department")

def department_menu(department, name):
    cls()
    print(name + "\n")
    counter = 0
    for i in department:
        counter += 1
        print(str(counter) + ". " + i[0] + " - $" + str(i[1]))
    print("Enter the number of the product you would like to add to your cart:")
    number = input_int("> ")
    if number > 0 and number <= len(department):
        cart.append(department[number - 1])
    else:
        print("Invalid input. Please enter a number between 1 and " + str(len(department)))

def cart_menu():
    cls()
    if len(cart) == 0:
        print("Your cart is empty.")
    else:
        total = 0
        print("Cart:")
        for i in cart:
            print(i[0] + " - $" + str(i[1]))
            total += i[1]
        print("Total: $" + str(total))
    print("1. Check out")
    print("2. Continue Shopping")
    print("Would you like to check out or continue shopping?")
    number = input_int("> ")
    if number == 1:
        print("Thank you for shopping at the Super Hardware Store!")
        print("Order Details:")
        for i in cart:
            print(i[0] + " - $" + str(i[1]))
        print("Your total is $" + str(total))
        input("Press enter to exit.")
    elif number == 2:
        return
    else:
        print("Invalid input. Please enter 1 or 2.")
while True:
    menu()
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
        break