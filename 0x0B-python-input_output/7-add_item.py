#!/usr/bin/python3
"""
Function That add all arguments to a Python list and save them to a file.
"""

import sys
from typing import List
from os import path
import json


def save_to_json_file(my_obj: List[str], filename: str) -> None:
    """Save an object to a JSON file."""
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename: str) -> List[str]:
    """Load an object from a JSON file."""
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)


if __name__ == "__main__":
    filename = "add_item.json"

    if path.isfile(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
