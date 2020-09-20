
class Parser:
    VALID_VALUES = {
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

    def __init__(self):
        self.scan_name = "My scan"

    def parse_an_account_number(self, account_number_origin_format_lines):
        cells = self.get_array_cells(account_number_origin_format_lines)
        cell_values = []
        for cell in cells:
            cell_values.append(self.get_digit_value_number(cell))

        return cell_values

    def get_digit_value_number(self, cell_format_origin):
        #If a candidate number is not valid in VALID_VALUES, this will be replaced by ?
        return self.VALID_VALUES.get(cell_format_origin, "?")

    def get_a_case_with_three_lines(self, input_case_lines):
        lines = ["", "", ""]
        number_line = 0

        for line in input_case_lines:
            lines[number_line] += line
            if len(lines[number_line]) == 27:
                number_line += 1

        return lines

    def get_array_cells(self, source_case):
        #this returns 9 candidate cells numbers from an account scan number
        cells = []

        # copy into lines
        lines = self.get_a_case_with_three_lines(source_case)

        for three_cells in range(0, 26, 3):
            # sub string with range 3 cells by 3 cells
            # get sub string from each three lines
            cell = lines[0][three_cells:three_cells + 3]
            cell += lines[1][three_cells:three_cells + 3]
            cell += lines[2][three_cells:three_cells + 3]

            cells.append(cell)

        return cells
