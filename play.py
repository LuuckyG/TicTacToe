import pygame

from controller.tictactoe import TicTacToe


def play():
    play = True
    TicTacToe(board_size=3)

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
                pygame.quit()
                play = False
                break
        


if __name__ == "__main__": play()
