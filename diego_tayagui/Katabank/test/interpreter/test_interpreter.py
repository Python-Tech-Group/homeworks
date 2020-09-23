import unittest

from src import interpreter


class TestInterpreter(unittest.TestCase):

    def setUp(self):
        self.interpreter = interpreter.Interpreter()

    def test_check_concurrency(self):
        # Verify that Interpreter recognize similarity patterns based on a string given
        test = "   \n  |\n  |\n"
        self.assertEqual({
            'head': [1, 4],
            'body': [1, 7],
            'footer': [1, 4, 7]
        }, self.interpreter.check_concurrences(test))

    def test_check_concurrences_failure(self):
        # Verify that interpreter can't recognize similarities out of scope
        test = " + \n  |\n  |\n"
        self.assertEqual({
            'head': [],
            'body': [1, 7],
            'footer': [1, 4, 7]
        }, self.interpreter.check_concurrences(test))

    def test_read_number(self):
        # Verify that interpreter can recognize numbers based on similarity patterns
        test = "   \n  |\n  |\n"
        self.assertEqual("1", self.interpreter.read_number(test))

    def test_read_number_failure(self):
        # Verify that interpreter can't recognize numbers with different similarity patterns
        test = " + \n  |\n  |\n"
        self.assertEqual("", self.interpreter.read_number(test))

    def test_read_number_diff_patterns(self):
        # Verify that interpreter can't recognize numbers with different similarity patterns
        test = " _ \n _|\n|_|\n"
        self.assertEqual("", self.interpreter.read_number(test))
