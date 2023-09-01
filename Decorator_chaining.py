def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper():
        result = func()
        return result + "!"
    return wrapper

@exclamation_decorator
@uppercase_decorator
def greet():
    return "hello"

print(greet())  # Output: HELLO!
