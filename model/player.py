import random

class Player:

    def __init__(self, symbol, player_type):
        self.symbol = symbol
        self.player_type = player_type

    def chose_tile(self, board):
        """Let 'AI' choose a random tile to make a move"""
        index = random.randint(0, len(board.empty_tiles) - 1)
        x, y = board.empty_tiles[index]
        selected_tile = board.get_tile_at_pos(x, y)
        return selected_tile
    
    def make_move(self, tile, view):
        """Make a move"""
        tile.state = self.symbol

        if self.symbol == 'X':
            view.draw_x(tile)
        elif self.symbol == 'O':
            view.draw_o(tile)
