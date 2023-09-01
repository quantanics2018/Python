def is_even(number):
    """
    This function checks if a number is even.
    
    Parameters:
    number (int): The number to check.
    
    Returns:
    bool: True if the number is even, False if it's odd.
    """
    if number % 2 == 0:
        return True
    else:
        return False

# Using the function
num = 10
if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
