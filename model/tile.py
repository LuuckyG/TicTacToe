import pygame

class Tile:
    """Class to create the seperate tiles of the tictactoe board."""

    def __init__(self, x, y, size, state='empty'):
        """Initialization of the tile.
        
            Args:
            - x: the horizontal coordinate (in px) of the tile (top left)
            - y: the vertical coordinate (in px) of the tile (top left)
            - size: size of the tile (in px)
            - state: the state of the tile. This is either 'empty' (default), 'X' or 'O'
        """
        self.x = x
        self.y = y
        self.size = size
        self.state = state
        self.rect = pygame.Rect(x, y, size, size)
        
        # Create little space (16,67%) for the circle radius
        self.radius = (self.size // 2) - (self.size // 6)

    def change_state(self, symbol):
        """A player makes a move and now an empty tile becomes a filled tile,
        based on the symbol of the player.
        
            Args:
            - symbol: the symbol of the player (human or AI) that makes the move,
                can be either 'X' or 'O'.
        """
        self.state = symbol
