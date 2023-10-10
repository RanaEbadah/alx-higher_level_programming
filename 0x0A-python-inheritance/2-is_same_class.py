#!/usr/bin/python3
'''Module for isinstance function.'''


def is_same_class(obj, a_class):
    '''isinstance function.
    Args:
        obj: the object we have to look up it.
        a_class: the parent class
    Returns:
        bool: True or False.'''
    return isinstance(obj, a_class)
