import random
import pygame

from view.view import GameView
from model.board import Board
from model.player import Player


class TicTacToe:
    """Controller class of the game TicTacToe"""

    def __init__(self):
        """Setup of game TicTacToe. All game variables, and the board and view
        are created.
        """
        self.play = True
        self.status = 'start_screen'

        self.winner = None
        self.winning_tiles = []
        self.win_combinations = []

        self.move_nr = 0
        self.player_list = []
        self.current_player = 0
        self.settings = {'vs_computer': False, 'board_size': 3}

        self.view = GameView()


    def get_current_player(self):
        return self.player_list[self.current_player]


    def process_click(self, x, y):
        """The main method of the controller.
        This method determines in which phase of the game we are and 
        what method needs to be executed based on the phase.

        Args:
        - x: x-coordinate of mouse at click (in px)
        - y: y-coordinate of mouse at click (in px)
        """

        if self.status == 'start_screen':
            self.start_screen(x, y)
        elif self.status == 'settings':
            self.update_settings(x, y)
        elif self.status == 'game':
            self.play_game(x, y)
        elif self.status == 'replay':
            self.new_game(x, y)
            

    def start_screen(self, x, y):
        """Start screen of the game.
        There are three options: start the game, look and 
        change the game settings, or quit the game.
        
        Args:
        - x: x-coordinate of mouse at click (in px)
        - y: y-coordinate of mouse at click (in px)
        """
        if self.view.start_game_button.is_clicked(x, y):
            self.status = 'game'
            self.get_settings()
            self.start_game()
        elif self.view.settings_button.is_clicked(x, y):
            self.status = 'settings'
        elif self.view.quit_game_button.is_clicked(x, y):
            self.status = 'end_game'
            self.play = False


    def get_settings(self):
        """Get the selected settings by the user"""
        for button in self.view.all_buttons:
            group = button.group
            if (group == 'vs_computer' or group == 'board_size') and button.selected:
                self.settings[group] = button.value


    def update_settings(self, x, y):
        """Settings page.
        Determine what settings the user changes. The values that can be changed are: 
        the opponent (human or AI), and the size of the board (3x3, 5x5, or 7x7).
        
        Args:
        - x: x-coordinate of mouse at click (in px)
        - y: y-coordinate of mouse at click (in px)
        """

        button_groups = ['vs_computer', 'board_size']

        # Check if button is clicked
        for button in self.view.all_buttons:
            if button.group in button_groups and button.is_clicked(x, y):
                
                # Update view of other buttons that are not selected
                for related_button in self.view.all_buttons:
                    if related_button.group == button.group and related_button.selected:
                        self.view.update_button_look(related_button, False, 
                                    self.view.LIGHT_GRAY, self.view.BLACK)

                # Update view of clicked button
                self.view.update_button_look(button, True, 
                                    self.view.GREEN, self.view.WHITE)
        
        # Check if user is satisfied with settings and wants to return to
        # start screen to start playing the game
        if self.view.back_button.is_clicked(x, y):
            self.status = 'start_screen'
            

    def start_game(self):
        """The game is started with the selected settings.
        The default settings are: human vs. human, and a 3x3 board."""

        # Create players
        self.player_list.append(Player('X', 'human'))
        
        if self.settings['vs_computer']:
            self.player_list.append(Player('O', 'AI'))
        else:
            self.player_list.append(Player('O', 'human'))
        
        random.shuffle(self.player_list)

        # Change starting screen to TicTacToe board
        self.board = Board(screen_size=self.view.screen_size, 
                           board_size=self.settings['board_size'])

        self.win_conditions()

        self.view.draw_board(board=self.board)
        player = self.get_current_player()
        self.view.show_turn(player.symbol, len(self.board.empty_tiles))


    def play_game(self, x, y):
        """This method takes the coordinates of the mouse when a click is registered,
        and takes these coordinates to find the corresponding tile. The tile is 
        afterwards filled with the correct symbol and in the end there is checked whether
        the last move results in a win or the next turn.
        
        Args:
        - x: x-coordinate of mouse at click (in px)
        - y: y-coordinate of mouse at click (in px)
        """

        clicked_tile = self.board.get_tile_at_pos(x, y)

        if clicked_tile is not None:
            player = self.get_current_player()
            player.make_move(clicked_tile, self.view)
            self.check_for_winner()


    def ai_move(self):
        """Let 'AI' make a random move as counter move"""
        ai = self.get_current_player()
        selected_tile = ai.chose_tile(self.board)

        pygame.time.delay(500)
        
        ai.make_move(selected_tile, self.view)
        self.check_for_winner()


    def next_turn(self):
        """Set next player for next turn"""
        player = self.get_current_player()
        next_player = 'O' if player.symbol != 'O' else 'X'
        self.current_player = 0 if self.move_nr % 2 == 0 else 1
        self.view.show_turn(next_player, len(self.board.empty_tiles))


    def check_for_winner(self):
        """Determine if one of the win conditions is met and if there
        is a winner, or if it is a draw. Else, continue game with next
        turn.
        """

        self.move_nr += 1
        self.check_win_conditions()

        if self.winner is not None:
            if self.winner == 'draw':
                self.view.show_message('Draw!', self.view.font)
            else:
                self.view.draw_win(self.winner, self.winning_tiles)
            
            self.status = 'replay'
        else:
            self.next_turn()


    def check_win_conditions(self):
        """Check for 2n + 2 win conditions and 1 draw condition.
        *) n = board size

        Example:
        - board size = 3
        - 3x horizontal, 3x vertical, 2x diagonal = 8 winconditions
        """
    
        board = self.board.board
        board_size = self.board.board_size

        for condition in self.win_combinations:
            states = []
            winning_tiles = []

            # Get states of tile of all combinations
            for index in condition:
                row = index // board_size
                column = index - (row * board_size)
                tile = board[row][column]

                states.append(tile.state)
                winning_tiles.append(tile)

            # Check for win
            if all(i == 'X' for i in states):
                self.winner = 'X'
                self.winning_tiles = winning_tiles
            elif all(i == 'O' for i in states):
                self.winner = 'O'
                self.winning_tiles = winning_tiles

        # Draw
        if self.winner is None and self.move_nr == (self.board.board_size ** 2):
            self.winner = 'draw'


    def win_conditions(self):
        """Add all indices of tiles together as winning combinations
        There are 2n + 2 win conditions and 1 draw condition

        For a 3x3 board this would be: 8 win conditions
        - Horizontal (3x): (0, 1, 2), (3, 4, 5), (6, 7, 8)
        - Vertical (3x): (0, 3, 6), (1, 4, 7), (2, 5, 8)
        - Diagonal (2x): (0, 4, 8), (2, 4, 6)
        """

        board_size = self.board.board_size
        tile_nrs = [x for x in range(0, board_size ** 2)]
        
        # Rows
        self.win_combinations += ([tuple(tile_nrs[i:i + board_size]) for i in range(0, len(tile_nrs), board_size)])

        # Columns
        self.win_combinations += ([tuple(x for x in range(y, len(tile_nrs), board_size)) for y in range(0, board_size)])

        # Diagonals
        self.win_combinations.append(tuple(x for x in range(0, len(tile_nrs), board_size + 1)))
        self.win_combinations.append(tuple(x for x in range(board_size - 1, len(tile_nrs) - (board_size - 1), board_size - 1)))


    def new_game(self, x, y):
        """Another game screen.
        Determine whether the user wants to play another game.
        
        Args:
        - x: x-coordinate of mouse at click (in px)
        - y: y-coordinate of mouse at click (in px)
        """
        
        self.winner = None
        self.winning_tiles = []
        self.win_combinations = []
        self.player_list = []

        self.move_nr = 0
        self.current_player = 0
        self.board.reset()

        # Two options: directly start next game, or go back to main start screen
        if self.view.play_again_button.is_clicked(x, y):
            self.status = 'start_screen'
        elif self.view.nomore_game_button.is_clicked(x, y):
            self.status = 'end_game'
            self.play = False
