#!/usr/bin/python3
"""This is the test file for the user class"""
import unittest
from models.user import User
from models.base_model import BaseModel

class Test_User(unittest.TestCase):
    """Test for the user class"""

    def test_instance(self):
        """Test if instance of user is created"""   
        u1 = User()
        self.assertIsInstance(u1, User)

    def test_issubclass(self):
        """Test if user is a subclass of BaseModels"""
        u1 = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """Test if user has the expected attributes"""
        u1 = User()
        self.assertTrue(hasattr(u1, "email"))
        self.assertTrue(hasattr(u1, "password"))
        self.assertTrue(hasattr(u1, "first_name"))
        self.assertTrue(hasattr(u1, "last_name"))

    def test_attribute_types(self):
        """Test if user attributes are of the expected types"""
        u1 = User()
        self.assertIsInstance(u1.email, str)
        self.assertIsInstance(u1.password, str)
        self.assertIsInstance(u1.first_name, str)
        self.assertIsInstance(u1.last_name, str)

    def test_attribute_values(self):
        """Test if user attributes have the expected default values"""
        u1 = User()
        self.assertEqual(u1.email, "")
        self.assertEqual(u1.password, "")
        self.assertEqual(u1.first_name, "")
        self.assertEqual(u1.last_name, "")
