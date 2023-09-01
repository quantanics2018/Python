# Creating a tuple
student_info = ("Adhiban", 18, "Computer Science")

# Accessing elements using indexing
print("Name:", student_info[0])          # Output: Name: Adhiban
print("Age:", student_info[1])            # Output: Age: 18
print("Major:", student_info[2])          # Output: Major: Computer Science

# Iterating through a tuple
for item in student_info:
    print(item)
# Output:
# Adhiban
# 18
# Computer Science

# Nested tuples
course1 = ("Math", 4)
course2 = ("History", 3)
courses = (course1, course2)

# Accessing elements in nested tuples
print("Course 1:", courses[0])          # Output: Course 1: ('Math', 4)
print("Course 2:", courses[1])          # Output: Course 2: ('History', 3)
print("Course 1 Name:", courses[0][0])  # Output: Course 1 Name: Math
print("Course 2 Credits:", courses[1][1])  # Output: Course 2 Credits: 3
