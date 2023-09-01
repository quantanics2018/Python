# Creating a list
fruits = ["apple", "banana", "orange", "grape"]

# Accessing items in a list using indexing
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: orange

# Modifying items in a list using indexing
fruits[1] = "kiwi"
print(fruits)  # Output: ['apple', 'kiwi', 'orange', 'grape']

# Adding an item to the end of the list using the `append` method
fruits.append("pear")
print(fruits)  # Output: ['apple', 'kiwi', 'orange', 'grape', 'pear']

# Inserting an item at a specific index using the `insert` method
fruits.insert(2, "pineapple")
print(fruits)  # Output: ['apple', 'kiwi', 'pineapple', 'orange', 'grape', 'pear']

# Removing an item from the list using the `remove` method
fruits.remove("kiwi")
print(fruits)  # Output: ['apple', 'pineapple', 'orange', 'grape', 'pear']

# Removing an item by index using the `pop` method
popped_fruit = fruits.pop(1)
print("Popped fruit:", popped_fruit)  # Output: Popped fruit: pineapple
print(fruits)  # Output: ['apple', 'orange', 'grape', 'pear']

# Finding the index of an item using the `index` method
index_orange = fruits.index("orange")
print("Index of 'orange':", index_orange)  # Output: Index of 'orange': 1

# Checking if an item is in the list using the `in` keyword
print("banana" in fruits)  # Output: False

# Getting the length of the list using the `len` function
print("Number of fruits:", len(fruits))  # Output: Number of fruits: 4

# Iterating through a list using a for loop
for fruit in fruits:
    print(fruit)
# Output:
# apple
# orange
# grape
# pear
