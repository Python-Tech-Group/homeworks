import unittest
import daniel_caballero.kata_bank_ocr.test.test_data as data
from ..src.BankOCR import BankOCR


class BankOCRTest(unittest.TestCase):
    bank_ocr = BankOCR()

    def test_map_entry_ocr_to_zero_numbers_account(self):
        actual_result = self.bank_ocr.map_entry_ocr_to_number(data.ALL_ZERO)
        expected_result = "000000000"
        self.assertEqual(actual_result, expected_result)

    def test_map_entry_ocr_to_one_numbers_account(self):
        actual_result = self.bank_ocr.map_entry_ocr_to_number(data.ALL_ONE)
        expected_result = "111111111"
        self.assertEqual(actual_result, expected_result)

    def test_map_entry_ocr_to_two_numbers_account(self):
        actual_result = self.bank_ocr.map_entry_ocr_to_number(data.ALL_TWO)
        expected_result = "222222222"
        self.assertEqual(actual_result, expected_result)

    def test_map_entry_ocr_to_three_numbers_account(self):
        actual_result = self.bank_ocr.map_entry_ocr_to_number(data.ALL_THREE)
        expected_result = "333333333"
        self.assertEqual(actual_result, expected_result)

    def test_map_entry_ocr_to_four_numbers_account(self):
        actual_result = self.bank_ocr.map_entry_ocr_to_number(data.ALL_FOUR)
        expected_result = "444444444"
        self.assertEqual(actual_result, expected_result)

    def test_map_entry_ocr_to_five_numbers_account(self):
        actual_result = self.bank_ocr.map_entry_ocr_to_number(data.ALL_FIVE)
        expected_result = "555555555"
        self.assertEqual(actual_result, expected_result)

    def test_map_entry_ocr_to_six_numbers_account(self):
        actual_result = self.bank_ocr.map_entry_ocr_to_number(data.ALL_SIX)
        expected_result = "666666666"
        self.assertEqual(actual_result, expected_result)

    def test_map_entry_ocr_to_seven_numbers_account(self):
        actual_result = self.bank_ocr.map_entry_ocr_to_number(data.ALL_SEVEN)
        expected_result = "777777777"
        self.assertEqual(actual_result, expected_result)

    def test_map_entry_ocr_to_eight_numbers_account(self):
        actual_result = self.bank_ocr.map_entry_ocr_to_number(data.ALL_EIGHT)
        expected_result = "888888888"
        self.assertEqual(actual_result, expected_result)

    def test_map_entry_ocr_to_nine_numbers_account(self):
        actual_result = self.bank_ocr.map_entry_ocr_to_number(data.ALL_NINE)
        expected_result = "999999999"
        self.assertEqual(actual_result, expected_result)

    def test_map_entry_ocr_to_all_numbers_account(self):
        actual_result = self.bank_ocr.map_entry_ocr_to_number(data.ALL_NUMBERS)
        expected_result = "123456789"
        self.assertEqual(actual_result, expected_result)

    def test_checksum_account_number_is_true(self):
        account_number = "345882865"
        actual_result = self.bank_ocr.checksum(account_number)
        self.assertTrue(actual_result)

    def test_checksum_account_number_is_false(self):
        account_number = "686381269"
        actual_result = self.bank_ocr.checksum(account_number)
        self.assertFalse(actual_result)

    def test_finding_checksum_error_account_number(self):
        actual_result = self.bank_ocr.get_findings(self.bank_ocr.map_entry_ocr_to_number(data.INVALID_CHECKSUM))
        expected_result = "123456189 ERR"
        self.assertEqual(actual_result, expected_result)

    def test_finding_illegible_account_number(self):
        actual_result = self.bank_ocr.get_findings(self.bank_ocr.map_entry_ocr_to_number(data.ILLEGIBLE_ACCOUNT))
        expected_result = "?234???89 ILL"
        self.assertEqual(actual_result, expected_result)
