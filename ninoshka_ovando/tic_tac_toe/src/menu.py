
class Menu(object):

    def __init__(self):
        print("Welcome to Tic Tac Toe game")
        print("=========================================================")
        print("This plays needs one or two players. Let's go to start!!")

    def select_number_players(self):
        number_players = 0
        try:
            number_players = int(input("Introduce your number players(1 or 2): "))
        except ValueError:
            print("You should fill numbers(1 or 2)")
            print("Please, try again.")
            self.select_number_players()

        if number_players <= 0 or number_players > 2:
            print("You should fill numbers(1 or 2)")
            print("Please, try again.")
            self.select_number_players()

        return number_players

    def introduce_player_name(self, player_id):
        name = ""
        try:
            name = input("%s: Introduce your name: " % player_id)
            if len(name) <=0:
                print("Your input should be not empty. Please, try again.")
                self.introduce_player_name(player_id)

        except (ValueError, TypeError):
            print("ValueError or TypeError occurred")
        return name

    def introduce_player_position(self, player_id, icon):
        position = 0
        try:
            position = int(input("%d: Introduce your Cell \"%s\" in a position number(1 to 9): " % (player_id, icon)))
        except ValueError:
            print("You should fill out numbers between 1 to 9")
            print("Please, try again.")
            self.introduce_player_position(player_id)

        if 0 >= position >= 10:
            print("You should fill out a positive number between 1 to 9")
            print("Please, try again.")
            self.introduce_player_position(player_id)

        return position

    def example_board_cells(self):
        print("Please, see the next board with each position that you will input in your turn:")
        print(" 1 | 2 | 3 ")
        print("---+---+---")
        print(" 4 | 5 | 6 ")
        print("---+---+---")
        print(" 7 | 8 | 9 ")

    def draw_board(self, board_position):
        print("Current Board Game:")
        print(" %s | %s | %s " % (board_position[1], board_position[2], board_position[3]))
        print("---+---+---")
        print(" %s | %s | %s " % (board_position[4], board_position[5], board_position[6]))
        print("---+---+--- ")
        print(" %s | %s | %s " % (board_position[7], board_position[8], board_position[9]))
        print("\n")

    def is_end_game(self):
        print("Tic Tac Toe has completed")
        option = input("Do you want to play again? Yes or No  -->")
        if option.lower() == "yes":
            return False
        elif option.lower() == "no":
            print("Thank you! bye!!")
            return True
        else:
            print("You need to answer: \'Yes\' or \'No\'")
            self.is_end_game()

    def print_winner_name(self, name, player_id):
        print("%d: %s is the winner!! Congratulations!!" % (player_id, name))

    def print_select_other_cell(self):
        print("Please, select other cell empty")

    def print_select_Machine_cell(self, cell):
        print("Machine has selected: %s" % cell)

    def print_none_has_won(self):
        print("Nobody has won. Thank you for playing Tic Tac Toe.")

