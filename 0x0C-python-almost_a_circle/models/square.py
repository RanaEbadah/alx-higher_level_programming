#!/usr/bin/python3
'''Module for class square '''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''class Square inherits from Rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''str override'''
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.height)

    @property
    def size(self):
        '''width getter'''
        return self.height

    @size.setter
    def size(self, value):
        '''width setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value
