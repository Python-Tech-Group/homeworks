

class Figure(object):

    def __init__(self, name, char="*"):
        self.name = name
        self.char = char
        self.output_share = self.name

    def get_share_as_string(self):
        self.output_share += "\n"


class Rectangle(Figure):

    def __init__(self, name, width=0, height=0, char="*"):
        super(Rectangle, self).__init__(name, char)
        self.width = width
        self.height = height
        self.get_share_as_string()

    def get_share_as_string(self):
        super(Rectangle, self).get_share_as_string()
        for output in range(self.height):
            self.output_share += self.char * self.width
            self.output_share += "\n"


class Triangle(Figure):

    def __init__(self, name, height=0, char="*"):
        super(Triangle, self).__init__(name, char)
        self.height = height
        self.get_share_as_string()

    def get_share_as_string(self):
        super(Triangle, self).get_share_as_string()
        for i_counter in range(self.height):

            # with spaces
            # aux = self.char+" "
            #self.output_share += " "*(self.height-1-i_counter) + aux*(i_counter+1)

            # without spaces
            self.output_share += (self.height - (i_counter + 1)) * " " + ((2*i_counter)+1) * self.char
            self.output_share += "\n"


class Rhombus(Figure):

    def __init__(self, name, height_odd=0, char="*"):
        super(Rhombus, self).__init__(name, char)
        self.height_odd = height_odd
        self.get_share_as_string()

    def get_share_as_string(self):
        super(Rhombus, self).get_share_as_string()

        for i_counter in range(self.height_odd):
            self.output_share += ' ' * (self.height_odd - i_counter - 1) + self.char * ((2 * i_counter) + 1)
            self.output_share += "\n"
        for i_counter in range(self.height_odd -1):
            self.output_share += ' ' * (i_counter + 1) + self.char * ((2 * ((self.height_odd - 1) - i_counter)) - 1)
            self.output_share += "\n"
