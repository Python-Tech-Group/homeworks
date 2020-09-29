from daniel_caballero.printer_project.src.figure import Figure
import abc


class HeightBasedFigure(Figure):

    def __init__(self, height, char):
        super().__init__(char)
        self.height = height

    @abc.abstractmethod
    def print(self):
        pass
