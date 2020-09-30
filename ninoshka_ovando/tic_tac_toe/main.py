from src.game import Game

def start_playing_tic_tac_toe():
    game = Game()
    game.previous_before_playing()
    game.start_play()


if __name__ == '__main__':
    start_playing_tic_tac_toe()