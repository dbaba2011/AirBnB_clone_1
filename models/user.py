#!/usr/bin/python3
"""User class that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """_summary_
    Contains basic info about the user
    Args:
        BaseModel (_type_): Main Class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
