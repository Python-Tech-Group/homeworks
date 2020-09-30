
class Shape:
    def __init__(self, char):
        self.char = char
        self.space = " "

    def print_figure(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height, char):
        Shape.__init__(self, char)
        self.width = width
        self.height = height

    def print_figure(self):
        print("Rectangle")
        for i in range(self.height):
            for j in range(self.width):
                print('%c' % "*", end='')
            print()
        print("\n")


class Triangle(Shape):
    def __init__(self, height, char):
        Shape.__init__(self, char)
        self.height = height
        self.char = char

    def print_figure(self):
        print("Triangle")
        for i in range(self.height):
            print((self.height - (i + 1)) * self.space + ((2 * i) + 1) * self.char)
        print("\n")


class Rhombus(Shape):
    def __init__(self, height, char):
        Shape.__init__(self, char)
        self.height = (height-1) + height
        self.char = char

    def print_figure(self):
        print("Rhombus")
        for i in range(1, self.height + 1):
            i = i - (self.height // 2 + 1)
            if i < 0:
                i = -i
            print(self.space * i + "*" * (self.height - i * 2) + self.space * i)
        print("\n")


class Printer:
    def __init__(self):
        self.__shapes = None

    def print_shape(self, shapes):
        print("Printing Queue")
        for shape in shapes:
            shape.print_figure()


