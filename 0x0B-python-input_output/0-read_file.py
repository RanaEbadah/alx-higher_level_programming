#!/usr/bin/python3
'''A module of function that reads a file and prints it'''


def read_file(filename=""):
    '''function that read a text file and print it
    Arguments:
    filename: the filr name'''

    with open(filename, 'r') as f:
        print(f.read(), end="")
