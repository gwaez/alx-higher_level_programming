# Python - More Classes and Objects

# Author: Ahmed Mahmoud (GitHub: gwaez)
# Cohort: 18

class Rectangle:
    number_of_instances = 0
    class_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return str(self.class_symbol) * self.width + '\n' + \
               (str(self.class_symbol) + ' ' * (self.width - 2) + self.class_symbol + '\n') * (self.height - 2) + \
               str(self.class_symbol) * self.width

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)


# Example usage:
# rect1 = Rectangle(5, 10)
# rect2 = Rectangle(8, 8)
# bigger_rect = Rectangle.bigger_or_equal(rect1, rect2)
# print(bigger_rect)
# print(Rectangle.number_of_instances)
# del rect1
# print(Rectangle.number_of_instances)

