#!/usr/bin/python3
"""Reiview class is here """

from models.base_model import BaseModel


class Review(BaseModel):
    """Contains the reivew made by users"""
    place_id = ""
    user_id = ""
    text = ""
