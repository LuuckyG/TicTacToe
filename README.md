# TicTacToe
A TicTacToe game made with PyGame, using an Object Orientated Design and Model View Controller (MVC) architecture.

To start the game run: `python -m play` in the terminal


## Game flow
The game follows the following flow:

1. **Start of game.** <br />A start screen is showed to the user, where (s)he can choose to either start or quit the game. 
The user also has the option to change the game settings, before starting the game.

2. **(optional) Adjusting settings.** <br />At the settings screen the user can change whether two players play against each other, or one player plays against the computer.
Moreover, the board size can be changed from 3x3 (default) to 5x5 or 7x7.

3. **The game** <br />The board, the current player and the number of empty tiles are shown to the user.

4. **Play again?** <br />If someone wins or the game is drawn, the user is asked if they wants to play again.
If yes, the user is taken back to the start screen. Else, the game is quit.

5. **Quit game.** <br />The user is thanked for playing the game and after some seconds the game window is closed.


## Game images
<img src="screenshots/startscreen.JPG" width="250"> <img src="screenshots/settings.JPG" width="250"> <img src="screenshots/board.JPG" width="250">
<img src="screenshots/endgame.JPG" width="250"> <img src="screenshots/thanks.JPG" width="250">
