import pygame as pg
import time
import sys
from pygame.locals import *
from src.board import Board


class Game(object):
    def __init__(self):
        self.XO = 'x'
        self.winner = None
        self.board = Board()
        self.screen = pg.display.set_mode((self.board.width, self.board.height))
        x_resource = pg.image.load("resources/x.png")
        y_resource = pg.image.load("resources/o.png")
        self.x_img = pg.transform.scale(x_resource, (80, 80))
        self.y_img = pg.transform.scale(y_resource, (80, 80))

    def drawXO(self, row, col):
        pos_x, pos_y = None, None
        if row == 1:
            pos_x = 30
        if row == 2:
            pos_x = self.board.width / 3 + 30
        if row == 3:
            pos_x = self.board.width / 3 * 2 + 30
        if col == 1:
            pos_y = 30
        if col == 2:
            pos_y = self.board.height / 3 + 30
        if col == 3:
            pos_y = self.board.height / 3 * 2 + 30
        self.board.set_col_row_value(row - 1, col - 1, self.XO)
        if self.XO == 'x':
            self.screen.blit(self.x_img, (int(pos_y), int(pos_x)))
            self.XO = 'o'
        else:
            self.screen.blit(self.y_img, (int(pos_y), int(pos_x)))
            self.XO = 'x'
        pg.display.update()

    def click(self):
        x, y = pg.mouse.get_pos()
        col, row = self.board.get_col_row(x, y)
        if row and col:
            self.drawXO(row, col)
            self.winner = self.board.check(self.screen)

    def reset_game(self):
        time.sleep(3)
        self.XO = 'x'
        self.board.draw_blank_board(self.screen)
        self.winner = None

    def start(self):
        pg.init()
        pg.display.set_caption("Diego Tayagüi - Tic Tac Toe")
        self.board.draw_blank_board(self.screen)

        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type is MOUSEBUTTONDOWN:
                    self.click()
                    if self.winner or self.board.draw:
                        self.reset_game()
            pg.display.update()
