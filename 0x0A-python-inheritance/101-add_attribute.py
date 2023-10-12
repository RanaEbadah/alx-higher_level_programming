#!/usr/bin/python3
'''Module for unction that adds a new attribute to an object'''


def add_attribute(obj, attrName, attrValue):
    '''Add a new attribute to an object if possible.
    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("Can't add new attribute")
    else:
        setattr(obj, attrName, attrValue)
