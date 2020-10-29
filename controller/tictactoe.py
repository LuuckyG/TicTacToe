import random
import pygame

from view.view import GameView
from model.board import Board
from model.player import HumanPlayer, ComputerPlayer


class TicTacToe:
    """Controller class of the game TicTacToe"""

    def __init__(self):
        """Setup of game TicTacToe. All game variables, and the board and view
        are created.
        """
        self.play = True
        self.start_screen = True
        self.winner = None
        self.winning_tiles = []
        self.win_combinations = []

        self.move_nr = 0
        self.player_list = []
        self.current_player = 0

        self.view = GameView()
        self.view.is_new_game()

    def get_settings(self, x, y):
        if self.view.human_vs_human_button.is_clicked(x, y):
            self.start_game()
        elif self.view.human_vs_ai_button.is_clicked(x, y):
            self.start_game(computer=True)

    def start_game(self, board_size=3, computer=False):
        """The game can only be started with two players. There is the choice between
        human vs human, or human vs AI."""

        # Create players
        self.add_player('X')
        if computer:
            self.add_player('O', human=False)
        else:
            self.add_player('O')
        
        random.shuffle(self.player_list)

        # Change starting screen to TicTacToe board
        self.start_screen = False
        self.board = Board(board_size=board_size)

        self.win_conditions()

        self.view.draw_board(board=self.board)
        self.view.show_turn(self.current_player, len(self.board.empty_tiles))

    def add_player(self, name, human=True):
        """Add player (human (default) or AI) to player list"""
        if human:
            player = HumanPlayer(name, 'human')
        else:
            player = ComputerPlayer(name, 'AI')
 
        self.player_list.append(player)
    
    def process_click(self, x, y):
        """The main method of the controller.
        This method takes the coordinates of the mouse when a click is registered,
        and takes these coordinates to find the corresponding tile. The tile is 
        afterwards filled with the correct symbol and in the end there is checked whether
        the last move results in a win or the next turn.

        Args:
            - x: x-coordinate of mouse at click (in px)
            - y: y-coordinate of mouse at click (in px)
        """

        if self.start_screen:
            if self.view.start_game_button.is_clicked(x, y):
                self.get_settings(x, y)
                self.start_screen = False
            elif self.view.quit_game_button.is_clicked(x, y):
                self.play = False
                pygame.quit()
        else:
            clicked_tile = self.board.get_tile_at_pos(x, y)

            # Fill clicked tile with symbol
            if clicked_tile is not None:
                if self.current_player == 0:
                    clicked_tile.state = 'X'
                    self.view.draw_x(clicked_tile)
                elif self.current_player == 1:
                    clicked_tile.state = 'O'
                    self.view.draw_o(clicked_tile)

                self.move_nr += 1

                # Check for winner
                pygame.display.update()
                self.check_win()

                if self.winner is not None:
                    if self.winner == 'draw':
                        self.view.draw_message('Draw!')
                    else:
                        self.view.draw_win(self.winner, self.winning_tiles)
                    
                    # self.play = False
                    self.new_game()
                else:
                    self.next_turn()

    def next_turn(self):
        """Set next player for next turn"""
        next_player = 1 if self.current_player == 0 else 0
        self.current_player = next_player
        self.view.show_turn(next_player, len(self.board.empty_tiles))

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

    def check_win(self):
        """ Check for 2n + 2 win conditions and 1 draw condition.
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

    def new_game(self):
        """Setup of new game, with same rules as current game."""
        
        # Show new game option
        self.view.is_new_game()
        
        # Ask for new game
        new_game = True     # PLACEHOLDER

        if new_game:
            self.play = True
            self.winner = None
            self.winning_tiles = []

            self.move_nr = 0
            self.player_list = []
            self.current_player = 0

            self.start_screen = True
            self.board.reset()
        else:
            self.view.draw_thanks()
