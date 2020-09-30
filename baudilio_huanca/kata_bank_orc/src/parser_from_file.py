
class ParserFromFile:
    def __init__(self, file_path, parse_account_number):
        self.__file_path = file_path
        self.__parse = parse_account_number

    def account_number(self):
        account_numbers = []
        line_count = 0
        number_lines = ''
        with open(self.__file_path, 'r') as f:
            for line in f:
                line_count += 1

                if (line_count % 4) == 0:
                    account_numbers.append(self.__parse.parse(number_lines))
                    number_lines = ''
                else:
                    number_lines += line.rstrip('\n')

        return account_numbers
