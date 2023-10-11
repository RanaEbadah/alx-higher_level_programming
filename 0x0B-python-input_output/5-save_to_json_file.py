#!/usr/bin/python3
'''A module of function returns an object represented by a JSON string'''


import json


def save_to_json_file(my_obj, filename):
    '''A function returns an object represented by a JSON string'''
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
