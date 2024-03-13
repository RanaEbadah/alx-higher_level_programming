#!/usr/bin/python3
'''A module of function that appends a string at the end of a file'''


def append_write(filename="", text=""):
    '''function that append to a text file
    Arguments:
    filename: the filr name
    text: the text will be written
    Return: No. of characters written'''

    with open(filename, 'a') as f:
        return f.write(text)
