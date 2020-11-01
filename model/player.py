import random

class Player:

    def __init__(self, symbol, player_type):
        self.symbol = symbol
        self.player_type = player_type

    def make_random_move(self, board):
        """Let 'AI' make random move"""
        index = random.randint(0, len(board.empty_tiles) - 1)
        x, y = board.empty_tiles[index]
        selected_tile = board.get_tile_at_pos(x, y)
        return selected_tile
    
    def make_good_move(self, board, depth):
        """Let 'AI' make good move"""
        pass