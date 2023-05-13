#!/usr/bin/python3
"""
This module contains unit tests for the Amenity class.
"""

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.base_model import BaseModel

class test_Amenity(test_basemodel):
    """
    This class contains unit tests for the Amenity class.
    """
    def test_instance(self):
        """Test if instance of amenity is created"""   
        a1 = Amenity()
        self.assertIsInstance(a1, Amenity)

    def test_issubclass(self):
        """Test if amenity is a subclass of BaseModels"""
        a1 = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """Test if amenity has the expected attributes"""
        a1 = Amenity()
        self.assertTrue(hasattr(a1, "name"))

    def test_attribute_types(self):
        """Test if amenity attributes are of the expected types"""
        a1 = Amenity()
        self.assertIsInstance(a1.name, str)

    def test_attribute_values(self):
        """Test if amenity attributes have the expected default values"""
        a1 = Amenity()
