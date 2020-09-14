from src.menu import Menu
from src.player import Player
from src.board import Board

class Game(object):

    def __init__(self):
        self.menu = Menu()
        self.board = Board()
        self.players = []

        # Initial Players
        self.player1 = Player(self.menu.introduce_player_name("1"), "Player1", "x")
        self.players.append(self.player1)
        self.player2 = Player(self.menu.introduce_player_name("2"), "Player2", "o")
        self.players.append(self.player2)

        # Initial board
        self.menu.example_board_cells()
        self.menu.draw_board(self.board.board_position)





    def start_play(self):
        # Start Playing
        continueGame = True
        while continueGame:

            for i in range(9):
                turn = True
                while turn and continueGame:
                    if i % 2 == 0:
                        turn = not self.board.set_marker_cells(self.menu.introduce_player_position(
                            self.players[0].player_id), self.players[0].icon)
                    else:
                        turn = not self.board.set_marker_cells(self.menu.introduce_player_position(
                            self.players[1].player_id), self. players[1].icon)
                    self.menu.draw_board(self.board.board_position)
                    for player in self.players:
                        if self.board.verify_win_cases() == player.icon:
                            self.menu.print_winner_name(player.name_player, player.player_id)
                            continueGame = False

            if self.board.marked_cells == 9 or continueGame == False:
                continueGame = False
                if not self.menu.is_end_game():
                    self.restart_game()
                else:
                    break

    def restart_game(self):
        self.board.restart_board()
        self.menu.draw_board(self.board.board_position)
        self.start_play()