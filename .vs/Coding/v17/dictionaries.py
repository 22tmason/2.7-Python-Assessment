# Example of a Python dictionary
person = {
    "name": "Tyler",
    "age": 30,
    "location": "Gibbston, New Zealand",
    "hobbies": ["cycling", "photography", "hiking"]
}

# Accessing dictionary values
print(person["name"])  # Output: Tyler
print(person["hobbies"])  # Output: ['cycling', 'photography', 'hiking']

# Original dictionary
person = {
    "name": "Tyler",
    "age": 30,
    "location": "Gibbston, New Zealand",
    "hobbies": ["cycling", "photography", "hiking"]
}

# Appending a new hobby
person["hobbies"].append("cooking")

# Check the updated dictionary
print(person["hobbies"])  # Output: ['cycling', 'photography', 'hiking', 'cooking']

# Adding a new key-value pair
person["profession"] = "Graphic Designer"

# Check the updated dictionary
print(person)

# Original dictionary
person = {
    "name": "Tyler",
    "age": 30,
    "location": "Gibbston, New Zealand",
    "hobbies": ["cycling", "photography", "hiking"]
}

# Modifying an existing value
person["age"] = 31  # Changing age
person["location"] = "Queenstown, New Zealand"  # Updating location

# Check the updated dictionary
print(person)

# Modifying the list in the dictionary
person["hobbies"].remove("cycling")  # Removing an item
person["hobbies"].append("skiing")  # Adding a new item

# Check the updated hobbies
print(person["hobbies"])  # Output: ['photography', 'hiking', 'skiing']

# Create an empty dictionary
person = {}

# Get user input to populate the dictionary
person["name"] = input("Enter your name: ")
person["age"] = int(input("Enter your age: "))
person["location"] = input("Enter your location: ")
person["hobbies"] = input("Enter your hobbies (separated by commas): ").split(", ")

# Print the updated dictionary
print("\nYour information:")
print(person)

# Example dictionary
person = {
    "name": "Tyler",
    "age": 30,
    "location": "Gibbston, New Zealand",
    "hobbies": ["cycling", "photography", "hiking"]
}

# Printing the dictionary using a for loop
for key, value in person.items():
    print(f"{key}: {value}")
"""output:
name: Tyler
age: 30
location: Gibbston, New Zealand
hobbies: ['cycling', 'photography', 'hiking']
"""