# Chaining comparison operators with logical operators in Python

# Let's assume we have three variables representing different values
x = 5
y = 10
z = 15

# Using 'and' to combine multiple comparisons
if x < y and y < z:
    print("Both conditions are true.")
else:
    print("At least one condition is not met.")

# Using 'or' to combine multiple comparisons
if x > y or y < z:
    print("At least one condition is true.")
else:
    print("No condition is true.")
