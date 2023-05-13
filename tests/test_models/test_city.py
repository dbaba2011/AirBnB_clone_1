#!/usr/bin/python3
"""Tests for  city class"""

import unittest
from models.base_model import BaseModel
from models.city import City
class Test_City(unittest.TestCase):
    """Test for the city class"""
    
    def test_instance(self):
        """Test if instance of city is created"""   
        c1 = City()
        self.assertIsInstance(c1, City)

    def test_issubclass(self):
        """Test if city is a subclass of BaseModels"""
        c1 = City()
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """Test if city has the expected attributes"""
        c1 = City()
        self.assertTrue(hasattr(c1, "state_id"))
        self.assertTrue(hasattr(c1, "name"))

    def test_attribute_types(self):
        """Test if city attributes are of the expected types"""
        c1 = City()
        self.assertIsInstance(c1.state_id, str)
        self.assertIsInstance(c1.name, str)

    def test_attribute_values(self):
        """Test if city attributes have the expected default values"""
        c1 = City()
        self.assertEqual(c1.state_id, "")
        self.assertEqual(c1.name, "")
