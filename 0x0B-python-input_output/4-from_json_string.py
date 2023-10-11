#!/usr/bin/python3
'''A module of function returns an object represented by a JSON string'''


import json


def from_json_string(my_str):
    '''A function returns an object represented by a JSON string'''
    return json.loads(my_str)
