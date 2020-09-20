from core.account import Account


class Validator():

    def __init__(self):
        pass

    def validate_account(self, array_numbers):
        account = Account(array_numbers, "OK")
        factor = 1
        sum_checksum = 0
        counter_range = 8
        while counter_range > -1:
            if array_numbers[counter_range] != "?":
                sum_checksum += (factor * array_numbers[counter_range])
                counter_range -= 1
                factor += 1
            else:
                account.set_label("ILL")
                break

        if (sum_checksum % 11) != 0 and account.label != "ILL":
            account.set_label("ERR")

        account.convert_to_account_data()
        return account

