#!/usr/bin/python3
""" This is the Base Model Class """

from uuid import uuid4
from datetime import datetime
import models


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

    def __init__(self, *args, **kwargs):
        """ Initilazes base class instance
        Args:
            *args: list of arguments(not used)
            **kwargs: dictionary of arguments"""
            
        if kwargs:
            dateformat = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                elif key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = datetime.strptime(value, dateformat)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, dateformat)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Print the string representation of the class """
        return "[{0}] ({1}) {2}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updated the updated_at attribute """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns the dictionary representation of the instance"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
