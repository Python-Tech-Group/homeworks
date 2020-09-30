class BankOCR:
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    NINE = 9
    ELEVEN = 11
    QUESTION_MARK = "?"
    ACCOUNT = [" _ | ||_|",
               "     |  |",
               " _  _||_ ",
               " _  _| _|",
               "   |_|  |",
               " _ |_  _|",
               " _ |_ |_|",
               " _   |  |",
               " _ |_||_|",
               " _ |_| _|",
               " _ | ||_|",
               "     |  |",
               " _  _||_ ",
               " _  _| _|",
               "   |_|  |",
               " _ |_  _|",
               " _ |_ |_|",
               " _   |  |",
               " _ |_||_|",
               " _ |_| _|"]

    def __init__(self):
        pass

    def get_digit(self, number):
        """
        :param number: is formed by pipes and underscores.
        :return: the value of the number, if it's not a number returns "?".
        """
        for index in range(len(self.ACCOUNT)):
            if self.ACCOUNT[index] == number:
                return str(index)
        return self.QUESTION_MARK

    def map_entry_ocr_to_number(self, lines):
        """
        :param lines: is a list of String pipes and underscores.
        :return: the String representation of the account number.
        """
        index = self.ZERO
        account = ""
        while index < len(lines[self.ZERO]):
            number = lines[self.ZERO][index: index + self.THREE] + \
                     lines[self.ONE][index: index + self.THREE] + \
                     lines[self.TWO][index: index + self.THREE]
            account += str(self.get_digit(number))
            index += self.THREE
        return account

    def checksum(self, account_number):
        """
        :param account_number: is formed by 9 numbers.
        :return: if the account number is valid or not.
        """
        number_position = list(account_number)
        checksum = self.ZERO
        i = self.ZERO
        j = self.NINE

        while i < len(number_position):
            checksum += int(number_position[i]) * j
            i += self.ONE
            j -= self.ONE

        return checksum % self.ELEVEN == self.ZERO

    def get_findings(self, account_number):
        """
        :param account_number: the account number to evaluate.
        :return: whether the account number is valid.
        """
        if self.QUESTION_MARK in account_number:
            return "{} ILL".format(account_number)
        return "{} ERR".format(account_number) if not self.checksum(account_number) else account_number
