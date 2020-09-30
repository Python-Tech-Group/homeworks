
class HelperAccountNumber:
    @staticmethod
    def checksum(number_tuple):
        sum = 0
        factor = 1
        for digit in number_tuple[::-1]:
            if digit == -1:
                return False

            sum += factor * int(digit)
            factor += 1

        return (sum % 11) == 0

    @staticmethod
    def format_account_number(number_tuple):
        is_valid_number = HelperAccountNumber.checksum(number_tuple)
        str_number = HelperAccountNumber.__number_to_str(number_tuple)
        if not is_valid_number:
            return HelperAccountNumber.__error_format(str_number)
        return str_number

    @staticmethod
    def __number_to_str(number_tuple):
        str_number = ''.join(str(e) for e in number_tuple)
        return str_number.replace("-1", "?")

    @staticmethod
    def __error_format(str_number):
        return "%s %s" % (str_number, "ILL")
