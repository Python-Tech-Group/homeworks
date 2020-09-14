
class Board(object):

    def __init__(self):
        self.marked_cells = 0
        self.board_position = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}

    def restart_board(self):
        self.marked_cells = 0
        self.board_position = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}


    def set_marker_cells(self, position, value):
        if self.marked_cells == 9:
            return False
        else:
            if 1 <= position <= 9:
                if self.board_position[position] == " ":
                    self.board_position[position] = value
                    self.marked_cells += 1
                    return True
                else:
                    return False
            else:
                return False


    def verify_win_cases(self):
        #rows
        if self.board_position[1] == self.board_position[2] == self.board_position[3] != " ":
            return self.board_position[1]
        elif self.board_position[4] == self.board_position[5] == self.board_position[6] != " ":
            return self.board_position[4]
        elif self.board_position[7] == self.board_position[8] == self.board_position[9] != " ":
            return self.board_position[7]
        #Columns
        elif self.board_position[1] == self.board_position[4] == self.board_position[7] != " ":
            return self.board_position[1]
        elif self.board_position[2] == self.board_position[5] == self.board_position[8] != " ":
            return self.board_position[2]
        elif self.board_position[3] == self.board_position[6] == self.board_position[9] != " ":
            return self.board_position[3]
        # diagonals
        elif self.board_position[1] == self.board_position[5] == self.board_position[9] != " ":
            return self.board_position[1]
        elif self.board_position[7] == self.board_position[5] == self.board_position[3] != " ":
            return self.board_position[7]
        else:
            return " "


