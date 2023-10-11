#!/usr/bin/python3
'''A module of function returns an object represented by a JSON string'''


import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file


args = sys.argv[1:]

oldArgs = load_from_json_file("add_item.json")
oldArgs.extend(args)
save_to_json_file(oldArgs, "add_item.json")
