class Player:

    def __init__(self, name, player_nr, player):
        self.name = name
        self.player_nr = player_nr
        self.player = player
    
    def set_symbol(self, player_nr):
        self.symbol = 'X' if player_nr == 0 else 'O'


class HumanPlayer(Player):
    def __init__(self, name, player_nr, player='human'):
        super().__init__(name, player_nr, player)
    
    def make_move(self, x, y):
        pass


class ComputerPlayer(Player):
    def __init__(self, name, player_nr, player='AI'):
        super().__init__(name, player_nr, player)
    
    def make_move(self, x, y):
        pass
