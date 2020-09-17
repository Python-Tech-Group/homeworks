

class Player(object):

    def __init__(self, name, player_id, icon, is_human):
        self.name_player = name
        self.player_id = player_id
        self.icon = icon
        self.is_human = is_human
        self.set_turns()

    def print_player_data(self):
        print("%s , Name: %s ;  Icon: %s" %
              (self.player_id, self.name_player,  self.icon))

    def set_turns(self):
        if self.player_id == 1:
            self.turns_list = [1, 3, 5, 7, 9]
        else:
            self.turns_list = [2, 4, 6, 8]

