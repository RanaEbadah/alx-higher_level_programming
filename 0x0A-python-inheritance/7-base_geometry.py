#!/usr/bin/python3
'''Module for BaseGeometry class.'''


class BaseGeometry:
    '''BaseGeometry class'''

    def area(self):
        '''Method to computer area'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Methos that validates value'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if int(value) <= 0:
            raise ValueError("{} must be greater than 0".format(name))
