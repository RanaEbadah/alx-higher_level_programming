#!/usr/bin/python3
'''Module for class Rectangle '''


from models.base import Base


class Rectangle(Base):
    '''class Rectangle sub class of Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(id)
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
        self.__width = value

    @height.setter
    def height(self, value):
        '''height setter'''
        self.__height = value

    @x.setter
    def x(self, value):
        '''x setter'''
        self.__x = value

    @y.setter
    def y(self, value):
        '''y setter'''
        self.__y = value
