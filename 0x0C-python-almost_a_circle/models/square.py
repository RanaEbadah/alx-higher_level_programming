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

    def update(self, *args, **kwargs):
        '''assigns an argument for each attribute'''
        if len(args) > 0:
            if type(args[0] is int):
                self.id = args[0]
            if len(args) > 1:
                if type(args[1] is int):
                    self.size = args[1]
            if len(args) > 2:
                if type(args[2] is int):
                    self.x = args[2]
            if len(args) > 3:
                if type(args[3] is int):
                    self.y = args[3]
        else:
            if "id" in kwargs.keys():
                self.id = kwargs["id"]
            if "size" in kwargs.keys():
                self.size = kwargs["size"]
            if "x" in kwargs.keys():
                self.x = kwargs["x"]
            if "y" in kwargs.keys():
                self.y = kwargs["y"]

    def to_dictionary(self):
        '''returns the dictionary representation of a square'''
        return {"id": self.id, "x": self.x, "size": self.size,
                "y": self.y}
