#!/usr/bin/python3
'''Module for inherits_from method.'''


def inherits_from(obj, a_class):
    '''Determines  if the object is an instance of  a class that inherited'''
    return isinstance(type(obj), a_class)
