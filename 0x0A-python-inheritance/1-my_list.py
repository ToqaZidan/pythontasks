#!/usr/bin/python3
""" Define a class MyList that inherits from list"""


class MyList(list):
    """A subclass of `list` that adds a `print_sorted` method to print the list sorted in ascending order.
    
    Inherits from:
        list: The built-in list class
    
    Example:
        x = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        x.print_sorted()  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    """
    
    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
