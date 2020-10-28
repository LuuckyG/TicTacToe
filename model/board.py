from model.tile import Tile

class Board:
    """Board class. Captures all `Tile` tiles in the board attribure"""

    def __init__(self, tile_size=180, board_size=3):
        """Set up of empty board of size `board_size ^ 2` (default = 3 ^ 2). 
        Each tile on the board has a width in px (default = 180px) of `tile_size`."""

        self.board = []
        self.empty_tiles = []
        self.tile_size = tile_size
        self.board_size = board_size

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
                self.empty_tiles.append((i, j))

            self.board.append(board_row)
        
    def get_tile_at_pos(self, x, y):
        for tile in self.board:
            if tile.rect.collidepoint(x, y) and tile.state == 'empty':
                index = self.empty_tiles.index((x, y))
                self.empty_tiles.pop(index)
                return tile
        return None
