#!/usr/bin/python3
'''A module of function returns JSON of an object (string):'''


import json


def to_json_string(my_obj):
    '''function returns JSON of an object (string):'''

    return json.dumps(my_obj)
