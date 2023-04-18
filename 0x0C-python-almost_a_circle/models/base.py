#!/usr/bin/python3
"""
Define a Bass class
0x0C. Python - Almost a circle, task 1, 15-20
"""
import json
import csv
import turtle


class Base:
    """
    Represent the base model.
    Represents the "base" for all other classes in project 0x0C*.
    Args:
        id (int): identifying number for each instance of cls, may be assigned
            to multiple instances
    Attributes:
        __nb_objects (int): number of `Base` instances not assigned id at
            initialization
    Project tasks:
        1. Base class - /models, __init__.py, class Base, __init__
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializing a new Base.
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries (list) of (dict): list to be converted
        Returns:
            JSON format string of `list_dictionaries`, or '[]' if None or
                empty
        Project tasks:
            15. Dictionary to JSON string - static method `to_json_string()`
                 that returns the JSON string representation of
                 list_dictionaries, or [] if None
        """
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list) of (dict): list of `Base` derived objects (in
                this project `Rectangle` and `Square`)
        Project tasks:
            16. JSON string to file - class method `save_to_file()` that writes
                the JSON string representation of `list_objs` to a file, using
                `to_json_string()`, overwriting existing file, class name in
                file name, if list None then list = []
        """
        if list_objs is None:
            list_objs = []

        list_dicts = []
        for item in list_objs:
            list_dicts.append(item.to_dictionary())
        json_dict = cls.to_json_string(list_dicts)

        fname = cls.__name__ + '.json'
        with open(fname, 'w', encoding='utf-8') as file:
            file.write(json_dict)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the deserialization of a JSON string.
        Args:
            json_string (str): JSON format string to be converted
        Returns:
            List of objects represented by JSON format string, or [] if
                `json_string` is None or empty
        Project tasks:
            17. JSON string to dictionary - static method `from_json_string()`
                that returns the list of the JSON string representation
                `json_string`, a string representing a list of dictionaries,
                or if None or empty, return an empty list
        """
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new dummy instance of class and `update()`s it using
        `dictionary` as keyword args
        Return:
          a class instantiated from a dictionary of attributes.
        Args:
            dictionary (dict): dictionary to be used as keyword args
        Project tasks:
            18. Dictionary to Instance - class method `create()` that creates
                a new dummy instance and `update()`s it with values in
                `dictionary` as keyword args
        """
        if cls.__name__ is 'Rectangle':
            new = cls(1, 1)
        elif cls.__name__ is 'Square':
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        Return a list of classes instantiated from a file of JSON strings
        Returns:
            list of instances of `cls` from file <class name>.json, or empty
                list if no file
        Project tasks:
            19. File to instances - class method `load_from_file()` returns
                list of instances from file <Class name>.json, or empty list
                if no file. must use `from_json_string()` and `create()`,
                class of instances in list depends on cls
        """
        import os.path

        fname = cls.__name__ + '.json'
        if os.path.exists(fname):
            with open(fname, 'r', encoding='utf-8') as new_file:
                json_str = new_file.read()
        else:
            return []
        obj_list = cls.from_json_string(json_str)
        instance_list = []
        for item in obj_list:
            instance_list.append(cls.create(**item))
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        class that serializes and deserializes in CSV.

        Args:
            list_objs (list) of (dict): list of `Base` derived objects (in
                this project `Rectangle` and `Square`)
        Project tasks:
            20. JSON ok, but CSV? - class method `save_from_file_csv()`
                returns list of instances from file <Class name>.csv, or empty
                list if no file. must use `from_json_string()` and `create()`,
                class of instances in list depends on cls
        """
        if list_objs is None:
            list_objs = []

        if cls.__name__ == 'Rectangle':
            keys = ('id', 'width', 'height', 'x', 'y')
        elif cls.__name__ == 'Square':
            keys = ('id', 'size', 'x', 'y')

        list_dicts = []
        for item in list_objs:
            list_dicts.append(item.to_dictionary())

        fname = cls.__name__ + '.csv'
        with open(fname, 'w', encoding='utf-8') as new_file:
            csv_writer = csv.DictWriter(new_file, keys)
            csv_writer.writeheader()
            for dict in list_dicts:
                csv_writer.writerow(dict)

    @classmethod
    def load_from_file_csv(cls):
        """
        A class method that serializes and deserializes in CSV
        Returns:
            list of instances of `cls` from file <class name>.csv, or empty
                list if no file
        Project tasks:
            20. JSON ok, but CSV? - class method `load_from_file_csv()`
                returns list of instances from file <Class name>.csv, or empty
                list if no file. must use `from_json_string()` and `create()`,
                class of instances in list depends on cls
        """
        import os.path

        if cls.__name__ == 'Rectangle':
            keys = ('id', 'width', 'height', 'x', 'y')
        elif cls.__name__ == 'Square':
            keys = ('id', 'size', 'x', 'y')

        fname = cls.__name__ + '.csv'
        if os.path.exists(fname):
            with open(fname, 'r', encoding='utf-8') as new_file:
                csv_reader = csv.DictReader(new_file)
                instance_list = []
                for row in csv_reader:
                    for key in keys:
                        row[key] = int(row[key])
                    instance_list.append(cls.create(**row))
                return instance_list
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        method that opens a window and draws all the Rectangles and Squares
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        trt = turtle.Turtle()
        trt.screen.bgcolor("#ebd9b0")
        trt.pensize(5)
        trt.shape("turtle")

        trt.color("#24382e")
        for rect in list_rectangles:
            trt.showturtle()
            trt.up()
            trt.goto(rect.x, rect.y)
            trt.down()
            for i in range(2):
                trt.forward(rect.width)
                trt.left(90)
                trt.forward(rect.height)
                trt.left(90)
            trt.hideturtle()

        trt.color("#8ede99")
        for sq in list_squares:
            trt.showturtle()
            trt.up()
            trt.goto(sq.x, sq.y)
            trt.down()
            for i in range(2):
                trt.forward(sq.width)
                trt.left(90)
                trt.forward(sq.height)
                trt.left(90)
            trt.hideturtle()

        turtle.exitonclick()
