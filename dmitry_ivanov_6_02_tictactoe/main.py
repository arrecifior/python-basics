################################################################
###                                                          ###
###   AUTHOR      : Dmitry Ivanov                            ###
###   DATE        : 2021-11-22                               ###
###   DESCRIPTION : This program is a game of Tic Tac Toe.   ###
###                 The computer uses random numbers to      ###
###                 make moves.                              ###  
###                                                          ###
###                 Updated to use modules.                  ###
###                                                          ###
################################################################

import time

# custom modules
from packages.tictactoe import game
from packages.tictactoe import move

###########################
###   Main game logic   ###
###########################

# init board with field indexes
board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

# game starts
print('''
╒═════════════════════════════╕
│                             │
│   Welcome to the game of    │
│        TIC-TAC-TOE!         │
│                             │
╘═════════════════════════════╛''')
time.sleep(1)
'''
    Artificial delays are important for a good user experience.
    If it takes time for a program to do important things,
    it seems more human and less intimidating.
'''
print('''┌─────────────────────────────┐
┆ Computer makes the first    ┆
┆ move                        ┆
└─────────────────────────────┘''')
print("             . . .             ")
time.sleep(1)
# first computer's move
board = move.make(board, "X", 5)
game.print_board(board)

move_count = 2
while True:

    # checking game status for game finish condition
    status = game.status(board)
    if status == "tie":
        print('''╒═════════════════════════════╕
│                             │
│         Game Over.          │
│        It is a tie!         │
│                             │
╘═════════════════════════════╛''')
        break
    elif status == "win":
        print('''╒═════════════════════════════╕
│     *     *          #      │
│         Game Over.      #   │
│   #      You WON!           │
│        #              *     │
╘═════════════════════════════╛''')
        break
    elif status == "lose":
        print('''╒═════════════════════════════╕
│                             │
│         Game Over.          │
│       Computer wins!        │
│                             │
╘═════════════════════════════╛''')
        break

    if move_count % 2 == 0:
        time.sleep(1)
        board = move.player(board)
        time.sleep(0.2)
    else:
        time.sleep(1.5)
        board = move.computer(board)
        time.sleep(1)
    game.print_board(board)

    move_count += 1
