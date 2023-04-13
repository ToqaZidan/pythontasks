#!/usr/bin/python3
"""
Define a function that adds all arguments to a Python list
and saves them to a JSON file.
"""


import sys
from typing import List
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_item(argv: List[str]) -> None:
    """
    Adds all arguments to a list and saves it to a JSON file.

    Args:
    argv: arguments to a list

    Return:
    JSON file contain a list
    """
    try:
        items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        items = []
    items.extend(argv[1:])
    save_to_json_file(items, 'add_item.json')


if __name__ == '__main__':
    add_item(sys.argv)
    items = load_from_json_file('add_item.json')
    print(items)
