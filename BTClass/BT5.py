from abc import ABC, abstractmethod
import math as m

# Abstract class Shape
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        """Tính diện tích"""
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        """Tính chu vi"""
        pass

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round(m.pi * self.radius ** 2, 2)

    def calculate_perimeter(self):
        return round(2 * m.pi * self.radius, 2)

# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return round(self.width * self.height, 2)

    def calculate_perimeter(self):
        return round(2 * (self.width + self.height), 2)

# Triangle class
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def calculate_area(self):
        # Sử dụng công thức Heron để tính diện tích
        s = (self.a + self.b + self.c) / 2
        return round(m.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)), 2)

    def calculate_perimeter(self):
        return round(self.a + self.b + self.c, 2)

# Tạo các đối tượng và tính toán
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)

print(f"Hình tròn có bán kính 5: Chu vi = {circle.calculate_perimeter()}, Diện tích = {circle.calculate_area()}")
print(f"Hình chữ nhật có chiều rộng 4 và chiều dài 6: Chu vi = {rectangle.calculate_perimeter()}, Diện tích = {rectangle.calculate_area()}")
print(f"Hình tam giác với các cạnh 3, 4, 5: Chu vi = {triangle.calculate_perimeter()}, Diện tích = {triangle.calculate_area()}")
