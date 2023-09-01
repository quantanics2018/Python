# Creating sets
fruits = {"apple", "banana", "orange"}
numbers = set([1, 2, 3, 3, 4, 4, 5])  # Creating a set from a list

# Adding and removing elements
fruits.add("grape")
fruits.remove("banana")
fruits.discard("watermelon")

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2  # Union using the | operator or .union() method
intersection_set = set1 & set2  # Intersection using the & operator or .intersection() method
difference_set = set1 - set2  # Difference using the - operator or .difference() method

# Checking membership
if "apple" in fruits:
    print("Apple is in the set")

# Iterating through sets
print("Fruits:")
for fruit in fruits:
    print(fruit)

# Set comprehensions
squared_numbers = {x**2 for x in range(1, 6)}

# Frozen sets
frozen = frozenset([1, 2, 3])

# Displaying results
print("Numbers:", numbers)  # Output: Numbers: {1, 2, 3, 4, 5}
print("Union Set:", union_set)  # Output: Union Set: {1, 2, 3, 4, 5}
print("Intersection Set:", intersection_set)  # Output: Intersection Set: {3}
print("Difference Set:", difference_set)  # Output: Difference Set: {1, 2}
print("Squared Numbers:", squared_numbers)  # Output: Squared Numbers: {1, 4, 9, 16, 25}
print("Frozen Set:", frozen)  # Output: Frozen Set: frozenset({1, 2, 3})

