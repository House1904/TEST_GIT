import math as m

class Triangle:
    """Đây là lớp Tam giác"""
    def __init__(self, side1, side2, side3, color):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.color = color

    def calculate_perimeter(self):
        return round((self.side1 + self.side2 + self.side3),2)

    def calculate_area(self):
        s = self.calculate_perimeter() / 2  # Nửa chu vi
        area = m.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return round(area, 2)

    def print_info(self):
        print(f"Tam giác có các cạnh là: {self.side1}, {self.side2}, {self.side3}")
        print(f"Màu sắc của tam giác: {self.color}")
        print(f"Chu vi tam giác: {self.calculate_perimeter()}")
        print(f"Diện tích tam giác: {self.calculate_area()}")

    def triangle_type(self):
        if (self.side1 == self.side2 == self.side3):
            return "Tam giác đều"
        elif (self.side1 == self.side2 or self.side2 == self.side3 or self.side1 == self.side3):
            if (self.is_right_triangle()):
                return "Tam giác vuông cân"
            else:
                return "Tam giác cân"
        elif (self.is_right_triangle()):
            return "Tam giác vuông"
        else:
            return "Tam giác thường"

    # Phương thức kiểm tra tam giác vuông
    def is_right_triangle(self):
        sides = sorted([self.side1, self.side2, self.side3])
        return m.isclose(sides[2] ** 2, sides[0] ** 2 + sides[1] ** 2)
        # kiểm tra xem có gần bằng nhau hay không

# Ví dụ sử dụng lớp Triangle
triangle = Triangle(3, 4, 5, "đỏ")

# Hiển thị thông tin về tam giác
triangle.print_info()

# Xác định loại tam giác
print(f"Loại tam giác: {triangle.triangle_type()}")