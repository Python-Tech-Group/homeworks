import unittest
from src.parser import KataParser
from src.manager import Manager


class PhaseOneTest(unittest.TestCase, KataParser, Manager):

    def test_read_zeroes(self):
        input = " _  _  _  _  _  _  _  _  _ " \
                "| || || || || || || || || |" \
                "|_||_||_||_||_||_||_||_||_|"

        account_number = self.parser(input)
        self.assertTrue(account_number == ('0', '0', '0', '0', '0', '0', '0', '0', '0'))

    def test_read_ones(self):
        input = "                           " \
                "  |  |  |  |  |  |  |  |  |" \
                "  |  |  |  |  |  |  |  |  |"

        account_number = self.parser(input)
        self.assertTrue(account_number == ('1', '1', '1', '1', '1', '1', '1', '1', '1'))

    def test_get_lines(self):
        input = "                           " \
                "  |  |  |  |  |  |  |  |  |" \
                "  |  |  |  |  |  |  |  |  |"

        lines = self.get_cells(input)
        self.assertTrue(lines[0][0] == ' ')
        self.assertTrue(lines[1][1] == ' ')
        self.assertTrue(lines[2][2] == ' ')

    def test_get_cells(self):
        input = " _  _  _  _  _  _  _  _  _ " \
                "| || || || || || || || || |" \
                "|_||_||_||_||_||_||_||_||_|"

        cells = self.get_cells(input)

        self.assertTrue(self.format_cell(cells[0]) == " _ \n| |\n|_|")

    def test_read_from_one_to_nine(self):
        input = "    _  _     _  _  _  _  _ " \
                "  | _| _||_||_ |_   ||_||_|" \
                "  ||_  _|  | _||_|  ||_| _|"

        account_number = self.parser(input)
        self.assertTrue(account_number == ('1', '2', '3', '4', '5', '6', '7', '8', '9'))


if __name__ == '__main__':
    unittest.main()
