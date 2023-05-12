#!/usr/bin/python3
""" This is the file storage class """

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class_dict = {
        "BaseModel": BaseModel,
        "User": User
        "State": State
        "City": City
        "Amenity": Amenity
        "Place": Place
        "Review": Review
        }


class FileStorage:
    """  serializes instances to a JSON file and
        deserializes JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns a dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the json path """
        obj_dict = {}
        for key in FileStorage.__objects:
            obj_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """ Deserilizes the json file to __objects """
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                obj = self.class_dict[value["__class__"]](**value)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
