
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        if radius > 0:
            self.radius = radius
        else:
            print("Invalid radius")

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        if width > 0 and height > 0:
            self.width = width
            self.height = height
        else:
            print("Invalid width or height")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a, b, c):
        if a > 0 and b > 0 and c > 0 and a+b > c and a+c > b and b+c > a:
            self.a = a
            self.b = b
            self.c = c
        else:
            print("Invalid side length")

    def area(self):
        #heron
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


def main():

    for form in [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]:
        print(form.__class__.__name__, "Area: ", form.area())
        print(form.__class__.__name__, "Perimeter: ", form.perimeter())


if __name__ == "__main__":
    main()