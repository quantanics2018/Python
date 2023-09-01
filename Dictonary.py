# Creating a dictionary
student = {
    "name": "Adhiban",
    "age": 18,
    "major": "Computer Science",
    "is_enrolled": True
}

# Accessing values using keys
print("Name:", student["name"])         # Output: Name: Adhiban
print("Age:", student["age"])           # Output: Age: 18
print("Major:", student["major"])       # Output: Major: Computer Science
print("Is Enrolled:", student["is_enrolled"])  # Output: Is Enrolled: True

# Modifying values using keys
student["age"] = 21
print("Updated Age:", student["age"])  # Output: Updated Age: 21

# Adding a new key-value pair
student["gender"] = "Male"
print("Gender:", student["gender"])    # Output: Gender: Male

# Removing a key-value pair using the `del` keyword
del student["is_enrolled"]
# The following line would raise a KeyError because the key "is_enrolled" no longer exists
# print("Is Enrolled:", student["is_enrolled"])

# Checking if a key exists in the dictionary
if "name" in student:
    print("Name exists in the dictionary")

# Getting a list of all keys using the `keys` method
keys_list = student.keys()
print("Keys:", keys_list)  # Output: Keys: dict_keys(['name', 'age', 'major', 'gender'])

# Getting a list of all values using the `values` method
values_list = student.values()
print("Values:", values_list)  # Output: Values: dict_values(['John Doe', 21, 'Computer Science', 'Male'])

# Iterating through keys and values using a loop
for key, value in student.items():
    print(key, ":", value)
# Output:
# name : Adhiban
# age : 21
# major : Computer Science
# gender : Male
