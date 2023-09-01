# Base class
class Animal:
    def speak(self):
        pass  # Placeholder for the method

# Subclasses inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating instances of subclasses
dog = Dog()
cat = Cat()

# Calling the overridden methods
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
