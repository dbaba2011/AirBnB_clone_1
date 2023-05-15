#!/usr/bin/python3
"""
This module contains unit tests for the Amenity class.
"""

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """
    This class contains unit tests for the Amenity class.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
        This method tests the 'name' attribute of Amenity.
        """
        new = self.value()
        self.assertEqual(type(n
