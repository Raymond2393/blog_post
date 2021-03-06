import unittest
from app.models import User


class UserModelTestCase(unittest.TestCase):

    def test_password_setter(self):
        u = User(password = 'don')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password = 'don')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password = 'don')
        self.assertTrue(u.verify_password('don'))
        self.assertFalse(u.verify_password('ted'))
