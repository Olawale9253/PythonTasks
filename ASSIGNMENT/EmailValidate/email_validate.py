import unittest
from pybank import validate_email

class TestValidateEmail(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(validate_email("user@mail.com"))

    def test_too_short(self):
        self.assertFalse(validate_email("a@b.c"))

    def test_no_at_symbol(self):
        self.assertFalse(validate_email("usermail.com"))

    def test_starts_with_at(self):
        self.assertFalse(validate_email("@mail.com"))

    def test_ends_with_at(self):
        self.assertFalse(validate_email("user@mail.com@"))

if __name__ == "__main__":
    unittest.main()
