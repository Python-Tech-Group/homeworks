class Computer:

    def __init__(self):
        self._description = "PC Computer Base"
        self.__maxprice = 900

    def sell(self):
        print("Selling: {}, Price: {}".format(self._description, self.__maxprice, ))

    def set_description(self, description):
        self._description = description

    def set_max_price(self, price):
        self.__maxprice = price


class NotebookComputer(Computer):
    def __init__(self):
        Computer.__init__(self)
        self._description = "Notebook Derived"
        self.__maxprice = 1000

    def sell(self):
        Computer.sell(self)

    def set_description(self, description):
        self._description = description

    def set_max_price(self, price):
        self.__maxprice = price


"""------BASE CLASS------"""
print("------BASE CLASS------")
computer = Computer()
computer.sell()

# changing attributes
computer._description = "PC HP Desktop 2020"
computer.__maxprice = 1000
computer.sell()

# using setter function
computer.set_description("Brand New PC 2020")
computer.set_max_price(1000)
computer.sell()
print("\n")

"""------DERIVED CLASS------"""
print("------DERIVED CLASS------")
notebook_pc = NotebookComputer()
notebook_pc.sell()

# Attempt to change attributes
notebook_pc._description = "Macbook Pro 16\""
notebook_pc.__maxprice = 2500
notebook_pc.sell()

# using setter function
notebook_pc.set_description("Dell XPS 13 2020")
notebook_pc.set_max_price(2000)
notebook_pc.sell()
