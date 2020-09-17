from src.menu import Menu
from src.player import Player
from src.board import Board


class Game(object):

    def __init__(self):
        self.menu = Menu()
        self.board = Board()
        self.players = []
        self.number_players = 0
        self.is_there_a_winner = False

    def previous_before_playing(self):
        # Initial Players
        self.number_players = self.menu.select_number_players()
        self.game_player_information()
        # Initial board
        self.menu.example_board_cells()
        self.menu.draw_board(self.board.board_position)

    def game_player_information(self):
        if self.number_players == 2:
            self.players.append(Player(self.menu.introduce_player_name("1"), 1, "x", True))
            self.players.append(Player(self.menu.introduce_player_name("2"), 2, "o", True))
        else:
            self.players.append(Player(self.menu.introduce_player_name("1"), 1, "x", True))
            self.players.append(Player("Machine", 2, "o", False))

    def start_play(self):
        # Start Playing
        continue_game = True
        while continue_game:
            continue_game = self.playing_a_player(self.board.marked_cells + 1)
            self.menu.draw_board(self.board.board_position)

            if self.board.marked_cells == 9 or not continue_game:
                if not self.is_there_a_winner:
                    self.menu.print_none_has_won()
                if not self.menu.is_end_game():
                    self.restart_game()
                else:
                    break

    def restart_game(self):
        self.menu = Menu()
        self.board = Board()
        self.players = []
        self.number_players = 0
        self.board.restart_board()
        self.previous_before_playing()
        self.start_play()

    def playing_a_player(self, turn_id):
        continue_playing = True
        if turn_id <= 9:
            for player in self.players:
                if turn_id in player.turns_list:
                    self.set_a_cell_free(player)
                    if self.board.verify_win_cases(player.icon):
                        self.menu.print_winner_name(player.name_player, player.player_id)
                        self.is_there_a_winner = True
                        continue_playing = False
        else:
            continue_playing = False
        return continue_playing

    def set_a_cell_free(self, player):
        if player.is_human:
            selected_cell = self.menu.introduce_player_position(player.player_id, player.icon)
            if self.board.board_position[selected_cell] == " ":
                self.board.board_position[selected_cell] = player.icon
                self.board.marked_cells += 1
            else:
                self.menu.print_select_other_cell()
                self.set_a_cell_free(player)
        else:
            cell = self.board.set_random_cell(player.icon)
            self.board.board_position[cell] = player.icon
            self.board.marked_cells += 1
            self.menu.print_select_Machine_cell(cell)

