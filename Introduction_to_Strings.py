# Define a string
my_string = "Hello, World!"

# Print the string
print("Original String:", my_string)

# Length of the string
string_length = len(my_string)
print("Length of String:", string_length)

# Accessing individual characters using indexing
first_char = my_string[0]
second_char = my_string[1]
print("First Character:", first_char)
print("Second Character:", second_char)

# Slicing to extract a substring
substring = my_string[7:12]
print("Substring:", substring)

# Concatenation
new_string = my_string + " Welcome to programming."
print("Concatenated String:", new_string)

# String methods
uppercase_string = my_string.upper()
lowercase_string = my_string.lower()
print("Uppercase:", uppercase_string)
print("Lowercase:", lowercase_string)

# Search for a substring
search_result = "Hello" in my_string
print("Contains 'Hello':", search_result)

# Replace a substring
replaced_string = my_string.replace("World", "Python")
print("Replaced String:", replaced_string)
