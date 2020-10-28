import pygame

from view.view import GameView
from model.board import Board
from model.player import HumanPlayer, ComputerPlayer


class TicTacToe:
    """Controller class of the game TicTacToe"""

    def __init__(self, board_size, tile_size = 180):
        self.play = True
        self.winner = None
        self.winning_tiles = []
        self.win_combinations = []

        self.move_nr = 0
        self.player_list = []
        self.current_player = 0

        self.board = Board(tile_size=tile_size,
                           board_size=board_size)
        self.view = GameView(tile_size=tile_size,
                             board=self.board)

        self.start_game()
        self.win_conditions()
        print(self.win_combinations)
    
    def start_game(self):
        self.add_player('player1')
        self.add_player('player2')

    def add_player(self, name, human=True):
        """Add player (human (default) or AI) to player list"""

        if len(self.player_list) > 2:
            # No more than 2 players
            self.play = False
            return
        
        player_nr = len(self.player_list)
        if human:
            player = HumanPlayer(name, player_nr, 'human')
        else:
            player = ComputerPlayer(name, player_nr, 'AI')
 
        self.player_list.append(player)
    
    def process_click(self, x, y):
        x = (x // self.board.tile_size) * self.board.tile_size
        y = (y // self.board.tile_size) * self.board.tile_size
        clicked_tile = self.board.get_tile_at_pos(x, y)

        if clicked_tile is not None:
            if self.current_player == 0:
                clicked_tile.state = 'X'
                self.view.draw_x(clicked_tile)
            elif self.current_player == 1:
                clicked_tile.state = 'O'
                self.view.draw_o(clicked_tile)

            pygame.display.update()
            self.check_win()

            if self.winner is not None:
                self.play = False
                self.view.draw_win(self.winner, self.winning_tiles)
                pygame.display.update()
            else:
                self.next_turn()

    def next_turn(self):
        self.move_nr += 1

        next_player = 1 if self.current_player == 0 else 0
        self.current_player = next_player

    def win_conditions(self):
        """Add all indices of tiles together as winning combinations
        There are 2n + 2 win conditions and 1 draw condition

        For a 3x3 board this would be: 8 win conditions
            - Horizontal (3x): (0, 1, 2), (3, 4, 5), (6, 7, 8)
            - Vertical (3x): (0, 3, 6), (1, 4, 7), (2, 5, 8)
            - Diagonal (2x): (0, 4, 8), (2, 4, 6)
        """

        board_size = self.board.board_size
        tile_nrs = [x for x in range(0, board_size * board_size)]
        
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
        if self.winner is None and self.move_nr == 9:
            self.winner = 'draw'

    def new_game(self):
        new_game = self.view.is_new_game()

        if new_game:
            self.play = True
            self.winner = None
            self.winning_tiles = []

            self.move_nr = 0
            self.player_list = []
            self.current_player = 0

            self.board.reset()

        else:
            self.view.draw_thanks()
