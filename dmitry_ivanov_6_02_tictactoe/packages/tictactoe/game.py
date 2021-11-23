def board_render(board):
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

def game_status(board):
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