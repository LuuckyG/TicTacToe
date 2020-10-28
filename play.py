import pygame
from pygame.locals import QUIT, MOUSEBUTTONUP, K_q

from controller.tictactoe import TicTacToe


def play():
    tictactoe = TicTacToe(board_size=5)
    tictactoe.view.clock.tick(60)

    while tictactoe.play:
        for event in pygame.event.get():
            if event.type == QUIT or pygame.key.get_pressed()[K_q]:
                tictactoe.play = False
                pygame.quit()
                break
            
            # Check if click is valid move, if so make move
            if event.type == MOUSEBUTTONUP:
                x, y = event.pos
                tictactoe.process_click(x, y)
    
                # Ask for new game
                if tictactoe.winner is not None:
                    tictactoe.new_game()
    
        pygame.time.delay(500)


if __name__ == "__main__": play()
