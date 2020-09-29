import sys

from daniel_caballero.printer_project.src.rectangle import Rectangle
from daniel_caballero.printer_project.src.rhombus import Rhombus
from daniel_caballero.printer_project.src.triangle import Triangle


class FiguresPrinter:

    def __init__(self):
        self.figures = []
        self.main()

    def main(self):
        print("\n")
        print("Printer Project")
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Rhombus")
        print("4. Print!")
        print("5. Exit")
        choice = input("Please enter your choice: ")
        print("\n")
        if choice == "1":
            self.print_rectangle_menu()
        elif choice == "2":
            self.print_triangle_menu()
        elif choice == "3":
            self.print_rhombus_menu()
        elif choice == "4":
            self.print_figure()
        elif choice == "5":
            sys.exit()
        else:
            print("You must only select either 1,2,3,4 or 5")
            print("Please try again")
            self.main()

    def print_rectangle_menu(self):

        print("Rectangle")
        while True:
            try:
                width = int(input("Enter width: "))
                height = int(input("Enter height: "))
                char = input("Enter char: ")
                throw_char_length_exception(char)
                break
            except ValueError:
                print("No valid integer! Please try again ...")
            except CharLengthError:
                print("Char length must be 1!!")
        self.figures.append(Rectangle(width, height, char))
        self.main()

    def print_triangle_menu(self):
        print("Triangle")
        while True:
            try:
                height = int(input("Enter height: "))
                char = input("Enter char: ")
                throw_char_length_exception(char)
                break
            except ValueError:
                print("No valid integer! Please try again ...")
            except CharLengthError:
                print("Char length must be 1!!")
        self.figures.append(Triangle(height, char))
        self.main()

    def print_rhombus_menu(self):
        print("Rhombus")
        while True:
            try:
                height = int(input("Enter height (odd number): "))
                if (height % 2) == 0:
                    raise Exception("Only odd numbers are allowed")
                char = input("Enter char: ")
                throw_char_length_exception(char)
                break
            except ValueError:
                print("No valid integer! Please try again ...")
            except CharLengthError:
                print("Char length must be 1!!")
            except Exception:
                print("Height must be an odd number!!")
        self.figures.append(Rhombus(height, char))
        self.main()

    def print_figure(self):
        if self.figures:
            for figure in self.figures:
                print(figure.print())
        else:
            print("You must first create a figure before printing!!")
        self.main()


class CharLengthError(Exception):
    """Raised when the char length is greater than one. """

    def __init__(self, char, message="Char length must be 1!!"):
        self.char = char
        self.message = message
        super().__init__(self.message)


def throw_char_length_exception(char):
    if len(char) > 1:
        raise CharLengthError("Char length must be 1!!")


printer = FiguresPrinter()
printer.__init__()
