import unittest
from src.parse_account_number import ParseAccountNumber
from src.helper_account_number import HelperAccountNumber


class TestParseAccountNumber(unittest.TestCase):
    def test_read_zeroes(self):
        input_data = " _  _  _  _  _  _  _  _  _ "\
                     "| || || || || || || || || |"\
                     "|_||_||_||_||_||_||_||_||_|"

        account_number = ParseAccountNumber().parse(input_data)
        self.assertEqual(account_number, (0, 0, 0, 0, 0, 0, 0, 0, 0))

    def test_read_numbers(self):
        input_data = "    _  _     _  _  _  _  _ "\
                     "  | _| _||_||_ |_   ||_||_|"\
                     "  ||_  _|  | _||_|  ||_| _|"

        account_number = ParseAccountNumber().parse(input_data)
        self.assertEqual(account_number, (1, 2, 3, 4, 5, 6, 7, 8, 9))

    def test_read_error_number(self):
        input_data = "    _  _  _  _  _  _     _ "\
                     "|_||_|| || ||_   |  |  | _ "\
                     "  | _||_||_||_|  |  |  | _|"

        account_number = ParseAccountNumber().parse(input_data)
        self.assertEqual(account_number, (4, 9, 0, 0, 6, 7, 7, 1, -1))

    def test_valid_account_number(self):
        input_data = "    _  _     _  _  _  _  _ " \
                     "  | _| _||_||_ |_   ||_||_|" \
                     "  ||_  _|  | _||_|  ||_| _|"

        account_number = ParseAccountNumber().parse(input_data)
        valid_account_number = HelperAccountNumber.checksum(account_number)
        self.assertTrue(valid_account_number)

    def test_invalid_account_number(self):
        input_data = "    _  _  _  _  _  _     _ " \
                     "| ||_|| || ||_   |  |  | _ " \
                     "  | _||_||_||_|  |  |  | _|"

        account_number = ParseAccountNumber().parse(input_data)
        invalid_account_number = HelperAccountNumber.checksum(account_number)
        self.assertFalse(invalid_account_number)


if __name__ == '__main__':
    unittest.main()
