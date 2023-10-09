#!/usr/bin/python3
'''Module for lookup function.'''


def lookup(obj):
    '''Looks up object attributes and methods.
    Args:
        obj: the object we have to look up it.
    Returns:
        list: the list of attributes and methods.'''

    return dir(obj)
