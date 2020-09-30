import random


class Board(object):

    def __init__(self):
        self.marked_cells = 0
        self.board_position = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}

    def restart_board(self):
        self.marked_cells = 0
        self.board_position = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

    def verify_win_cases(self, icon):
        there_is_a_winner = False
        #rows
        if self.board_position[1] == self.board_position[2] == self.board_position[3] == icon:
            there_is_a_winner = True
        elif self.board_position[4] == self.board_position[5] == self.board_position[6] == icon:
            there_is_a_winner = True
        elif self.board_position[7] == self.board_position[8] == self.board_position[9] == icon:
            there_is_a_winner = True
        #Columns
        elif self.board_position[1] == self.board_position[4] == self.board_position[7] == icon:
            there_is_a_winner = True
        elif self.board_position[2] == self.board_position[5] == self.board_position[8] == icon:
            there_is_a_winner = True
        elif self.board_position[3] == self.board_position[6] == self.board_position[9] == icon:
            there_is_a_winner = True
        # diagonals
        elif self.board_position[1] == self.board_position[5] == self.board_position[9] == icon:
            there_is_a_winner = True
        elif self.board_position[7] == self.board_position[5] == self.board_position[3] == icon:
            there_is_a_winner = True
        return there_is_a_winner

    def get_empty_cells(self):
        empty_cell_list = []
        for i in range(1, 10):
            if self.board_position[i] == " ":
                empty_cell_list.append(i)
        return empty_cell_list

    def set_random_cell(self, icon):
        cell = random.choice(self.get_empty_cells())
        return cell
