import pygame
from pygame.locals import QUIT, MOUSEBUTTONUP, MOUSEMOTION, K_q

from controller.tictactoe import TicTacToe


def play():
    tictactoe = TicTacToe()
    tictactoe.view.clock.tick(60)

    while tictactoe.play:
        for event in pygame.event.get():
            if event.type == QUIT or pygame.key.get_pressed()[K_q]:
                tictactoe.play = False
                pygame.quit()
                break

            # Start screen
            if tictactoe.start_screen and event.type == MOUSEMOTION:
                x, y = event.pos
                tictactoe.view.follow_mouse(x, y)

            # During the game
            if event.type == MOUSEBUTTONUP:
                x, y = event.pos
                tictactoe.process_click(x, y)

                # Ask for new game
                if tictactoe.winner is not None:
                    tictactoe.new_game()
                    pygame.time.delay(500)

            pygame.display.update()

if __name__ == "__main__": play()
