import pygame

class GameView:
    """Class to make game view / GUI with pygame"""
    
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)

    def __init__(self, tile_size, board, border=20, line_width=5):
        """Set up of start screen
           
            Args:
            - tile_size:
            - board:
            - border:
            - line_width:
        """    
        
        # Initialise pygame
        pygame.init()

        # Get grid sizes
        self.board_size = board.board_size
        self.tile_size = tile_size
        self.border = border
        self.line_width = line_width

        # Create screen
        self.offset = (self.border * 2) + (self.line_width * (self.board_size - 1))
        self.surface_size = (self.board_size * self.tile_size) + self.offset
        self.screen = pygame.display.set_mode((self.surface_size, self.surface_size))
        self.font = pygame.font.SysFont('courier', 40)
        pygame.display.set_caption('TicTacToe')
        
        # Fill background
        self.screen.fill(self.WHITE)
        
        # Draw lines of tiles
        self.draw_board()

        pygame.display.update()

    def draw_board(self):
        """To draw the grid, we have to draw (n-1)^2 lines, 
        where n^2 is the total number of tiles (normally 9, so n = 3)"""
        
        half_offset = self.offset / 2

        for i in range(1, self.board_size):
            # Vertical line
            pygame.draw.line(self.screen, self.BLACK, (i * self.tile_size + half_offset, 0 + half_offset), 
                (i * self.tile_size + half_offset, self.board_size * self.tile_size + half_offset), self.line_width)
            
            # Horizontal line
            pygame.draw.line(self.screen, self.BLACK, (0 + half_offset, i * self.tile_size + half_offset), 
                (self.board_size * self.tile_size + half_offset, i * self.tile_size + half_offset), self.line_width)


    def draw_x(self, x, y):
        pass

    def draw_o(self, x, y):
        pygame.draw.circle(self.background, self.BLUE)

    def get_tile_at_click_pos(self):
        pass

    def get_mouse_click(self):
        pass

    def show_move(self):
        pass

    def show_end_screen(self):
        pass
