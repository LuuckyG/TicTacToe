class Player:

    def __init__(self, name, player):
        self.name = name
        self.player = player


class HumanPlayer(Player):
    def __init__(self, name, player='human'):
        super().__init__(name, player)
    
    def make_move(self, x, y):
        pass


class ComputerPlayer(Player):
    def __init__(self, name, player='AI'):
        super().__init__(name, player)
    
    def make_move(self, x, y):
        pass
