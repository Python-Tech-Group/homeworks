import abc


class Figure:

    def __init__(self, char):
        self.char = char

    @abc.abstractmethod
    def print(self):
        pass
