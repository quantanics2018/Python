class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating an object of the class
dog1 = Dog("Buddy", 3)

# Accessing attributes and calling methods
print(f"{dog1.name} is {dog1.age} years old.")  # Output: Buddy is 3 years old.
dog1.bark()  # Output: Buddy says Woof!
