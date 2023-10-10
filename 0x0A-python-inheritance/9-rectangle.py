#!/usr/bin/python3
'''Modyule for Rectangle class'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''subclass rectangle'''
    def __init__(self, width, height):
        '''the constructor'''
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height

    def area(self):
        '''Method to computing area'''
        return self.__height * self.__width

    def __str__(self):
        '''Method for str and print'''
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
