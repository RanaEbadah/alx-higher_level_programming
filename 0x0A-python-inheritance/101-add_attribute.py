#!/usr/bin/python3
'''Module for unction that adds a new attribute to an object'''


def add_attribute(obj, attrName, attrValue):
    '''function that adds a new attribute to an object'''
    if '__dict__' in dir(obj):
        obj.__dict__[attrName] = attrValue
    else:
        raise TypeError("Can't add new attribute")
