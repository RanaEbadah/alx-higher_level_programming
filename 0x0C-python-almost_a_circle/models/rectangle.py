#!/usr/bin/python3
'''Module for class Rectangle '''


from models.base import Base


class Rectangle(Base):
    '''class Rectangle sub class of Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__y = y
        self.__x = x

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @width.setter
    def width(self, value):
        '''width setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        '''height setter'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        '''x setter'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        '''y setter'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''area function to calculate the rectabgle area'''
        return self.__width * self.__height

    def display(self):
        '''prints in stdout the Rectangle instance with the character #'''
        for yy in range(0, self.__y):
            print()
        for h in range(0, self.__height):
            for xx in range(0, self.__x):
                print(" ", end="")
            for w in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        '''override of __str__()'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        '''assigns an argument for each attribute'''
        if len(args) > 0:
            if type(args[0] is int):
                self.id = args[0]
            if len(args) > 1:
                if type(args[1] is int):
                    self.__width = args[1]
            if len(args) > 2:
                if type(args[2] is int):
                    self.__height = args[2]
            if len(args) > 3:
                if type(args[3] is int):
                    self.__x = args[3]
            if len(args) > 4:
                if type(args[4] is int):
                    self.__y = args[4]
        else:
            if "id" in kwargs.keys():
                self.id = kwargs["id"]
            if "width" in kwargs.keys():
                self.__width = kwargs["width"]
            if "height" in kwargs.keys():
                self.__height = kwargs["height"]
            if "x" in kwargs.keys():
                self.__x = kwargs["x"]
            if "y" in kwargs.keys():
                self.__y = kwargs["y"]

    def to_dictionary(self):
        '''returns the dictionary representation of a Rectangle'''
        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}
    
    def to_json(self):
        '''return dictionary repr'''
        return self.to_dictionary()
