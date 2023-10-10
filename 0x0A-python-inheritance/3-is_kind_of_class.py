#!/usr/bin/python3
'''Module for is_kind_of_class method.'''


def is_kind_of_class(obj, a_class):
    '''Determines if an object is an object or subclass of a class.'''
    return isinstance(obj, a_class)
