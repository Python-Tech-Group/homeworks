import os
import unittest

from src import reader


class TestReader(unittest.TestCase):

    def setUp(self):
        self.path = os.path.abspath("../../source_data D.txt")
        self.reader = reader.Reader(self.path)

    def test_read_file(self):
        # Verify that get_file method is reading the txt file and returning the content of it
        file = self.reader.get_file()
        self.assertEqual(1336, len(file))

    def test_split_rows(self):
        # Verify that text file contains 16 accounts
        rows = self.reader.split_rows()
        self.assertEqual(16, len(rows))

    def test_split_row_columns(self):
        # Verify that each row contains 9 numbers
        rows = self.reader.split_rows()
        for row in range(len(rows)):
            account_numbers = self.reader.split_row_columns(row)
            with self.subTest(account_numbers=account_numbers):
                self.assertEqual(9, len(account_numbers))

    def test_read_file_failure(self):
        # Verify that reader return empty string if file isn't end with txt
        self.reader = reader.Reader(self.path + "error")
        file = self.reader.get_file()
        self.assertEqual(0, len(file))

    def test_split_rows_failure(self):
        # Verify that wrong read of file return a empty row
        self.reader = reader.Reader(self.path + "error")
        rows = self.reader.split_rows()
        self.assertEqual(1, len(rows))
        self.assertEqual([""], rows)

    def test_split_row_columns_failure(self):
        # Verify that even empty row contains 9 columns empty as numbers
        self.reader = reader.Reader(self.path + "error")
        rows = self.reader.split_rows()
        empty_number = "   \n   \n   "
        for row in range(len(rows)):
            account_numbers = self.reader.split_row_columns(row)
            with self.subTest(account_numbers=account_numbers):
                self.assertEqual(9, len(account_numbers))
            for account_number in account_numbers:
                with self.subTest(account_number=account_number):
                    self.assertEqual(empty_number, account_number)