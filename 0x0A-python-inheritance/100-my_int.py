#!/usr/bin/python3
'''Module for class MyInt that inherits from int'''


class MyInt(int):
    '''class MyInt'''
    def __eq__(self, other):
        '''== function'''
        return super().__ne__(other)

    def __ne__(self, other):
        '''!= function'''
        return super().__eq__(other)
