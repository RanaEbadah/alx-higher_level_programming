#!/usr/bin/python3
'''A module for the Base class'''


import json


class Base:
    '''The Base class for all coming classes'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''constructor'''
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Converts list of dictionaries to JSON string'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes the JSON string representation of list_objs to a file'''

        fileName = type(list_objs).__name__ + ".json"
        file = open(fileName, "w")

        if list_objs is None:
            emptyList = []
            file.write(cls.to_json_string(emptyList))

        else:
            file.write(cls.to_json_string(list_objs))
        
        file.close()
