import unittest

from app.models import User


class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password='cat')
        self.assertIsNotNone(u.password_hash)

    def test_no_password_getter(self):
        u = User()
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))
