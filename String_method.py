# String immutability
string_immutable = "Python is great!"
# This will result in an error:
# string_immutable[0] = 'J'

# String transformation methods
text = "Hello, World!"
lower_text = text.lower()
upper_text = text.upper()
capitalized_text = text.capitalize()
title_text = text.title()
print("Original:", text)
print("Lowercase:", lower_text)
print("Uppercase:", upper_text)
print("Capitalized:", capitalized_text)
print("Title:", title_text)

# String manipulation methods
whitespace_text = "   whitespace   "
stripped_text = whitespace_text.strip()
print("Stripped:", stripped_text)

comma_sep_text = "apple,banana,orange"
split_fruits = comma_sep_text.split(",")
print("Split:", split_fruits)

fruits = ["apple", "banana", "cherry"]
joined_text = ", ".join(fruits)
print("Joined:", joined_text)

replaced_text = text.replace("Hello", "Hi")
print("Replaced:", replaced_text)

index1 = text.find("World")
index2 = text.index("World")
print("Index (find):", index1)
print("Index (index):", index2)

count_a = text.count("o")
print("Count of 'o':", count_a)

# String testing methods
startsWithHello = text.startswith("Hello")
endsWithWorld = text.endswith("World")
print("Starts with 'Hello':", startsWithHello)
print("Ends with 'World':", endsWithWorld)

isAlphaNumeric = text.isalnum()
isDigit = text.isdigit()
isAlpha = text.isalpha()
isSpace = text.isspace()
isLower = text.islower()
isUpper = text.isupper()
print("isalnum:", isAlphaNumeric)
print("isdigit:", isDigit)
print("isalpha:", isAlpha)
print("isspace:", isSpace)
print("islower:", isLower)
print("isupper:", isUpper)

# Other string methods
string_length = len(text)
formatted_text = "My name is {}. I am {} years old.".format("Alice", 30)
split_lines_text = "Line 1\nLine 2\nLine 3".splitlines()
encoded_text = text.encode("utf-8")

print("String length:", string_length)
print("Formatted text:", formatted_text)
print("Split lines:", split_lines_text)
print("Encoded text:", encoded_text)
