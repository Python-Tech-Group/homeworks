
class Menu(object):

    def __init__(self):
        print ("Welcome to Tic Tac Toe game")
        print("=========================================================")
        print("This plays needs two player. Let's go to start!!")


    def introduce_player_name(self, player_id):
        try:
            name = input("%s: Introduce your name: " % player_id)
            if(len(name)<=0):
                print("Your input should be not empty. Please, try again.")
                self.introduce_player_name(player_id)

        except (ValueError, TypeError):
            print("ValueError or TypeError occurred")
        return name

    def introduce_player_position(self, player_id):
        try:
            position = 0
            position = int(input("%s: Introduce your selected Cell position number(1 to 9): " % player_id))
        except ValueError:
            print("You should fill out numbers between 1 to 9")
            print("Please, try again.")
            self.introduce_player_position(player_id)

        if position < 0:
            print("You should fill out a positive number")
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
        print("%s: %s is the winner!! Congratulations!!" % (player_id, name))
