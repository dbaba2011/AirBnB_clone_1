#!/usr/bin/python3 
""" This is the file storage class """

import json


class FileStorage:
    """  serializes instances to a JSON file and deserializes JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns a dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w") as fp:
            json.dump(FileStorage.__objects, fp)

    def reload(self):
        """ deserializes the json file to __objects(only if the json file(_file_path) exits, otherwise do nothin, if the file doesn't exist, no exception should be raised"""
        try:
            with open(FileStorage.__file_path, "r") as fp:
                FileStorage.__objects = json.load(fp)
        except Exception:
            pass

