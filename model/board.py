from model.tile import Tile

class Board:
    """Board class. Captures all `Tile` tiles in the board attribure"""

    def __init__(self, screen_size=540, board_size=3):
        """Set up of empty board of size `board_size ^ 2` (default = 3 ^ 2). 
        Each tile on the board has a width in px (default = 180px) of `tile_size`.
        
        Args:
        - screen_size: the width of the game window (in px), default = 540px.
        - board_size: the number of tiles on a row, column or diagonal of the board (default = 3).
        """

        self.screen_size = screen_size
        self.board_size = board_size
        self.tile_size = screen_size // board_size
        self.reset()

    def reset(self):
        """Create empty board, consisting of `board_size` * `board_size` tiles"""

        self.board = []
        self.empty_tiles = []

        for i in range(self.board_size):
            board_row = []
            for j in range(self.board_size):
                tile = Tile(i * self.tile_size, j * self.tile_size, self.tile_size, 'empty')
                board_row.append(tile)
                self.empty_tiles.append((i * self.tile_size, j * self.tile_size))
            self.board.append(board_row)
        
    def get_tile_at_pos(self, x, y):
        """"Get the empty tile at the mouse click location.
        
        Args:
        - x: x-coordinate of mouse at click
        - y: y-coordinate of mouse at click
        """
        for rows in self.board:
            for tile in rows:
                if tile.rect.collidepoint(x, y) and tile.state == 'empty':
                    index = self.empty_tiles.index((tile.x, tile.y))
                    self.empty_tiles.pop(index)
                    return tile
        return None
