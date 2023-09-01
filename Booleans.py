# Boolean Values
is_student = True
has_passed_exam = False

# Boolean Operators
and_result = is_student and has_passed_exam  # False
or_result = is_student or has_passed_exam   # True
not_result = not is_student                 # False

# Comparison Operators
age = 20
is_adult = age >= 18  # True

# Truthy and Falsy Values
empty_list = []
non_empty_list = [1, 2, 3]
empty_string = ""
non_empty_string = "Hello"
zero = 0
non_zero = 42

# Conditional Statements
if is_adult:
    print("You are an adult.")
else:
    print("You are not an adult.")

if non_empty_list:
    print("The list is not empty.")
else:
    print("The list is empty.")

if not empty_string:
    print("The string is empty.")
else:
    print("The string is not empty.")

if non_zero:
    print("The number is non-zero.")
else:
    print("The number is zero.")
