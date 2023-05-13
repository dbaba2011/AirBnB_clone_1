#!/usr/bin/python3
"""Contains test for the state class"""
import unittest
from models.base_model import BaseModel
from models.state import State

class State(unittest.TestCase):
    """Test for the state class"""
    def test_instance(self):
        """Test if instance of state is created"""   
        s1 = State()
        self.assertIsInstance(s1, State)

    def test_issubclass(self):
        """Test if state is a subclass of BaseModels"""
        s1 = State()
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        """Test if state has the expected attributes"""
        s1 = State()
        self.assertTrue(hasattr(s1, "name"))

    def test_attribute_types(self):
        """Test if state attributes are of the expected types"""
        s1 = State()
        self.assertIsInstance(s1.name, str)

    def test_attribute_values(self):
        """Test if state attributes have the expected default values"""
        s1 = State()
        self.assertEqual(s1.name, "")
