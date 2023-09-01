def repeat(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * num
        return wrapper
    return decorator

@repeat(3)
def say_hi(name):
    return f"Hi, {name}"

print(say_hi("Alice"))  # Output: Hi, AliceHi, AliceHi, Alice
