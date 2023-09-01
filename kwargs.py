def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name='Adhiban', age=18)  # Output: name: Adhiban age: 18
print_kwargs(country='India', city='Madurai')  # Output: country: India city: Madurai
