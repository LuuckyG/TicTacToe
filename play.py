import pygame
from pygame.locals import QUIT, MOUSEBUTTONUP, MOUSEMOTION, K_q

from controller.tictactoe import TicTacToe


def play():
    """The main game loop"""
    tictactoe = TicTacToe()
    tictactoe.view.clock.tick(60)

    while tictactoe.play:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT or pygame.key.get_pressed()[K_q]:
                tictactoe.play = False
                pygame.quit()
                break
            
            # Start and settings screens
            if tictactoe.status != 'game':
                if event.type == MOUSEMOTION:
                    x, y = event.pos
                    tictactoe.view.follow_mouse(x, y)
                
                elif event.type == MOUSEBUTTONUP:
                    x, y = event.pos
                    tictactoe.process_click(x, y)

            # During the game
            if tictactoe.status == 'game':
                player = tictactoe.player_list[tictactoe.current_player]

                if player.player_type == 'AI':
                    tictactoe.ai_move()

                elif event.type == MOUSEBUTTONUP:
                    x, y = event.pos
                    tictactoe.process_click(x, y)

            tictactoe.view.draw_screens(tictactoe.status)

if __name__ == "__main__": play()
