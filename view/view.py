import pygame, os

class GameView:
    """Class to make game view / GUI with pygame"""
    
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    LIGHT_GRAY = (225, 225, 225)
    GREEN = (0, 255, 0)

    def __init__(self, board, screen_size=540, border=20, line_width=5):
        """Set up of start screen
           
            Args:
            - tile_size: width of the screen (in px)
            - board: TicTacToe game board
            - border: border around game
            - line_width: Thickness of lines, for drawing the board and the symbols
        """    
        
        # Initialise pygame
        pygame.init()
        self.clock = pygame.time.Clock()

        # Get grid sizes
        self.board_size = board.board_size
        self.tile_size = board.tile_size
        self.border = border
        self.line_width = line_width

        # Create screen
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size + 100))

        # Load image
        file_name = "view/media/start_screen.png"
        self.start_screen = pygame.image.load(file_name)
        self.start_screen = pygame.transform.scale(self.start_screen, (self.screen_size, self.screen_size))
        
        self.font = pygame.font.SysFont(None, 30)
        pygame.display.set_caption('TicTacToe')
        pygame.display.update()

        # Display starting screen
        self.is_new_game()
    
    def is_new_game(self):
        """Draw the starting screen, showing the two game options"""
        self.screen.blit(self.start_screen, (0, 0))

        # Create two buttons, one voor human vs. human 
        # and one for human vs. AI
        #TODO!
        pygame.display.update() 

    def draw_board(self):
        """To draw the grid, we have to draw (n-1)^2 lines, 
        where n^2 is the total number of tiles (normally 9, so n = 3)"""

        self.screen.fill(self.WHITE)

        # Create box at the bottom of the display
        self.screen.fill(self.BLACK, (0, self.screen_size, self.screen_size, 100))

        for i in range(1, self.board_size):
            # Vertical line
            pygame.draw.line(self.screen, self.BLACK, (i * self.tile_size, 0), 
                (i * self.tile_size, self.board_size * self.tile_size), self.line_width)
            
            # Horizontal line
            pygame.draw.line(self.screen, self.BLACK, (0, i * self.tile_size), 
                (self.board_size * self.tile_size, i * self.tile_size), self.line_width)
        
        pygame.display.update()

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

    def draw_message(self, message):
        # Create box at the bottom of the display
        self.screen.fill(self.BLACK, (0, self.screen_size, self.screen_size, 100))
        
        text = self.font.render(message, True, self.WHITE, self.BLACK)
        text_box = text.get_rect()
        text_box.center = (self.screen_size / 2, self.screen_size + 50)

        # Show message
        self.screen.blit(text, text_box)
        pygame.display.update()

    def draw_win(self, winner, winning_tiles):
        first_tile = winning_tiles[0]
        last_tile = winning_tiles[-1]
        pygame.draw.line(self.screen, self.GREEN, first_tile.rect.center, last_tile.rect.center, 2 * self.line_width)

        message = f"{winner} Wins!"
        self.draw_message(message)
        pygame.time.delay(3000)

    def show_turn(self, player, num_empty_tiles):
        message = f"{'XO'[player]}'s Turn. {num_empty_tiles} Empty Tiles Left"
        self.draw_message(message)

       

    def draw_thanks(self):
        pass
