from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, length):
    	self.length = length
    def area(self):
    	return self.length**2


class AreaCalculator:
    def total_area(self, shapes):
        total = 0
        for shape in shapes:
            total += shape.area()
        return total


# Usage
rectangle = Rectangle(4, 5)
circle = Circle(3)
square = Square(4)

calculator = AreaCalculator()
total_area = calculator.total_area([rectangle, circle, square])

print(f"Total area: {total_area}")

