#!/usr/bin/python3
'''Module for unction that adds a new attribute to an object'''


def add_attribute(obj, attrName, attrValue):
    '''function that adds a new attribute to an object'''
    if hasattr(obj, attrName):
        raise TypeError("Can't add new attribute")
    else:
        setattr(obj, attrName, attrValue)
