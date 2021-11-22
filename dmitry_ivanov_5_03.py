################################################################
###                                                          ###
###   AUTHOR      : Dmitry Ivanov                            ###
###   DATE        : 2021-11-20                               ###
###   DESCRIPTION : This program is a game of Tic Tac Toe.   ###
###                 The computer uses random numbers to      ###
###                 make moves.                              ###  
###                                                          ###
################################################################

import time
from random import randrange

def board_render():
    # prints current state of the board to the console
    print("╭─────────┬─────────┬─────────╮")
    for i in range(len(board)):
        print("│         │         │         │\n│    ", end='')
        for j in range(len(board[i])):
            print(board[i][j], end='    │    ')
        print("\n│         │         │         │")
        if i < len(board) - 1:
            print("├─────────┼─────────┼─────────┤")
    print("╰─────────┴─────────┴─────────╯")

def make_move(player, field):
    # accepts 'player' mark and puts it into the 'field' by index
    # returns True if the move i valid, False if invalid

    put_move = False # move is invalid by default
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == field:
                board[i][j] = player
                put_move = True # marks move as valid and done
    return put_move

def move_player():
    # player's move
    print('''┌─────────────────────────────┐
┆ It's your turn              ┆
└─────────────────────────────┘''')
    while not make_move("O", int(input("Enter your move: "))):
        print("Invalid move! Try again.")

def move_computer():
    #computer's move
    print('''┌─────────────────────────────┐
┆ Computer makes a move       ┆
└─────────────────────────────┘''')
    print("             . . .             ")
    while not make_move("X", randrange(1,10)):
        pass

def game_status():
    # checks board for the game status
    # returns 'continue' if there is no game result
    #         'tie' for a tie, 'win' for player's
    #         win and 'lose' for computer's win
    if_win = False
    if_lose = False
    if_full = True

    # win/lose checks
    # diagonal lines check
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        if_lose = True
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        if_lose = True
    # horizontal lines check
    for i in range(len(board)):
        move_value = board[i][0]
        moves_equal = True
        for j in range(len(board[i])):
            if board[i][0] != board[i][j]:
                moves_equal = False
        if moves_equal:
            if move_value == "O":
                if_win = True
            elif move_value == "X":
                if_lose = True
    # vertical lines check
    for j in range(len(board[0])):
        move_value = board[0][j]
        moves_equal = True
        for i in range(len(board)):
            if board[0][j] != board[i][j]:
                moves_equal = False
        if moves_equal:
            if move_value == "O":
                if_win = True
            elif move_value == "X":
                if_lose = True

    # full board check
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != "O" and board[i][j] != "X":
                if_full = False

    if if_win:
        return "win"
    elif if_lose:
        return "lose"
    elif if_full:
        return "tie"
    else:
        return "continue"

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
make_move("X", 5)
board_render()

move_count = 2
while True:

    # checking game status for game finish condition
    status = game_status()
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
        move_player()
        time.sleep(0.2)
    else:
        time.sleep(1.5)
        move_computer()
        time.sleep(1)
    board_render()

    move_count += 1
