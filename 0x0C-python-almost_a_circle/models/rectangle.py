#!/usr/bin/python3
"""
Class Rectangle that inherits from Base.
0x0C. Python - Almost a circle, task 2 - 13
"""
from models.base import Base


class Rectangle(Base):
    """
    Intializing a rectangle objects.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Creates rectangle objects.

        Args:
            width (int): x dimension of rectangle
            height (int): y dimension of rectangle
            x (int): horizontal offset of rectangle
            y (int): vertical offset of rectangle
            id (int): unique identifer for each instance of super()

        Raises:
            TypeError: If either of width or height is not an intger.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an intger.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        set/get the width of the Rectangle

        Returns:
            __width (int): x dimension of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Args:
            value (int): x dimension of rectangle
        Attributes:
            __width (int): x dimension of rectangle
        """
        if value <= 0:
            raise ValueError("width must be > 0")
        if type(value) != int:
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """
        set/get the height of the Rectangle

        Returns:
            __height (int): y dimension of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Args:
            value (int): y dimension of rectangle
        Attributes:
            __height (int): y dimension of rectangle
        """
        if value <= 0:
            raise ValueError("height must be > 0")
        if type(value) != int:
            raise TypeError("height must be an integer")
        self.__height = value

    @property
    def x(self):
        """
        set/get the X of the Rectangle

        Returns:
            __x (int): horizontal offset of rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Args:
            value (int): horizontal offset of rectangle
        Attributes:
            __x (int): horizontal offset of rectangle
        """
        if value <= 0:
            raise ValueError("x must be > 0")
        if type(value) != int:
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """
        set/get the Y of the Rectangle
        Returns:
            __y (int): vertical offset of rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Args:
            value (int): vertical offset of rectangle
        Attributes:
            __y (int): vertical offset of rectangle
        """
        if value <= 0:
            raise ValueError("x must be > 0")
        if type(value) != int:
            raise TypeError("x must be an integer")
        self.__y = value

    def area(self):
        """
        Calculate area of rectangle as product of `width`* `height`.
        Returns:
            area of rectangle
        Project tasks:
            4. Area first - public method area()
        """
        return self.width * self.height

    def display(self):
        """
        Prints rectangle to stdout using '#' character.

        Attributes:
            display (str): printed # art drawing of rectangle
            __display (str): final value of `display`.
        Project tasks:
            5. Display #0 - public method `display()`, only use `width`
        and `height`
            7. Display #1 - include use of offset vars `x` and `y`
        """
        display = ''
        for row in range(self.y):
            display += '\n'
        for row in range(self.height):
            for column in range(self.x):
                display += ' '
            for column in range(self.width):
                display += '#'
            if row < self.height - 1:
                display += '\n'
        self.__display = display
        print(display)

    def __str__(self):
        """
        class method that Returns string with numeric
        representation of rectangle
        Returns:
            '[Rectangle] (<id>) <x>/<y> - <width>/<height>'
        Project tasks:
            6. __str__ - `__str__` method
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Updates attributes in a given order based on variable amount of
        non-keyword args, or in any order with keyword args.
        `*args` takes precedence over `**kwargs`: if any non-keyword args are
        present, keyword args are ignored.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id
                - 2nd argument represents width
                - 3rd argument represent height
                - 4th argument represents x
                - 5th argument represents y
            **kwargs (dict): New key/value pairs of attributes.
        Project tasks:
            8. Update #0 - updates `id`, `width`, `height`, `x`, or `y` based
                on amount of args using *args
            9. Update #1 - adds use of **kwargs to access key-worded argments
                in any order. if *args not empty, **kwargs skipped
        """
        if args and len(args) != 0:
            r1 = 0
            for arg in args:
                if r1 == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
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
                        self.__init__(self.width, self.height, self.x, self.y)
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
         Dictionary representation of a Rectangle
        Returns:
            rect_dict (dict): dictionary of private attribute values
        Project tasks:
            13. Rectangle instance to dictionary representation
        """
        rect_dict = dict()
        rect_dict['id'] = self.id
        rect_dict['width'] = self.width
        rect_dict['height'] = self.height
        rect_dict['x'] = self.x
        rect_dict['y'] = self.y
        return rect_dict
