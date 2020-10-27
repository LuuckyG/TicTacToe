class Tile:
    """Class to create the seperate tiles of the tictactoe board."""

    def __init__(self, x, y, state='empty'):
        """Initialization of the tile.
        
            Args:
            - x: the horizontal coordinate of the tile
            - y: the vertical coordinate of the tile
            - state: the state of the tile. This is either 'empty' (default), 'X' or 'O'
        """
        self.x = x
        self.y = y
        self.state = state

    def change_state(self, symbol):
        """A player makes a move and now an empty tile becomes a filled tile,
        based on the symbol of the player.
        
            Args:
            - symbol: the symbol of the player (human or AI) that makes the move,
                can be either 'X' or 'O'.
        """
        self.state = symbol
