import unittest
from src import generator


class TestGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = generator.Generator()

    def test_count_concurrences(self):
        # Verify Generator count concurrences of a given string based on it´s header, body and footer
        test = "   \n  |\n  |"
        self.assertEqual([0, 1, 1], self.generator.count_concurrences(test))

    def test_count_concurrences_out_scope(self):
        # Verify Generator count concurrences of a given string based on it´s header, body and footer
        test = " + \n  |\n  |"
        self.assertEqual([0, 1, 1], self.generator.count_concurrences(test))

    def test_guess_number(self):
        # Verify Generator can guess possible numbers based on similar patterns
        test = "   \n|_|\n   "
        self.assertEqual([4], self.generator.guess_number(test))

    def test_guess_numbers_with_different_possibilities(self):
        # Verify Generator can guess possible numbers based on similar patterns
        test = " _ \n|_|\n _|"
        self.assertEqual([3, 5, 8, 9], self.generator.guess_number(test))

    def test_check_possible_numbers(self):
        # Verify Generator return possible numbers based on concurrency check by the Interpreter
        test = " _ \n|_|\n _|"
        self.assertEqual([3, 5, 8, 9], self.generator.check_possible_numbers(test))

    def test_check_possible_numbers_singular(self):
        # Verify Generator return possible numbers based on concurrency check by the Interpreter
        test = "   \n|_|\n   "
        self.assertEqual([4], self.generator.check_possible_numbers(test))
