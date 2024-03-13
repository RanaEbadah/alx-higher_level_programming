#!/usr/bin/python3
'''Module for square class'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square'''
    def __init__(self, size):
        '''Constructor'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Method to calculate area'''
        return self.__size * self.__size

    def __str__(self):
        '''Method to print() and str()'''
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
