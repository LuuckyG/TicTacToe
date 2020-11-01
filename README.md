# TicTacToe
A TicTacToe game made with PyGame, using an Object Orientated Design.

## Game flow
The game follows the following flow:

* 1) Start of game. 
A start screen is showed to the user, where (s)he can choose to either start or quit the game. 
The user also has the option to change the game settings, before starting the game.

![Start screen](/screenshots/startscreen.jpg?raw=true "Start screen")

* 2) (optional) Adjustng settings.
At the settings screen the user can change whether two players play against each other, or one player plays against the computer.
Moreover, the board size can be changed from 3x3 (default) to 5x5 or 7x7.

![Settings](/screenshots/settings.jpg?raw=true "Settings")

* 3) The game
The board, the current player and the number of empty tiles are shown to the user.

![Board](/screenshots/board.jpg?raw=true "Board")

* 4) Play again?
If someone wins or the game is drawn, the user is asked if they wants to play again.
If yes, the user is taken back to the start screen. Else, the game is quit.

![Play Again?](/screenshots/endgame.jpg?raw=true "Play Again?")

* 5) Quit game.
The user is thanked for playing the game and after some seconds the game window is closed.

![Thanks](/screenshots/thanks.jpg?raw=true "Thanks")


## Stil to do:
Add a smart AI, which makes good moves based on the current position. 
Make the strength of this AI also a setting which can be changed by the user.
