from src.menu import Menu
from src.figure import Rectangle, Triangle, Rhombus


class Printer(object):
    LIMIT_INIT = 1
    LIMIT_END = 30

    def __init__(self):
        self.options = {
            1: "Rectangle",
            2: "Triangle",
            3: "Rhombus",
            4: "Print",
            5: "Exit"
        }
        self.menu = Menu()
        self.figures = []

    def add_rectangle(self):
        width = self.menu.get_input_number("width", self.LIMIT_INIT, self.LIMIT_END)
        height = self.menu.get_input_number("height", self.LIMIT_INIT, self.LIMIT_END)
        char_printer = self.menu.get_input_char("char(e.g.: *)")
        return Rectangle("Rectangle", width, height, char_printer)

    def add_triangle(self):
        height = self.menu.get_input_number("height", self.LIMIT_INIT, self.LIMIT_END)
        char_printer = self.menu.get_input_char("char(e.g.: *)")
        return Triangle("Triangle", height, char_printer)

    def add_rhombus(self):
        height = self.menu.get_input_number("height odd", self.LIMIT_INIT, self.LIMIT_END, True)
        char_printer = self.menu.get_input_char("char(e.g.: *)")
        return Rhombus("Rhombus", height, char_printer)

    def start_program(self):
        # Start Playing
        continue_running = True

        while continue_running:
            option = self.menu.select_option_number(self.options)

            if self.options[option] == "Exit":
                self.menu.exit_menu()
                continue_running = False
            elif self.options[option] == "Print":
                if len(self.figures) > 0:
                    self.menu.print_figure(self.figures)
                    self.restart_printer()
                else:
                    self.menu.print_message("Please, select at least one shape option.")
            elif self.options[option] == "Rectangle":
                self.figures.append(self.add_rectangle())
            elif self.options[option] == "Triangle":
                self.figures.append(self.add_triangle())
            elif self.options[option] == "Rhombus":
                self.figures.append(self.add_rhombus())

    def restart_printer(self):
        self.menu = Menu()
        self.figures = []
        self.start_program()
