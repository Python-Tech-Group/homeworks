from ..src.figure import Figure


class Rectangle(Figure):

    def __init__(self, width, height, char):
        super().__init__(char)
        self.width = width
        self.height = height

    def print(self):
        figure = ""
        for i in range(self.height):
            for j in range(self.width):
                figure += self.char
            figure += '\n'
        return figure
