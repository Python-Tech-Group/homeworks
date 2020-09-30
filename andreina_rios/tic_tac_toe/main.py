
board = ["*", "*", "*",
         "*", "*", "*",
         "*", "*", "*"]

game = True

winner = None

player_one = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2]+ "     1 | 2 | 3")
    print("__" + " __ " + " __ "+ "     __ __ __")
    print(board[3] + " | " + board[4] + " | " + board[5]+ "     4 | 5 | 6")
    print("__" + " __ " + " __ "+ "     __ __ __")
    print(board[6] + " | " + board[7] + " | " + board[8]+ "     7 | 8 | 9")


def play_game():
    display_board()

    while game:
        player_turn(player_one)

        review_gameover()

        change_player()

    if winner == "X" or winner == "O":
        print("Player "+ winner + " won the game.")

    elif winner == None:
        print("It's a tie. Nobody has won.")


def player_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Please choose a position from 1-9 once again: ")

    position = int(position) - 1

    if board[position] == "*":
        valid = True
    else:
        print("This position had already been selected. Please choose another one: ")

    board[position] = player

    display_board()


def review_gameover():
    review_winner()
    review_tie()


def review_winner():
    global winner
    r_winner = r_rows()
    c_winner = r_columns()
    d_winner = r_diagonals()

    if r_winner:
        winner = r_winner
    elif c_winner:
        winner = c_winner
    elif d_winner:
        winner = d_winner
    else:
        winner = None
    return


def r_rows():
    global game
    row_1 = board[0] == board[1] == board[2] != "*"
    row_2 = board[3] == board[4] == board[5] != "*"
    row_3 = board[6] == board[7] == board[8] != "*"
    if row_1 or row_2 or row_3:
        game = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def r_columns():
    global game
    col_1 = board[0] == board[3] == board[6] != "*"
    col_2 = board[1] == board[4] == board[7] != "*"
    col_3 = board[2] == board[5] == board[8] != "*"
    if col_1 or col_2 or col_3:
        game = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def r_diagonals():
    global game
    diagonal_1 = board[0] == board[4] == board[8] != "*"
    diagonal_2 = board[2] == board[4] == board[6] != "*"
    if diagonal_1 or diagonal_2:
        game = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None


def review_tie():
    global game
    if "*" not in board:
        game = False
    return


def change_player():
    global player_one
    if player_one == "X":
        player_one = "O"
    elif player_one == "O":
        player_one = "X"
    return

print("Welcome to TIC TAC TOE game: ")
play_game()