#!/usr/bin/python3
'''A module of function returns an object represented by a JSON string'''


import json


def load_from_json_file(filename):
    '''function returns an object represented by a JSON string'''
    with open(filename, 'r') as f:
        return json.loads(f.read())
