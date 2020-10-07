from .board import Board


class Game:
    def __init__(self):
        self.player1 = ''
        self.player2 = ''
        self.board = Board()

    def select_char(self):
        self.player1 = 'X'
        self.player2 = 'O'

    def play_game(self):
        self.select_char()
        print('Player1 is [%s] and Player2 is [%s]' % (self.player1, self.player2))
        result = '%%% Deuce ! %%%'
        while self.board.space_exist():
            self.board.print_board()
            move = self.get_move()
            moved, won = self.board.make_move(self.player1, move)
            if not moved:
                print(' >> Invalid number ! Try again !')
                continue
            if won:
                result = '*** Congratulations ! You won ! ***'
                break
            elif self.computer_move(self)[1]:
                result = '=== You lose! =='
                break
        self.board.print_board()
        print(result)

    def get_move(self):
        print('# Make your move ! [1-9] : ', end='')
        return int(input())

    def computer_move(self):
        move = -1
        self.__can_win(move)
        if move == -1:
            self.__can_win_block_player(move)
        if move == -1:
            self.__take_one_place(move)
        return self.board.make_move(self.player2, move)

    def __can_win(self, move):
        for i in range(1, 10):
            if self.board.make_move(self.player2, i, True)[1]:
                move = i
                break

    def __can_win_block_player(self, move):
        for i in range(1, 10):
            if self.board.make_move(self.player1, i, True)[1]:
                move = i
                break

    def __take_one_place(self, move):
        for tup in self.board.moves:
            for mv in tup:
                if move == -1 and self.board.can_move(self.player2, mv):
                    move = mv
                    break
