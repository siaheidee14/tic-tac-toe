# --------------- Global Variables -------------------

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If Game is still going
game_still_going = True

# Who won? or tie?
winner = None

# Who's turn is it?
current_player = 'X'

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Play a game of tic-tac-toe
def play_game():
    # Display initial board
    display_board()

    # while the game is still going
    while game_still_going:
        # handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # change to other player
        change_player()

    # The game has ended
    if winner == 'X' or winner == 'O':
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

# Handle a single turn of an arbitrary player
def handle_turn(player):
    print(player + "'s turn.")
    position = input('Choose a position from 1-9: ')

    valid_inputs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    valid = False
    while not valid:
        # check if input is valid
        while position not in valid_inputs:
            position = input('Choose a position from 1-9: ')
        position = int(position) - 1
        if board[position] == '-':
            valid = True
        else:
            print("You can't go there try again")
    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    # Setup global variable
    global winner

    # check rows
    row_winner = check_rows()

    # check columns
    column_winner = check_columns()

    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    # Setup up global variables
    global game_still_going

    # check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    # if any rows does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner (x or o)
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return

def check_columns():
    # Setup up global variables
    global game_still_going

    # check if any of the columns have all the same value (and is not empty)
    col_1 = board[0] == board[3] == board[6] != '-'
    col_2 = board[1] == board[4] == board[7] != '-'
    col_3 = board[2] == board[5] == board[8] != '-'

    # if any columns does have a match, flag that there is a win
    if col_1 or col_2 or col_3:
        game_still_going = False
    # Return the winner (x or o)
    if col_1:
        return board[0]
    if col_2:
        return board[1]
    if col_3:
        return board[2]
    return

def check_diagonals():
    # Setup up global variables
    global game_still_going

    # check if any of the columns have all the same value (and is not empty)
    diag_1 = board[0] == board[4] == board[8] != '-'
    diag_2 = board[6] == board[4] == board[2] != '-'

    # if any columns does have a match, flag that there is a win
    if diag_1 or diag_2:
        game_still_going = False
    # Return the winner (x or o)
    if diag_1:
        return board[0]
    if diag_2:
        return board[6]
    return

def check_if_tie():
    # Setup global variable
    global game_still_going

    if '-' not in board:
        game_still_going = False
    return

def change_player():
    # Global variable we need
    global current_player

    # if the current player was x, then change it to o
    if current_player == 'X':
        current_player = 'O'
        # if the current player was O, then change it to X
    elif current_player == 'O':
        current_player = 'X'
    return

play_game()
