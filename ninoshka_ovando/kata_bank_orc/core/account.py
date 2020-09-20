class Account:

    def __init__(self, number, label=None):
        self.number = number
        self.label = label  # ERR, ILL , OK
        self.account_data = ""

    def set_number(self, number):
        self.number = number

    def set_label(self, label):
        self.label = label

    def convert_to_account_data(self):
        for digit in self.number:
            self.account_data += str(digit)
        if self.label == "ILL":
            self.account_data += " ILL"
        elif self.label == "ERR":
            self.account_data += " ERR"
