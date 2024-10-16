import math as m

class Point:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x_coord(self):
        return self._x

    @x_coord.setter
    def x_coord(self, value):
        self._x = value

    @property
    def y_coord(self):
        return self._y

    @y_coord.setter
    def y_coord(self, value):
        self._y = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def display(self):
        print(f"Coordinates: ( {self._x}, {self._y} ) and Color: {self._color}")

    def translate(self, distance):
        self._x += distance
        print(f"x-coordinate after translating by {distance} is {self._x}")

    def translate_2d(self, distance):
        self._x += distance
        self._y += distance
        print(f"Coordinates after translating by {distance} are ({self._x}, {self._y})")

    def distance_from_O(self):
        return m.sqrt(self._x ** 2 + self._y ** 2)

    def distance_between_points(self, point):
        return m.sqrt((self._x - point.x_coord) ** 2 + (self._y - point.y_coord) ** 2)

# Create two points
p1 = Point(1, 2, "red")
p2 = Point(4, 6, "blue")

p1.display()
p2.display()

p1.translate(6)
p2.translate(-9)

p1.translate_2d(-5)
p2.translate_2d(-7)

print(f"Khoảng cách từ điểm p1 đến O là {round(p1.distance_from_O(),2)}")
print(f"Khoảng cách từ điểm p2 đến O là {round(p2.distance_from_O(),2)}")

# Calculate the distance between p1 and p2
distance = p1.distance_between_points(p2)
print(f"The distance between p1 and p2 is: {round(distance,2)}")
