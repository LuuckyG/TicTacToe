import pygame, os

from model.button import Button

class GameView:
    """Class to make game view / GUI with pygame"""
    
    WHITE = (255, 255, 255)
    YELLOW = (255, 233, 33)
    ORANGE = (255,237,194)
    RED = (255, 82, 82)
    BLUE = (69, 125, 255)
    BLACK = (0, 0, 0)
    LIGHT_GRAY = (225, 225, 225)
    GREEN = (71, 255, 78)

    def __init__(self, screen_size=540, border=20, line_width=5):
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

        self.border = border
        self.line_width = line_width
        self.all_buttons = []

        # Create screen
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size + 100))
        
        self.font = pygame.font.SysFont(None, 30)
        self.big_font = pygame.font.SysFont(None, 40)
        self.small_font = pygame.font.SysFont(None, 20)
        pygame.display.set_caption('TicTacToe')

        # Display starting screen
        self.is_new_game()


    def draw_screens(self, status):
        """Method to control what screen is draw when tracking mouse movement.
        Default mode is drawing the starting screen."""

        if status == 'start_screen':
            self.draw_start_screen()
        elif status == 'settings':
            self.draw_settings_screen()
        elif status == 'replay':
            self.draw_play_again_screen()
        elif status == 'end_game':
            self.draw_thanks()


    def follow_mouse(self, x, y):
        """Track mouse movement and if hovered over a button, change the color
        of the button to indicate focus."""
        for button in self.all_buttons:
            if button.is_hover(x, y):
                button.color = self.YELLOW
            else:
                if button.selected:
                    button.color = self.GREEN
                else:
                    button.color = self.LIGHT_GRAY


    def is_new_game(self):
        """Draw the starting screen, showing the game options"""       
        file_name = "view/media/start_screen.png"
        self.start_screen_image = pygame.image.load(file_name)
        self.start_screen_image = pygame.transform.scale(self.start_screen_image, (self.screen_size, self.screen_size))
        
        self.create_buttons()
        self.draw_start_screen()


    def draw_start_screen(self):
        """Start screen"""
        self.screen.fill(self.WHITE)
        self.screen.blit(self.start_screen_image, (0, 0))

        self.settings_button.draw(self.screen, self.small_font, thickness=1)
        self.start_game_button.draw(self.screen, self.big_font)
        self.quit_game_button.draw(self.screen, self.small_font, thickness=1)

   
    def draw_settings_screen(self):
        """Settings screen"""
        self.screen.fill(self.LIGHT_GRAY)

        # Title
        title_text = self.big_font.render('Settings', True, self.BLACK, self.LIGHT_GRAY)
        title_text_box = title_text.get_rect()
        title_text_box.center = (self.screen_size / 2, 0.3 * self.screen_size)
        
        # Show settings
        # Human vs. Human or Human vs. AI
        game_type_text = self.font.render('Game Type', True, self.BLACK, self.LIGHT_GRAY)
        game_type_text_box = game_type_text.get_rect()
        game_type_text_box.center = (0.2 * self.screen_size, 0.5 * self.screen_size)

        self.human_vs_human_button.draw(self.screen, self.small_font)
        self.human_vs_ai_button.draw(self.screen, self.small_font)

        # AI level
        ai_level_text = self.font.render('AI level', True, self.BLACK, self.LIGHT_GRAY)
        ai_level_text_box = ai_level_text.get_rect()
        ai_level_text_box.center = (0.17 * self.screen_size, 0.6 * self.screen_size)

        self.ai_level_1_button.draw(self.screen, self.small_font)
        self.ai_level_2_button.draw(self.screen, self.small_font)
        self.ai_level_3_button.draw(self.screen, self.small_font)

        # Board size
        board_size_text = self.font.render('Board Size', True, self.BLACK, self.LIGHT_GRAY)
        board_size_text_box = board_size_text.get_rect()
        board_size_text_box.center = (0.2 * self.screen_size, 0.7 * self.screen_size)

        self.board_size_3_button.draw(self.screen, self.small_font)
        self.board_size_5_button.draw(self.screen, self.small_font)
        self.board_size_7_button.draw(self.screen, self.small_font)

        # Go back button
        self.back_button.draw(self.screen, self.small_font)

        # Blit everything to screen
        self.screen.blit(title_text, title_text_box)
        self.screen.blit(game_type_text, game_type_text_box)
        self.screen.blit(ai_level_text, ai_level_text_box)
        self.screen.blit(board_size_text, board_size_text_box)


    def draw_play_again_screen(self):
        """Show message if player wants to play another game"""
        border = 2
        self.screen.fill(self.BLACK, (0.20 * self.screen_size - border, 0.40 * self.screen_size - border, 
                                       0.60 * self.screen_size + 2 * border, 0.20 * self.screen_size + 2 * border))
        self.screen.fill(self.ORANGE, (0.20 * self.screen_size, 0.40 * self.screen_size, 
                                       0.60 * self.screen_size, 0.20 * self.screen_size))

        text = self.big_font.render('Play Again?', True, self.BLACK, self.ORANGE)
        text_box = text.get_rect()
        text_box.center = (0.5 * self.screen_size, 0.45 * self.screen_size)
        self.screen.blit(text, text_box)

        self.play_again_button.draw(self.screen, self.font)
        self.nomore_game_button.draw(self.screen, self.font)
        return True


    def draw_thanks(self):
        """Show 'thank you' message before closing application."""
        self.screen.fill(self.WHITE)
        self.screen.blit(self.start_screen_image, (0, 0))
        self.show_message('Thanks for Playing!', self.big_font, text_color=self.BLACK, background=self.WHITE)
        pygame.time.delay(500)


    def draw_board(self, board):
        """Draw the game board.
        To draw the grid, we have to draw (n-1)^2 lines, 
        where n^2 is the total number of tiles (normally 9, so n = 3).
        """

        # Get grid sizes
        self.board_size = board.board_size
        self.tile_size = board.tile_size

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


    def draw_x(self, tile):
        """Draw 'X' symbol on tile. To draw the X, we draw two seperate lines"""
        offset = tile.size * 0.2

        # Line from top left to bottom right
        pygame.draw.line(self.screen, self.RED, (tile.x + offset, tile.y + offset), 
                                                (tile.x + tile.size - offset, tile.y + tile.size - offset), 2 * self.line_width)
        
        # Line from bottom left to top right
        pygame.draw.line(self.screen, self.RED, (tile.x + offset, tile.y + tile.size - offset), 
                                                (tile.x + tile.size - offset, tile.y + offset), 2 * self.line_width)


    def draw_o(self, tile):
        """Draw 'O' symbol on tile"""
        pygame.draw.circle(self.screen, self.BLUE, tile.rect.center, tile.radius, 2 * self.line_width)


    def show_message(self, message, font, text_color=(255, 255, 255), background=(0, 0, 0)):
        """Show message with info to the user at the bottom of the window, below the play board"""
        # Create box at the bottom of the display
        self.screen.fill(background, (0, self.screen_size, self.screen_size, 100))
        
        text = font.render(message, True, text_color, background)
        text_box = text.get_rect()
        text_box.center = (self.screen_size / 2, self.screen_size + 50)

        # Show message
        self.screen.blit(text, text_box)
        pygame.display.update()


    def draw_win(self, winner, winning_tiles):
        """Indicate who has won the game"""
        first_tile = winning_tiles[0]
        last_tile = winning_tiles[-1]
        pygame.draw.line(self.screen, self.GREEN, first_tile.rect.center, last_tile.rect.center, 2 * self.line_width)

        message = f"{winner} Wins!"
        self.show_message(message, self.font)
        pygame.time.delay(500)


    def show_turn(self, player, num_empty_tiles):
        """Show who's turn it is and how many empty tiles are left"""
        message = f"{player}'s Turn. {num_empty_tiles} Empty Tiles Left"
        self.show_message(message, self.font)


    def update_button_look(self, button, status, color, text_color):
        """Method to change look of buttons, based on the fact if they are
        selected or not."""
        
        button.selected = status
        button.color = color
        button.text_color = text_color


    def create_buttons(self):
        """Function to create the buttons needed to navigate throught the game"""

        #### Start Screen ####
        self.settings_button = Button(color=self.LIGHT_GRAY, 
                                      x=0.05 * self.screen_size, 
                                      y=self.screen_size + 30, 
                                      width=0.2 * self.screen_size, 
                                      height=40, 
                                      value='settings', 
                                      group='start_screen', 
                                      selected=False, 
                                      text_color=self.BLACK, 
                                      text='Settings')

        self.start_game_button = Button(color=self.GREEN, 
                                        x=0.30 * self.screen_size, 
                                        y=self.screen_size + 15, 
                                        width=0.4 * self.screen_size, 
                                        height=70, 
                                        value='start', 
                                        group='start_screen', 
                                        selected=True, 
                                        text_color=self.WHITE, 
                                        text='PLAY!')

        self.quit_game_button = Button(color=self.LIGHT_GRAY, 
                                       x=0.75 * self.screen_size, 
                                       y=self.screen_size + 30, 
                                       width=0.2 * self.screen_size, 
                                       height=40, 
                                       value='quit',
                                       group='start_screen', 
                                       selected=False, 
                                       text_color=self.BLACK, 
                                       text='Quit')

        # ---------------------------------------------------------------------------------- #
        #### Settings Screen ####

        # Create two buttons, one voor human vs. human and one for human vs. AI
        self.human_vs_human_button = Button(color=self.GREEN, 
                                            x=0.5 * self.screen_size, 
                                            y=0.5 * self.screen_size - 15, 
                                            width=0.2 * self.screen_size, 
                                            height=30, 
                                            value=False,
                                            group='vs_computer', 
                                            selected=True, 
                                            text_color=self.WHITE, 
                                            text='Human vs. Human')

        self.human_vs_ai_button = Button(color=self.LIGHT_GRAY, 
                                         x=0.75 * self.screen_size, 
                                         y=0.5 * self.screen_size - 15, 
                                         width=0.2 * self.screen_size, 
                                         height=30,
                                         value=True,
                                         group='vs_computer', 
                                         selected=False, 
                                         text_color=self.BLACK, 
                                         text='Human vs. AI')
        
        # Create buttons to select the level of the AI
        self.ai_level_1_button = Button(color=self.GREEN, 
                                        x=0.5 * self.screen_size, 
                                        y=0.6 * self.screen_size - 15, 
                                        width=0.1 * self.screen_size, 
                                        height=30, 
                                        value=1,
                                        group='ai_level', 
                                        selected=True, 
                                        text_color=self.WHITE, 
                                        text='1')

        self.ai_level_2_button = Button(color=self.LIGHT_GRAY, 
                                        x=0.65 * self.screen_size, 
                                        y=0.6 * self.screen_size - 15, 
                                        width=0.1 * self.screen_size, 
                                        height=30, 
                                        value=2,
                                        group='ai_level', 
                                        selected=False, 
                                        text_color=self.BLACK, 
                                        text='2')
                                          
        self.ai_level_3_button = Button(color=self.LIGHT_GRAY, 
                                        x=0.8 * self.screen_size, 
                                        y=0.6 * self.screen_size - 15, 
                                        width=0.1 * self.screen_size, 
                                        height=30, 
                                        value=3,
                                        group='ai_level', 
                                        selected=False, 
                                        text_color=self.BLACK, 
                                        text='3')

        # Create buttons to select the size of the play board
        self.board_size_3_button = Button(color=self.GREEN, 
                                          x=0.5 * self.screen_size, 
                                          y=0.7 * self.screen_size - 15, 
                                          width=0.1 * self.screen_size, 
                                          height=30, 
                                          value=3,
                                          group='board_size', 
                                          selected=True, 
                                          text_color=self.WHITE, 
                                          text='3 x 3')

        self.board_size_5_button = Button(color=self.LIGHT_GRAY, 
                                          x=0.65 * self.screen_size, 
                                          y=0.7 * self.screen_size - 15, 
                                          width=0.1 * self.screen_size, 
                                          height=30, 
                                          value=5,
                                          group='board_size', 
                                          selected=False, 
                                          text_color=self.BLACK, 
                                          text='5 x 5')
                                          
        self.board_size_7_button = Button(color=self.LIGHT_GRAY, 
                                          x=0.8 * self.screen_size, 
                                          y=0.7 * self.screen_size - 15, 
                                          width=0.1 * self.screen_size, 
                                          height=30, 
                                          value=7,
                                          group='board_size', 
                                          selected=False, 
                                          text_color=self.BLACK, 
                                          text='7 x 7')
        
        # Go back button
        self.back_button = Button(color=self.LIGHT_GRAY, 
                                  x=0.1 * self.screen_size, 
                                  y=self.screen_size, 
                                  width=0.1 * self.screen_size, 
                                  height=30, 
                                  value='cancel', 
                                  group='cancel', 
                                  selected=False, 
                                  text_color=self.BLACK, 
                                  text='Back')
        
        # ---------------------------------------------------------------------------------- #

        #### End Screen ####
        self.play_again_button = Button(color=self.GREEN, 
                                        x=0.25 * self.screen_size, 
                                        y=0.50 * self.screen_size + 5, 
                                        width=0.2 * self.screen_size, 
                                        height=40, 
                                        value=True,
                                        group='end_screen', 
                                        selected=True, 
                                        text_color=self.WHITE, 
                                        text='Yes!!')

        self.nomore_game_button = Button(color=self.RED, 
                                         x=0.55 * self.screen_size, 
                                         y=0.50 * self.screen_size + 5, 
                                         width=0.2 * self.screen_size, 
                                         height=40, 
                                         value=False,
                                         group='end_screen', 
                                         selected=False, 
                                         text_color=self.BLACK, 
                                         text='No')
        
        # Collect all buttons
        self.all_buttons.extend((self.settings_button, self.start_game_button, self.quit_game_button,
                                 self.human_vs_human_button, self.human_vs_ai_button, 
                                 self.ai_level_1_button, self.ai_level_2_button, self.ai_level_3_button,
                                 self.board_size_3_button, self.board_size_5_button, self.board_size_7_button,
                                 self.back_button,
                                 self.play_again_button, self.nomore_game_button))
