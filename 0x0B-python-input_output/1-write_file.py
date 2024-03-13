#!/usr/bin/python3
'''A module of function that writes to a file'''


def write_file(filename="", text=""):
    '''function that writes to a text file
    Arguments:
    filename: the filr name
    text: the text will be written
    Return: No. of characters written'''

    with open(filename, 'w') as f:
        return f.write(text)
