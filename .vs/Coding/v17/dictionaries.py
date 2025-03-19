#create a dictionary
student = {
    "name": "John",
    "age": 17,
    "grade": "A"
}
# prints the whole dictionary
print("Student Info:", student)

# accessing data from the using keys
print("Name:", student["name"]) # Accessing the value assicted with the key 'name'

# using the get() method to safely access the value of a key
print("School:", student.get("school", "Not assigned"))

# Adding a new key-value pair
student["school"] = "High School"
print("Updated Student Info:", student)

# USing keys, you can retiieve a value by speifying its key in square brackets.
print(student["grade"])

#using get() method is useful because you can specify a default value to return if the key does not exist.
print(student.get("age", "age not found"))

#Checking for Keys: Use the in keyword to check if a key exists.
if "name" in student:
    print("Name is in the dictionary!")

"""
When to Use Dictionaries vs. Lists
Dictionaries:
Best for: Situations where you want to associate a unique key with a value (e.g., a phonebook, where names map to phone numbers).
Access: Data is accessed using keys, which makes lookups very fast.
Lists:
Best for: When you need an ordered collection of items, such as a sequence of numbers or a list of names.
Access: Items are accessed by their position (index) in the list.
In summary, dictionaries are ideal for scenarios where you need to quickly look up data by a specific identifier, whereas lists are great when the order of items is important and you're mainly iterating through the collection.
"""