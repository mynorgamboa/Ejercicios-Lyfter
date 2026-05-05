from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    pi = 3.1416
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        self.perimeter = (2 * self.pi) * self.radius
        return self.perimeter

    def calculate_area(self):
        self.area = self.pi * (self.radius**2)
        return self.area


class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_perimeter(self):
        self.perimeter = 4 * self.side
        return self.perimeter

    def calculate_area(self):
        self.area = self.side**2
        return self.area


class Rectangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_perimeter(self):
        self.perimeter = 2*self.base + 2*self.height
        return self.perimeter

    def calculate_area(self):
        self.area = self.base * self.height
        return self.area
    

new_circle = Circle(10)

print(f'Circle perimeter: {new_circle.calculate_perimeter()}')
print(f'Circle area: {new_circle.calculate_area()}')

new_square = Square(29)

print(f'Square perimeter: {new_square.calculate_perimeter()}')
print(f'Square area: {new_square.calculate_area()}')

new_rectangle = Rectangle(7,3)

print(f'Rectangle perimeter: {new_rectangle.calculate_perimeter()}')
print(f'Rectangle area: {new_rectangle.calculate_area()}')
