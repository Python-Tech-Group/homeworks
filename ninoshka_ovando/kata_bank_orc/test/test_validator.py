import unittest
import data.data_without_file as data
from core.parser import Parser
from core.validator import Validator


class TestParser(unittest.TestCase):
    parser = Parser()
    validator = Validator()

    def test_read_invalid_account_number_ill(self):
        valid_account_output = "12345678? ILL"
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT123_INVALID)
        account_ill = self.validator.validate_account(calculated_account_number)
        self.assertEqual(account_ill.account_data, valid_account_output)

    def test_read_invalid_digits_ill_all(self):
        valid_account_output = "????????? ILL"
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT_WITH_ILLS_ALL)
        account_ill = self.validator.validate_account(calculated_account_number)
        self.assertEqual(account_ill.account_data, valid_account_output)

    def test_read_checksumm_valid_one(self):
        valid_account_output = "000000051"
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT_VALID_CHECKSUM1)
        account_ill = self.validator.validate_account(calculated_account_number)
        self.assertEqual(account_ill.account_data, valid_account_output)

    def test_read_checksumm_valid_two(self):
        valid_account_output = "345882865"
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT_VALID_CHECKSUM2)
        account_ill = self.validator.validate_account(calculated_account_number)
        self.assertEqual(account_ill.account_data, valid_account_output)

    def test_read_checksumm_invalid(self):
        valid_account_output = "664371495 ERR"
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT_INVALID_CHECKSUM)
        account_ill = self.validator.validate_account(calculated_account_number)
        self.assertEqual(account_ill.account_data, valid_account_output)
