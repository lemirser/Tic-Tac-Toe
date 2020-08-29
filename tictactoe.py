# ----- Global Variables -----

# Board
# Initialize an empty board
board = [
    "-",
    "-",
    "-",
    "-",
    "-",
    "-",
    "-",
    "-",
    "-",
]

# If game is still going
game_still_going = True

# Who won or tie?
winner = None

# Whose turn is it?
current_player = "X"


# Display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Play Game
def play_game():
    display_board()

    # Check whether to keep playing
    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(f"The winner is {winner}!")
    elif winner is None:
        print("Tie")


# Handle turn
def handle_turn(player):
    print(f"\n{player}'s turn!")
    position = input("Choose a position from 1-9: ")

    is_valid = False
    while not is_valid:
        # As long as the is_valid is False, then it will ask the user again for input. If the input is valid,
        # it will then check if the the board position is still available. If the board position is open (!= "-"),
        # then is_valued will be changed to True, ending the while loop.

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            # Check for user input validation
            # Regex can be used here
            print("\nPlease input a correct value!")
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            is_valid = True
        else:
            print("You can't go there. Go again!")

    board[position] = player

    display_board()


# Check win
def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # Access global variable
    global winner

    # Check rows
    row_winner = check_rows()

    # Check columns
    column_winner = check_columns()

    # Check diagonals
    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None

    return winner


def check_rows():
    # Access global variable
    global game_still_going
    global winner

    # Check whether rows have same values
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    # Return winner
    if row_1:
        winner = board[0]
    elif row_2:
        winner = board[3]
    elif row_3:
        winner = board[6]

    return winner


def check_columns():
    # Access global variable
    global game_still_going
    global winner

    # Check whether columns have same values
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    # Return winner
    if column_1:
        winner = board[0]
    elif column_2:
        winner = board[1]
    elif column_3:
        winner = board[2]

    return winner


def check_diagonals():
    # Access global variable
    global game_still_going
    global winner

    # Check whether diagonals have same values
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False

    # Return winner
    if diagonal_1:
        winner = board[0]
    elif diagonal_2:
        winner = board[6]

    return winner


# Check tie
def check_if_tie():
    # Access global variable
    global game_still_going

    if "-" not in board:
        game_still_going = False


def flip_player():
    # Access global variable
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


play_game()
