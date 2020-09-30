import unittest
import data.data_without_file as data
from core.parser import Parser
import numpy as np


class Test(unittest.TestCase):
    parser = Parser()

    def test_read_zeroes(self):
        valid_account_output = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT000)
        np.testing.assert_array_almost_equal(calculated_account_number, valid_account_output, 2)

    def test_read_ones_to_nines(self):
        valid_account_output = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT111)
        np.testing.assert_array_almost_equal(calculated_account_number, valid_account_output, 2)

        valid_account_output = [2, 2, 2, 2, 2, 2, 2, 2, 2]
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT222)
        np.testing.assert_array_almost_equal(calculated_account_number, valid_account_output, 2)

        valid_account_output = [3, 3, 3, 3, 3, 3, 3, 3, 3]
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT333)
        np.testing.assert_array_almost_equal(calculated_account_number, valid_account_output, 2)

        valid_account_output = [4, 4, 4, 4, 4, 4, 4, 4, 4]
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT444)
        np.testing.assert_array_almost_equal(calculated_account_number, valid_account_output, 2)

        valid_account_output = [5, 5, 5, 5, 5, 5, 5, 5, 5]
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT555)
        np.testing.assert_array_almost_equal(calculated_account_number, valid_account_output, 2)

        valid_account_output = [6, 6, 6, 6, 6, 6, 6, 6, 6]
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT666)
        np.testing.assert_array_almost_equal(calculated_account_number, valid_account_output, 2)

        valid_account_output = [7, 7, 7, 7, 7, 7, 7, 7, 7]
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT777)
        np.testing.assert_array_almost_equal(calculated_account_number, valid_account_output, 2)

        valid_account_output = [8, 8, 8, 8, 8, 8, 8, 8, 8]
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT888)
        np.testing.assert_array_almost_equal(calculated_account_number, valid_account_output, 2)

        valid_account_output = [9, 9, 9, 9, 9, 9, 9, 9, 9]
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT999)
        np.testing.assert_array_almost_equal(calculated_account_number, valid_account_output, 2)

    def test_read_serie_number(self):
        valid_account_output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT123)
        np.testing.assert_array_almost_equal(calculated_account_number, valid_account_output, 2)

    def test_read_invalid_digit(self):
        valid_account_output = [1, 2, 3, 4, 5, 6, 7, 8, "?"]
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT123_INVALID)

        self.assertListEqual(calculated_account_number, valid_account_output)

    def test_read_invalid_digit_ill(self):
        valid_account_output = [4, 9, 0, 0, 6, 7, 7, 1, "?"]
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT_WITH_ILL)

        self.assertListEqual(calculated_account_number, valid_account_output)

    def test_read_invalid_digits_ill(self):
        valid_account_output = [1, 2, 3, 4, "?", 6, 7, 8, "?"]
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT_WITH_ILLS)

        self.assertListEqual(calculated_account_number, valid_account_output)

    def test_read_invalid_digits_ill_all(self):
        valid_account_output = ["?", "?", "?", "?", "?", "?", "?", "?", "?"]
        calculated_account_number = self.parser.parse_an_account_number(data.INPUT_WITH_ILLS_ALL)

        self.assertListEqual(calculated_account_number, valid_account_output)
