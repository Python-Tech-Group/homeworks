
class Board:
    def __init__(self):
        self.__board = [i for i in range(0, 9)]
        self.table = range(1, 10)
        self.winnersCombinations = (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6))
        self.moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))

    def print_board(self):
        x = 1
        for i in self.__board:
            end = ' | '
            if x % 3 == 0:
                end = ' \n'
                if i != 1:
                    end += '---------\n'
            char = ' '
            if i in ('X', 'O'):
                char = i
            x += 1
            print(char, end=end)

    def space_exist(self):
        return self.__board.count('X') + self.__board.count('O') != 9

    def make_move(self, player, move, undo=False):
        if self.can_move(player, move):
            self.__board[move - 1] = player
            win = self.can_win(player, move)
            if undo:
                self.__board[move - 1] = move - 1
            return (True, win)
        return (False, False)

    def can_move(self, player, move):
        if move in self.table and self.__board[move - 1] == move - 1:
            return True
        return False

    def can_win(self, player, move):
        places = []
        x = 0
        for i in self.__board:
            if i == player:
                places.append(x)
            x += 1
        win = True
        for tup in self.winnersCombinations:
            win = True
            for ix in tup:
                if self.__board[ix] != player:
                    win = False
                    break
            if win == True:
                break
        return win