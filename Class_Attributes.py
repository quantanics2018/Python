class Car:
    # Class attribute
    wheels = 4

# Accessing class attribute using the class name
print(Car.wheels)  # Output: 4

# Creating instances of the class
car1 = Car()
car2 = Car()

# Accessing class attribute using instances
print(car1.wheels)  # Output: 4
print(car2.wheels)  # Output: 4
