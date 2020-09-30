from src import interpreter
from functools import reduce
from collections import OrderedDict

import operator


class Generator:

    def __init__(self):
        self.interpreter = interpreter.Interpreter()
        self.numbers = {
            '0': [1, 2, 3],
            '1': [0, 1, 1],
            '2': [1, 2, 2],
            '3': [1, 2, 2],
            '4': [0, 3, 1],
            '5': [1, 2, 2],
            '6': [1, 2, 3],
            '7': [1, 1, 1],
            '8': [1, 3, 3],
            '9': [1, 3, 2],
        }

    def count_concurrences(self, number):
        """ Count every _ and | peer row and return it in a list"""
        lines = number.splitlines()[0:3]
        occurrences = [0, 0, 0]
        for i, line in enumerate(lines):
            occurrences[i] = line.count("|") + line.count("_")
        return occurrences

    def guess_number(self, string_number):
        """
        Check the concurrencies on the string given,
        Check possible numbers for each row analyzed
        And Compare that possible numbers with the example
        adding or removing a character
        """
        string_concurrency = self.count_concurrences(string_number)
        concurrency_values = self.check_possible_numbers(string_number)
        possible_number = []
        for item in concurrency_values:
            difference = 0
            for i, concurrency in enumerate(self.numbers[str(item)]):
                difference += abs(concurrency - string_concurrency[i])
            if difference <= 1:
                possible_number.append(item)
        return possible_number

    def check_possible_numbers(self, string_number):
        """
        Check that every possible number given by the interpreter
        is repeated at least 2 times
        """
        number_concurrency = self.interpreter.check_concurrences(string_number)
        concurrency_values = reduce(operator.concat, number_concurrency.values())
        more_concurrent_numbers = [number
                                   for number in concurrency_values
                                   if concurrency_values.count(number) > 1]
        possible_numbers = list(OrderedDict.fromkeys(more_concurrent_numbers))
        return possible_numbers
