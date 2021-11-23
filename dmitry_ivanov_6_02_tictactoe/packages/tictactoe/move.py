from random import randrange

def make_move(board, player, field):
    # accepts 'player' mark and puts it into the 'field' by index
    # returns True if the move i valid, False if invalid

    put_move = False # move is invalid by default
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == field:
                board[i][j] = player
                put_move = True # marks move as valid and done
    if put_move:
        return board
    else:
        return put_move

def move_player(board):
    # player's move
    print('''┌─────────────────────────────┐
┆ It's your turn              ┆
└─────────────────────────────┘''')
    while not make_move(board, "O", int(input("Enter your move: "))):
        print("Invalid move! Try again.")
    return board        

def move_computer(board):
    #computer's move
    print('''┌─────────────────────────────┐
┆ Computer makes a move       ┆
└─────────────────────────────┘''')
    print("             . . .             ")
    while not make_move(board, "X", randrange(1,10)):
        pass
    return board