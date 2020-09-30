
class ParseAccountNumber:
    def __init__(self):
        self.__number_codes = {
            ' _ | ||_|': 0,
            '     |  |': 1,
            ' _  _||_ ': 2,
            ' _  _| _|': 3,
            '   |_|  |': 4,
            ' _ |_  _|': 5,
            ' _ |_ |_|': 6,
            ' _   |  |': 7,
            ' _ |_||_|': 8,
            ' _ |_| _|': 9
        }

    def parse(self, input_data):
        cells = self.__get_cells(input_data)
        cell_values = []
        for cell in cells:
            cell_values.append(self.__get_cell_value(cell))

        return tuple(cell_values)

    def __get_cells(self, input_data):
        cells = []
        lines = self.__get_lines(input_data)

        for offset in range(0, 26, 3):
            cell = lines[0][offset:offset + 3]
            cell += lines[1][offset:offset + 3]
            cell += lines[2][offset:offset + 3]

            cells.append(cell)

        return cells

    def __get_lines(self, input_data):
        lines = ["", "", ""]
        offset = 0

        for char in input_data:
            lines[offset] += char
            if len(lines[offset]) == 27:
                offset += 1

        return lines

    def __get_cell_value(self, cell):
        return self.__number_codes.get(cell, -1)
