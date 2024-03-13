#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        elif height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height
        self.__class__.number_of_instances += 1

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
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):

        if self.__width == 0 or self.__height == 0:
            return ""

        resultString = ""
        for x in range(0, self.__height):
            for y in range(0, self.__width):
                resultString += "#"

            if x != self.height - 1:
                resultString += "\n"

        return resultString

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1
