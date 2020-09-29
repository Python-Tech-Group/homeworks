from ..src.height_based_figure import HeightBasedFigure


class Rhombus(HeightBasedFigure):

    def print(self):
        j = 0
        figure = ""
        for i in range(1, self.height + 1):
            for gap in range(1, (self.height - i) + 1):
                figure += ' '
            while j != (2 * i - 1):
                figure += self.char
                j = j + 1
            j = 0
            figure += '\n'
        for i in range(self.height - 1, 0, -1):
            for gap in range(1, (self.height - i) + 1):
                figure += ' '
            while j != (2 * i - 1):
                figure += self.char
                j = j + 1
            j = 0
            figure += '\n'
        return figure
