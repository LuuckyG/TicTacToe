import pygame

from view.view import GameView
from model.board import Board
from model.player import HumanPlayer, ComputerPlayer


class TicTacToe:
    """Controller class of the game TicTacToe"""

    def __init__(self, board_size, tile_size = 180):
        self.play = True
        self.winner = None
        self.winning_tiles = None

        self.move_nr = 0
        self.player_list = []
        self.current_player = 0

        self.board = Board(tile_size=tile_size,
                           board_size=board_size)
        self.view = GameView(tile_size=tile_size,
                             board=self.board)

        self.start_game()
    
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
        clicked_tile = self.board.get_tile_at_pos(x, y)

        if clicked_tile is not None:
            if self.current_player == 0:
                clicked_tile.state = 'X'
                self.view.draw_x
            elif self.current_player == 1:
                clicked_tile.state = 'O'
                self.view.draw_o

            pygame.display.update()
            self.check_win_conditions()

            if self.winner is not None:
                self.play = False
                self.view.draw_win(self.winner, self.winning_tiles)
            else:
                self.next_turn()

    def next_turn(self):
        self.move_nr += 1

        next_player = 1 if self.current_player == 0 else 0
        self.current_player = next_player

    def check_win_conditions(self):
        """ Check for 2n + 2 win conditions and 1 draw condition.
            *) n = board size

            Example:
            - board size = 3
            - 3x horizontal, 3x vertical, 2x diagonal = 8 winconditions
        """

        winner = None
        winning_tiles = None

        board = self.board.board
        board_size = self.board.board_size
        
        # Draw
        if self.move_nr == 9:
            self.winner = 'draw'
            return
               
        # Check rows
        for i in range(board_size):
            if board[i][0] != 'empty':
                
                winner = board[i][0]
                
                for j in range(1, board_size):
                    if (winner == board[i][j]):
                        winner = board[i][j]
                        winning_tiles.append((i,j))
                    else:
                        winner = None
                        winning_tiles = None
                        break
                
        # Determine if there is a winner
        if winner is not None:
            self.winner = winner
            self.winning_tiles = winning_tiles

        # Check columns
        for j in range(board_size):
            if board[0][j] != 'empty':
                
                winner = board[0][j]
                
                for i in range(1, board_size):
                    if (winner == board[i][j]):
                        winner = board[i][j]
                        winning_tiles.append((i,j))
                    else:
                        winner = None
                        winning_tiles = None
                        break
        
        # Determine if there is a winner
        if winner is not None:
            self.winner = winner
            self.winning_tiles = winning_tiles

        # Check diagonals
        if board[0][0] != 'empty':

            # First diagonal
            winner = board[0][0]
            for i in range(1, board_size):
                if (winner == board[i][i]):
                    winner = board[i][i]
                    winning_tiles.append((i,i))
                else:
                    winner = None
                    winning_tiles = None
                    break
        
        # Determine if there is a winner
        if winner is not None:
            self.winner = winner
            self.winning_tiles = winning_tiles
        
        elif board[0][board_size] != 'empty':
            
            # Second diagonal
            winner = board[0][board_size]
            for i in range(1, board_size):
                if (winner == board[i][board_size - i]):
                    winner = board[i][board_size - i]
                    winning_tiles.append((i, board_size - i))
                else:
                    winner = None
                    winning_tiles = None
                    break

        # Determine if there is a winner
        if winner is not None:
            self.winner = winner
            self.winning_tiles = winning_tiles
        

    def new_game(self):
        new_game = self.view.is_new_game()

        if new_game:
            self.play = True
            self.winner = None
            self.winning_tiles = None

            self.move_nr = 0
            self.player_list = []
            self.current_player = 0

            self.board.reset()

        else:
            self.view.draw_thanks()
