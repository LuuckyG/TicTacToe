from model.tile import Tile

class Board:
    """Board class. Captures all `Tile` tiles in the board attribure"""

    def __init__(self, screen_size=540, board_size=3):
        """Set up of empty board of size `board_size ^ 2` (default = 3 ^ 2). 
        Each tile on the board has a width in px (default = 180px) of `tile_size`."""

        self.board = []
        self.empty_tiles = []
        self.screen_size = screen_size
        self.board_size = board_size
        self.tile_size = screen_size // board_size
        self.reset()

    def empty_board(self):
        """Reset the board to an empty board"""
        self.board = []
        self.empty_tiles = []

    def reset(self):
        """Create empty board, consisting of `board_size` * `board_size` tiles"""
        self.empty_board()

        for i in range(self.board_size):
            board_row = []
            for j in range(self.board_size):
                tile = Tile(i * self.tile_size, j * self.tile_size, self.tile_size, 'empty')
                board_row.append(tile)
                self.empty_tiles.append((i * self.tile_size, j * self.tile_size))
            self.board.append(board_row)
        
    def get_tile_at_pos(self, x, y):
        for rows in self.board:
            for tile in rows:
                if tile.rect.collidepoint(x, y) and tile.state == 'empty':
                    index = self.empty_tiles.index((tile.x, tile.y))
                    self.empty_tiles.pop(index)
                    return tile
        return None
