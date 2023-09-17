#!/usr/bin/python3
"""base module"""
import json
import csv
import turtle


class Base:
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def type_validator(self, name, value):
        """validate if type  of value is int"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

    def value_validator(self, name, value):
        """validate the value of argument"""
        if name == "height" or name == "width":
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
        else:
            if value < 0:
                raise ValueError(f"{name} must be >= 0")

    @staticmethod
    def to_json_string(list_dictionaries):
        """dictionary to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        list_dict = []
        if list_objs is None or len(list_objs) == 0:
            list_dict = []
        else:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        with open(f"{cls.__name__}.json", "w") as f:
            list_of_json = cls.to_json_string(list_dict)
            f.write(list_of_json)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle" or cls.__name__ == "Square":
            temp = cls(5, 5)
            temp.update(**dictionary)
            return temp

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(f"{cls.__name__}.json") as f:
                obj_list = cls.from_json_string(f.read())
                instances_list = []
                for obj in obj_list:
                    instances_list.append(cls.create(**obj))
                return instances_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        list_dict = []
        if list_objs is None or len(list_objs) == 0:
            list_dict = []
        else:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        with open(f"{cls.__name__}.csv", "w") as csv_file:
            if list_objs is None or len(list_objs) == 0:
                return csv_file.write("[]")
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for obj in list_dict:
                writer.writerow(obj)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        try:
            instances_list = []
            with open(f"{cls.__name__}.csv") as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    for key, value in row.items():
                        row[key] = int(value)
                    instances_list.append(cls.create(**row))
                return instances_list
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        tk = turtle.Turtle()
        tk.speed(1)
        turtle.bgcolor("black")
        tk.color("gray")
        tk.pensize(4)
        colors = ["cyan", "purple", "red", "blue", "orange"]
        for i, rectangle in enumerate(list_rectangles):
            tk.up()
            tk.goto(rectangle.x, rectangle.y)
            tk.down()
            tk.begin_fill()
            for _ in range(2):
                tk.fd(rectangle.width)
                tk.left(90)
                tk.fd(rectangle.height)
                tk.left(90)
            tk.fillcolor(colors[i % 5])
            tk.end_fill()

        for square in list_squares:
            i += 1
            tk.up()
            tk.goto(square.x, square.y)
            tk.down()
            tk.begin_fill()
            for _ in range(4):
                tk.forward(square.size)
                tk.left(90)

            tk.fillcolor(colors[i % 5])
            tk.end_fill()

        tk.hideturtle()
        turtle.done()
