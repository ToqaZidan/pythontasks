#!/usr/bin/python3
"""
Define a square class
0x0C. Python - Almost a circle, task 10 - 14
"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """
    Creates square objects.
    Args:
        size (int): x and y dimensions of square
        x (int): horizontal offset of square
        y (int): vertical offset of square
        id (int): unique identifer for each instance of super().super()
    Project task:
        10. And now, the Square! - class Square `__init__`, `__str__`,
            inherited, no new attributes
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        class method returns a string with numeric representation of square
        Returns:
            '[Square] (<id>) <x>/<y> - <size>'
        Project task:
            10. And now, the Square! - class Square `__init__`, `__str__`,
                inherited, no new attributes
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """
        get/set the size of square
        Returns:
            __size (int): x and y dimensions of square
        Project task:
            11. Square size - public getter and setter `size`, using
                validation from super().width
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Args:
            value (int): x and y dimensions of square
        Project task:
            11. Square size - public getter and setter `size`, using
                validation from super().width
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates superclass attributes in a given order based on variable
        amount of non-keyword args, or in any order with keyword args.
        `*args` takes precedence over `**kwargs`: if any non-keyword args are
        present, keyword args are ignored.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id
                - 2nd argument represents size
                - 3rd argument represents x
                - 4th argument represents y
            **kwargs (dict): New key/value pairs of attributes.
        Project tasks:
            12. Square update - updates `id`, `size`, `x`, or `y` based on
                *args, or uses **kwargs to access key-worded argments in
                any order. if *args are not empty, **kwargs are skipped
        """
        if args and len(args) != 0:
            r1 = 0
            for arg in args:
                if r1 == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif r1 == 1:
                    self.width = arg
                elif r1 == 2:
                    self.height = arg
                elif r1 == 3:
                    self.x = arg
                elif r1 == 4:
                    self.y = arg
                r1 += 1

        elif kwargs and len(kwargs) != 0:
            for a, v in kwargs.items():
                if a == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif a == "width":
                    self.width = v
                elif a == "height":
                    self.height = v
                elif a == "x":
                    self.x = v
                elif a == "y":
                    self.y = v

    def to_dictionary(self):
        """
        Dictionary representation of a square

        Returns:
            sqr_dict (dict): dictionary of private attribute values
        Project tasks:
            14. Square instance to dictionary representation
        """
        sqr_dict = dict()
        sqr_dict['id'] = self.id
        sqr_dict['size'] = self.size
        sqr_dict['x'] = self.x
        sqr_dict['y'] = self.y
        return sqr_dict
