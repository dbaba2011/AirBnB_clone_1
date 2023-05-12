#!/usr/bin/python3
"""User class that inherits from BaseModel"""

from base_model import BaseModels


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
