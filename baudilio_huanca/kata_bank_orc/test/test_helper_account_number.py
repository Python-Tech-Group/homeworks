import unittest
from src.helper_account_number import HelperAccountNumber


class TestHelperAccountNumber(unittest.TestCase):
    def test_valid_account_number(self):
        tuple_account_number = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertTrue(HelperAccountNumber.checksum(tuple_account_number))

    def test_invalid_account_number(self):
        tuple_account_number = (-1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertFalse(HelperAccountNumber.checksum(tuple_account_number))

    def test_format_valid_account_number(self):
        tuple_account_number = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        str_number = HelperAccountNumber.format_account_number(tuple_account_number)
        self.assertEqual(str_number, "123456789")

    def test_format_invalid_account_number(self):
        tuple_account_number = (-1, 2, 3, 4, 5, 6, 7, 8, 9)
        str_number = HelperAccountNumber.format_account_number(tuple_account_number)
        self.assertEqual(str_number, "?23456789 ILL")


if __name__ == '__main__':
    unittest.main()
