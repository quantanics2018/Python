# Base class
class Shape:
    def area(self):
        pass  # Placeholder for the method

# Subclasses inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Creating instances of subclasses
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Using polymorphism to calculate areas
shapes = [circle, rectangle]

for shape in shapes:
    print("Area:", shape.area())
