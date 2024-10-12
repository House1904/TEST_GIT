import math as m

class Circle:
    """Lớp đối tượng Hình tròn"""
    def __init__(self, radius):
        self._radius = radius  # Sử dụng _radius để bảo vệ thuộc tính

    # Định nghĩa property cho radius
    @property
    def radius(self):
        return self._radius

    # Định nghĩa setter cho radius
    @radius.setter
    def radius(self, value):
        if (value <= 0):
            raise ValueError("Bán kính phải là số dương")
        self._radius = value

    def print_info(self):
        print(f"Hình tròn có bán kính là {self.radius}")
        print(f"Diện tích hình tròn là: {self.calculate_area()}")
        print(f"Chu vi hình tròn là: {self.calculate_perimeter()}")

    def calculate_area(self):
        return round(m.pi * self.radius ** 2, 2)

    def calculate_perimeter(self):
        return round(m.pi * self.radius * 2, 2)

# Tạo đối tượng hình tròn với bán kính 5
c = Circle(5)

# In thông tin hình tròn
c.print_info()

# Thay đổi bán kính thông qua setter
c.radius = 10

# In thông tin hình tròn sau khi thay đổi bán kính
c.print_info()

# Thử thiết lập giá trị bán kính không hợp lệ
try:
    c.radius = -3                                                                
except ValueError as e:
    print(e)
