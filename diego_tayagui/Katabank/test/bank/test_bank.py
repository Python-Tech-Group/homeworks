import os
import unittest
from src import bank


class TestBank(unittest.TestCase):

    def setUp(self):
        path = os.path.abspath("../../source_data D.txt")
        self.bank = bank.Bank(path)

    def test_validate_account(self):
        # Verify that first account is valid
        account = "86110??36"
        self.assertEqual(True, self.bank.validate_account(account))

    def test_validate_account_failure(self):
        # Verify that account is invalid
        account = "111111111"
        self.assertEqual(False, self.bank.validate_account(account))

    def test_read_accounts(self):
        # Verify that first account on the file is read and printed first
        self.assertEqual([
            "123456789",
            "000000000",
            "111111111",
            "222222222",
            "333333333",
            "888888888",
            "000000051",
            "49006771?",
            "1234?678?",
            "490067715",
            "777777777",
            "200000000",
            "345882865",
            "457508000",
            "664371495",
            "86110??36"
        ], self.bank.read_accounts())

    def test_print(self):
        """
        Verify that accounts with ? ends with ILL
        and invalid accounts with ERR
        """
        self.assertEqual([
            "123456789",
            "000000000",
            "111111111 ERR",
            "222222222 ERR",
            "333333333 ERR",
            "888888888 ERR",
            "000000051",
            "49006771? ILL",
            "1234?678? ILL",
            "490067715 ERR",
            "777777777 ERR",
            "200000000 ERR",
            "345882865",
            "457508000",
            "664371495 ERR",
            "86110??36 ILL"
        ], self.bank.print_accounts())

    def test_fix_account_incomplete(self):
        # Verify that incomplete account (1234?678?) with ? is resolved
        index = 8
        self.assertEqual("123456789", self.bank.fix_account(index))

    def test_fix_account_invalid(self):
        # Verify that invalid account (111111111) is valid making some changes
        index = 2
        self.assertEqual(["711111111"], self.bank.fix_account(index))

    def test_fix_account_multiple_accounts(self):
        # Verify that invalid account (88888888) has many variation to be valid
        index = 5
        self.assertEqual(sorted(["888886888", "888888880", "888888988"]), sorted(self.bank.fix_account(index)))