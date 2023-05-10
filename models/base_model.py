#!/usr/bin/python3
""" This is the Base Model Class """

import uuid
import datetime


class BaseModel:
    """ Base models class
    Attributes:
    id: string assign with uuid when instance is created
    created_at: current datetime when an instance is created
    updated_at: current datetime when an instance is created
    Methods:
    init: basic method ,constructor
    str: print string representation
    sace: updates the public instance attribute
    to_dict: return a dictionary reprenstation
    """
    def __init__(self):
        """ Constructor method """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ Print the string representation of the class """
        return "[{0}] ({1}) {2}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updated the updated_at attribute """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns the dictionary representation of the instance"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
