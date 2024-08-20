#!/usr/bin/python3
"""
class base
"""
import json
import csv


class Base:
    """ base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                dictionaries = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries represented by json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy Square instance
        else:
            return None

        dummy.update(**dictionary)  # Apply real values using update method
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from a file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                content = file.read()
                dictionaries = cls.from_json_string(content)
                instances = [
                        cls.create(**dictionary) for dictionary in dictionaries
                        ]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list_objs into a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline='') as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id, obj.width,
                                        obj.height, obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize a CSV file into a list of instances."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r") as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(
                            int(row[1]), int(row[2]), int(row[3]),
                            int(row[4]), int(row[0])
                        )
                    elif cls.__name__ == "Square":
                        instance = cls(
                            int(row[1]), int(row[2]), int(row[3]), int(row[0])
                        )
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
