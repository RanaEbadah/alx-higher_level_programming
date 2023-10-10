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
