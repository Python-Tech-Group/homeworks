import unittest
from src.menu import Menu
from src.player import Player
from src.board import Board

class Test(unittest.TestCase):

    def test_game_row1(self):
        board = Board()
        # Initial Players
        player1 = Player("Sara", "Player1", "x")
        board_position_row = {1: "x", 2: "x", 3: "x", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
        board.board_position = board_position_row

        self.assertEqual(board.verify_win_cases(),"x")

    def test_game_row2(self):
        board = Board()
        # Initial Players
        player1 = Player("Sara", "Player1", "x")
        board_position_row = {1: " ", 2: " ", 3: " ", 4: "x", 5: "x", 6: "x", 7: " ", 8: " ", 9: " "}
        board.board_position = board_position_row

        self.assertEqual(board.verify_win_cases(),"x")

    def test_game_row3(self):
        board = Board()
        # Initial Players
        player1 = Player("Sara", "Player1", "x")
        board_position_row = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: "x", 8: "x", 9: "x"}
        board.board_position = board_position_row

        self.assertEqual(board.verify_win_cases(),"x")

    def test_game_column1(self):
        board = Board()
        # Initial Players
        player1 = Player("Sara", "Player1", "x")
        board_position_row = {1: "x", 2: " ", 3: " ", 4: "x", 5: " ", 6: " ", 7: "x", 8: " ", 9: " "}
        board.board_position = board_position_row

        self.assertEqual(board.verify_win_cases(),"x")

    def test_game_column2(self):
        board = Board()
        # Initial Players
        player1 = Player("Sara", "Player1", "x")
        board_position_row = {1: " ", 2: "x", 3: " ", 4: " ", 5: "x", 6: " ", 7: " ", 8: "x", 9: " "}
        board.board_position = board_position_row

        self.assertEqual(board.verify_win_cases(),"x")

    def test_game_column3(self):
        board = Board()
        # Initial Players
        player1 = Player("Sara", "Player1", "x")
        board_position_row = {1: " ", 2: " ", 3: "x", 4: " ", 5: " ", 6: "x", 7: " ", 8: " ", 9: "x"}
        board.board_position = board_position_row

        self.assertEqual(board.verify_win_cases(),"x")

    def test_game_diagonal1(self):
        board = Board()
        # Initial Players
        player1 = Player("Sara", "Player1", "x")
        board_position_row = {1: "x", 2: " ", 3: " ", 4: " ", 5: "x", 6: " ", 7: " ", 8: " ", 9: "x"}
        board.board_position = board_position_row

        self.assertEqual(board.verify_win_cases(),"x")

    def test_game_diagonal2(self):
        board = Board()
        # Initial Players
        player1 = Player("Sara", "Player1", "x")
        board_position_row = {1: " ", 2: " ", 3: "x", 4: " ", 5: "x", 6: " ", 7: "x", 8: " ", 9: " "}
        board.board_position = board_position_row

        self.assertEqual(board.verify_win_cases(), "x")

    def test_game_none_player(self):
        board = Board()
        # Initial Players
        player1 = Player("Sara", "Player1", "x")
        player1 = Player("Michel", "Player2", "o")
        board_position_row = {1: "x", 2: "o", 3: "x", 4: "o", 5: "x", 6: "o", 7: "o", 8: "x", 9: "o"}
        board.board_position = board_position_row

        self.assertEqual(board.verify_win_cases(), " ")

    def test_game_none_player_win(self):
        board = Board()

        board_position_row = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}
        board.board_position = board_position_row

        self.assertEqual(board.verify_win_cases(), " ")

#unittest.main()
if __name__ == "__main__":
    unittest.main()