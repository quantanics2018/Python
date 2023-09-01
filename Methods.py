class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        print(f"{self.name} is barking!")

# Creating an instance of the class
dog1 = Dog("Buddy", 3)

# Calling an instance method
dog1.bark()  # Output: Buddy is barking!
