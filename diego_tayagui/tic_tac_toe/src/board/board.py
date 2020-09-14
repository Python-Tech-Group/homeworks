import pygame as pg


class Board(object):

    def __init__(self):
        self.draw = None
        self.width = 400
        self.height = 400
        self.white = (255, 255, 255)
        self.line_color = (0, 0, 0)
        self.array_board = [[None] * 3, [None] * 3, [None] * 3]

    def draw_blank_board(self, screen):
        self.draw = False
        self.array_board = [[None] * 3, [None] * 3, [None] * 3]
        screen.fill(self.white)
        # drawing vertical lines
        pg.draw.line(screen, self.line_color, (int(self.width / 3), 0),
                     (int(self.width / 3), self.height), 7)
        pg.draw.line(screen, self.line_color, (int(self.width / 3 * 2), 0),
                     (int(self.width / 3 * 2), self.height), 7)
        # drawing horizontal lines
        pg.draw.line(screen, self.line_color, (0, int(self.height / 3)),
                     (self.width, int(self.height / 3)), 7)
        pg.draw.line(screen, self.line_color, (0, int(self.height / 3 * 2)),
                     (self.width, int(self.height / 3 * 2)), 7)

    def get_col_row(self, x, y):
        col, row = None, None
        if x < self.width / 3:
            col = 1
        elif x < self.width / 3 * 2:
            col = 2
        elif x < self.width:
            col = 3
        if y < self.height / 3:
            row = 1
        elif y < self.height / 3 * 2:
            row = 2
        elif y < self.height:
            row = 3
        if self.array_board[row - 1][col - 1] is None:
            return col, row
        else:
            return None, None

    def set_col_row_value(self, row, col, value):
        self.array_board[row][col] = value

    def check(self, screen):
        winner = None
        # checking for winning rows
        for row in range(0, 3):
            if (self.array_board[row][0] == self.array_board[row][1] == self.array_board[row][2])\
                    and (self.array_board[row][0] is not None):
                winner = self.array_board[row][0]
                delta = int((row + 1) * self.height / 3 - self.height / 6)
                pg.draw.line(screen, self.line_color, (0, delta), (self.width, delta), 10)
                break
        # checking for winning columns
        for col in range(0, 3):
            if (self.array_board[0][col] == self.array_board[1][col] == self.array_board[2][col])\
                    and (self.array_board[0][col] is not None):
                winner = self.array_board[0][col]
                delta = int((col + 1) * self.width / 3 - self.width / 6)
                pg.draw.line(screen, self.line_color, (delta, 0), (delta, self.height), 10)
                break
        # check for diagonal winners
        if (self.array_board[0][0] == self.array_board[1][1] == self.array_board[2][2])\
                and (self.array_board[0][0] is not None):
            # game won diagonally left to right
            winner = self.array_board[0][0]
            pg.draw.line(screen, self.line_color, (50, 50), (350, 350), 10)
        if (self.array_board[0][2] == self.array_board[1][1] == self.array_board[2][0])\
                and (self.array_board[0][2] is not None):
            # game won diagonally right to left
            winner = self.array_board[0][2]
            pg.draw.line(screen, self.line_color, (350, 50), (50, 350), 10)
        if all([all(row) for row in self.array_board]) and winner is None:
            self.draw = True

        return winner

