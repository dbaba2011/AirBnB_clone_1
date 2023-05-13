#!/usr/bin/python3
"""
    Defines the unittests for models/base_modle.py
    Uniittest classes:
    TestBase_save
    TestBase_json_format
    TestBase_instance(print here too)
    seModel_to_dict
"""

import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from datetime import datetime
from uuid import uuid4
import json
from time import sleep


class TestBase_Instance(unittest.TestCase):
    """Unittests for testing for instantiation fo BaseModel"""

    def test_isInstanceOf(self):
        """Test if instance is created"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        # test for subclass
        self.assertTrue(issubclass(type(b1), BaseModel))

    def test_id(self):
        """Test if the id is generated correctly and works properly"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertTrue(hasattr(b2, "id"))
        # test for type of id
        self.assertIsInstance(b1.id, str)

        # compare 2 instances
        self.assertNotEqual(b1.id, b2.id)

        # test uuid is valid (uses regex)
        self.assertRegex(b1.id,
                         '^[0-9a-f]{8}-[0-9a-f]{4}'
                         '-[0-9a-f]{4}-[0-9a-f]{4}'
                         '-[0-9a-f]{12}$')

    def test_created_at(self):
        """checks if the datetime module is implemented correctly"""
        date_now = datetime.now
        b1 = BaseModel()
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsNotNone(b1.created_at)
        self.assertEqual(type(b1.created_at).__name__, 'datetime')

    def test_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        b1 = BaseModel(id="123", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(b1.id, "123")
        self.assertEqual(b1.created_at, date)
        self.assertEqual(b1.updated_at, date)

    class TestBase_save(unittest.TestCase):
        """Unittest for testing save"""

        def test_safe(self):
            """Check if save is valid"""
            b1 = BaseModel()
            update1 = b1.updated_at
            b1.save()
            update2 = b1.updated_at
            self.assertNotEqual(update1, update2)
            b2 = BaseModel()
            sleep(0.05)
            update1 = b2.updated_at
            b2.save()
            update2 = b2.updated_at
            self.assert_Less(update1, update2)
            sleep(0.05)
            b1.save()
            self.assertLess(update2, b1.updated_at)

    class TestBase_Ditc_Methods(unittest.TestCase):
        """Class to test for to_dict method of the baseModel class"""

        def test_classname(self):
            """Test for the class name"""
            b1 = BaseModel
            dic = b1.to_dict()
            self.assertNotEqual(dic, b1.__dict__)

        def test_isoformat(self):
            """test for the iso format"""
            b1 = BaseModel()
            dic = b1.to_dict()
            self.assertIsInstance(dic['created_at'], str)
            self.assertIsInstance(dic["update_at"], str)

        def test_keys(self):
            """Test for correct keys"""
            model = BaseModel()
            self.assertIn("id", model.to_dict())
            self.assertIn("create_at", model.to_dict())
            self.assertIn("updated_at", model.to_dict())
            self.assertIn("__class__", model.to_dict())

        def test_todict(self):
            """Test for the dict output"""
            date = datetime.now
            b1 = BaseModel()
            b1.id = "12345"
            b1.created_at = b1.updated_at = date
            b1dict = {
                'id': '123456',
                '__class__': 'BaseModel',
                'created_at': date.isoformat(),
                'updated_at': date.isoformat()
            }
            self.assertDictEqual(b1.to_dict(), b1dict)

        def test_todict_withdunderdict_(self):
            """Test with the dunder dict"""
            b1 = BaseModel()
            self.assertNotEqual(b1.to_dict(), b1.__dict__)

        def test_dict_with_args(self):
            b1 = BaseModel()
            with self.assertRaises(TypeError):
                b1.to_dict(None)
