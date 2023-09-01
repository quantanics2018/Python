def get_student_info():
    """
    This function simulates getting information about a student.
    
    Returns:
    tuple: A tuple containing the student's name, age, and grade.
    """
    name = "Alice"
    age = 20
    grade = "A"
    return name, age, grade

# Using tuple unpacking with a function
student_name, student_age, student_grade = get_student_info()

# Output the unpacked values
print(f"Student Name: {student_name}")
print(f"Student Age: {student_age}")
print(f"Student Grade: {student_grade}")
