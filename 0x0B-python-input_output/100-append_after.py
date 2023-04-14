#!/usr/bin/python3
"""
Define a function that nserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing
    a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line of the file.
        new_string (str): The string to insert after
        each line containing the `search_string`.

    Returns:
        None

    Raises:
        None
    """
    with open(filename, 'r') as new_file:
        lines = new_file.readlines()

    with open(filename, 'w') as new_file:
        for line in lines:
            new_file.write(line)
            if search_string in line:
                new_file.write(new_string + '\n')

    with open(filename, 'a') as new_file:
        new_file.write('\n')
