
from src.parse_account_number import ParseAccountNumber
from src.parser_from_string import ParserFromString
from src.helper_account_number import HelperAccountNumber

parse = ParseAccountNumber()
inputData = " _  _  _  _  _  _  _  _  _ "\
            "|  | || || || || || || || |"\
            "|  |_||_||_||_||_||_||_||_|"

parser = ParserFromString(inputData, parse)
account_number = parser.account_number()
print(HelperAccountNumber.format_account_number(account_number))
