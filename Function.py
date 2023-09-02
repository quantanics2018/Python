# Example: Defining and using a function to calculate the area of a rectangle

# Function definition
def calculate_rectangle_area(length, width):
    """
    This function calculates the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    
    Returns:
    float: The calculated area of the rectangle.
    """
    area = length * width
    return area

# Using the function
rectangle_length = 5.0
rectangle_width = 3.0
area_of_rectangle = calculate_rectangle_area(rectangle_length, rectangle_width)

# Output
print(f"The area of the rectangle is: {area_of_rectangle}")
