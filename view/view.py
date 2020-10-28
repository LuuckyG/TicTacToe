import pygame

class GameView:
    """Class to make game view / GUI with pygame"""
    
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    LIGHT_GRAY = (225, 225, 225)
    GREEN = (0, 255, 0)

    def __init__(self, tile_size, board, border=20, line_width=5):
        """Set up of start screen
           
            Args:
            - tile_size: width of a tile (in px)
            - board: TicTacToe game board
            - border: border around game
            - line_width: Thickness of lines, for drawing the board and the symbols
        """    
        
        # Initialise pygame
        pygame.init()
        self.clock = pygame.time.Clock()

        # Get grid sizes
        self.board_size = board.board_size
        self.tile_size = tile_size
        self.border = border
        self.line_width = line_width

        # Create screen
        self.surface_size = (self.board_size * self.tile_size)
        self.screen = pygame.display.set_mode((self.surface_size, self.surface_size))
        self.screen.fill(self.WHITE)

        self.draw_board()

        # Display board
        self.font = pygame.font.SysFont('courier', 40)
        pygame.display.set_caption('TicTacToe')
        pygame.display.update()

    def draw_board(self):
        """To draw the grid, we have to draw (n-1)^2 lines, 
        where n^2 is the total number of tiles (normally 9, so n = 3)"""

        for i in range(1, self.board_size):
            # Vertical line
            pygame.draw.line(self.screen, self.BLACK, (i * self.tile_size, 0), 
                (i * self.tile_size, self.board_size * self.tile_size), self.line_width)
            
            # Horizontal line
            pygame.draw.line(self.screen, self.BLACK, (0, i * self.tile_size), 
                (self.board_size * self.tile_size, i * self.tile_size), self.line_width)

    def draw_x(self, tile):
        """To draw the X, we draw two seperate lines"""
        offset = tile.size * 0.2

        # Line from top left to bottom right
        pygame.draw.line(self.screen, self.RED, (tile.x + offset, tile.y + offset), 
                                                (tile.x + tile.size - offset, tile.y + tile.size - offset), 2 * self.line_width)
        
        # Line from bottom left to top right
        pygame.draw.line(self.screen, self.RED, (tile.x + offset, tile.y + tile.size - offset), 
                                                (tile.x + tile.size - offset, tile.y + offset), 2 * self.line_width)

    def draw_o(self, tile):
        pygame.draw.circle(self.screen, self.BLUE, tile.rect.center, tile.radius, 2 * self.line_width)

    def draw_win(self, winner, winning_tiles):
        first_tile, _, last_tile = winning_tiles
        pygame.draw.line(self.screen, self.GREEN, first_tile.center, last_tile.center, 2 * self.line_width)

    def draw_move(self, current_player, tile):     
        if current_player == 0:
            self.draw_x(tile)
        elif current_player == 1:
            self.draw_o(tile)

    def is_new_game(self):
        return False

    def draw_thanks(self):
        pass
