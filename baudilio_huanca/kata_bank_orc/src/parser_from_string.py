from src.parse_account_number import ParseAccountNumber


class ParserFromString:
    def __init__(self, input_data, parse_account_number):
        self.__input_data = input_data
        self.__parser = parse_account_number

    def account_number(self):
        return self.__parser.parse(self.__input_data)


