class Person:
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

# Creating instances of the class
person1 = Person("Person1", 25)
person2 = Person("Person2", 30)

# Accessing instance attributes
print(person1.name, person1.age)  # Output: Person1 25
print(person2.name, person2.age)  # Output: Person2 30
