

class Figure(object):

    def __init__(self, name, char="*"):
        self.name = name
        self.char = char
        self.output_shape = ""

    def build_shape_as_string(self):
        pass


class Rectangle(Figure):

    def __init__(self, name, width=0, height=0, char="*"):
        super(Rectangle, self).__init__(name, char)
        self.width = width
        self.height = height
        self.build_shape_as_string()

    def build_shape_as_string(self):
        super(Rectangle, self).build_shape_as_string()
        for output in range(self.height):
            self.output_shape += self.char * self.width
            self.output_shape += "\n"


class Triangle(Figure):

    def __init__(self, name, height=0, char="*"):
        super(Triangle, self).__init__(name, char)
        self.height = height
        self.build_shape_as_string()

    def build_shape_as_string(self):
        super(Triangle, self).build_shape_as_string()
        for i_counter in range(self.height):

            self.output_shape += (self.height - (i_counter + 1)) * " " + ((2*i_counter)+1) * self.char
            self.output_shape += "\n"


class Rhombus(Figure):

    def __init__(self, name, height_odd=0, char="*"):
        super(Rhombus, self).__init__(name, char)
        self.height_odd = height_odd
        self.build_shape_as_string()

    def build_shape_as_string(self):
        super(Rhombus, self).build_shape_as_string()

        for i_counter in range(self.height_odd):
            self.output_shape += ' ' * (self.height_odd - i_counter - 1) + self.char * ((2 * i_counter) + 1)
            self.output_shape += "\n"
        for i_counter in range(self.height_odd -1):
            self.output_shape += ' ' * (i_counter + 1) + self.char * ((2 * ((self.height_odd - 1) - i_counter)) - 1)
            self.output_shape += "\n"
