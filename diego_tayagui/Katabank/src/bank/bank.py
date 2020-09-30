from src import reader
from src import interpreter
from src import generator


class Bank:

    def __init__(self, path):
        self.read = reader.Reader(path)
        self.interpret = interpreter.Interpreter()
        self.generator = generator.Generator()
        self.string_accounts = [self.read.split_row_columns(i) for i in range(0, len(self.read.split_rows()))]
        self.accounts = self.read_accounts()

    def validate_account(self, account):
        """ Validate accounts by index given of the account needed """
        res = 0
        if "?" not in account:
            for i, number in enumerate(account[::-1]):
                res += (i + 1) * int(number)
        else:
            res = 1
        return False if res % 11 else True

    def read_accounts(self):
        """ Read all accounts of a text file"""
        accounts = []
        for i, string_account in enumerate(self.string_accounts):
            accounts.append("")
            for string_number in string_account:
                number = self.interpret.read_number(string_number)
                accounts[i] += number or "?"
        return accounts

    def fix_account(self, index):
        """ Fix account given by index based on type of error that has """
        account = self.accounts[index]
        if "?" in account:
            return self.fill_account(index, account)
        elif not self.validate_account(account):
            possible_accounts = []
            for i in range(0, len(account)):
                possible_account = account[0:i] + '?' + account[i + 1:]
                possible_account = self.fill_account(index, possible_account)
                if self.validate_account(possible_account):
                    possible_accounts.append(possible_account)
            return possible_accounts
        else:
            return account

    def fill_account(self, index, account):
        """
        Verify if account has ? and calls generator to get possible numbers by it's patterns
        then check one peer one until found a valid account between the possibilities
        """
        if self.validate_account(account):
            return account
        elif "?" in account:
            number_index = account.find("?")
            possible_numbers = self.generator.guess_number(self.string_accounts[index][number_index])
            for i, number in enumerate(possible_numbers):
                account = account.replace("?", str(number), 1)
                account = self.fill_account(index, account)
                if not self.validate_account(account):
                    account = account[0:number_index] + '?' + account[number_index + 1:]
                    if i is len(possible_numbers) - 1:
                        return account
                else:
                    return account
        else:
            return account

    def print_accounts(self):
        """ Print accounts according to the validation of it"""
        output = []
        for i, account in enumerate(self.accounts):
            if not self.validate_account(account):
                account_fixed = self.fix_account(i)
                if "?" in self.accounts[i] and "?" not in account_fixed:
                    output.append(account_fixed)
                elif "?" not in self.accounts[i]:
                    if len(account_fixed) > 1:
                        output.append(self.accounts[i] + " AMD " + str(account_fixed))
                    else:
                        output.append(account_fixed[0])
                else:
                    output.append(self.accounts[i] + " ILL" if "?" in self.accounts[i] else " ERR")
            else:
                output.append(account)
        return output
