# Example: Using list comprehensions to filter even numbers and calculate their squares

# Original list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension to filter even numbers and calculate their squares
even_square_list = [x ** 2 for x in numbers if x % 2 == 0]

# Explanation:
# 1. We start with a list of numbers from 1 to 10.
# 2. The list comprehension iterates through each number in the 'numbers' list.
# 3. For each number, the condition 'x % 2 == 0' checks if the number is even.
#    If it is, the number is squared using 'x ** 2'.
# 4. The squared value is added to the new list 'even_square_list'.
# 5. After iterating through all numbers, the resulting list contains squares of even numbers.

# Output
print(even_square_list)
