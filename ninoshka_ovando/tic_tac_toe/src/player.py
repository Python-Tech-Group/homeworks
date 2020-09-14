

class Player(object):
    name_player = ""
    player_id = ""
    icon = ""
    def __init__(self, name, id, icon):
        self.name_player = name
        self.player_id = id
        self.icon = icon

    def get_name_player(self):
        return self.name_player

    def print_player_data(self):
        print("%s , Name: %s ;  Icon: %s" %
              (self.player_id, self.name_player,  self.icon))