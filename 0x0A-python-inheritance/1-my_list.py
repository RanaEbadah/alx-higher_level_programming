#!/usr/bin/python3
'''Module for myList class'''


class MyList(list):
    '''myList class'''
    def print_sorted(self):
        '''finction for myList ascending order'''
        sorted_list = sorted(self)
        print(sorted_list)
