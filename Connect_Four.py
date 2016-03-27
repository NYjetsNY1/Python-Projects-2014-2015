# Ben Sklar
# Connect 4
# Plays the game of Connect 4 against the computer.
# Can play-again as many times as the player wants.
# Uses functions, random computer moves, "global" variables, variables, for and while loops, etc.
# Includes all extensions.

import random
# Global constants, mostly to make the code more readable.
X = "X"
O = "O"
EMPTY = " " 
TIE = "TIE"
NUM_ROWS = 6
NUM_COLS = 8


def display_instruct():
    """Display game instructions."""  
    print(
    """
    Welcome to the second greatest intellectual challenge of all time: Connect4.  
    This will be a showdown between your human brain and my silicon processor.  

    You will make your move known by entering a COLUMN number, 1 - 7.  Your move 
    (if that COLUMN isn't already filled) will move to the lowest available position.

    Prepare yourself, human.  May the Schwartz be with you! \n
    """
    )


def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Ask for a number within a range."""
    # Allows user to choose only a number in the range 1 through 7 (the columns).
    response = None
    while response not in range(low, high):
        response = input(question)
        if response.isdigit() == False:
            print("Try again.")
        else:
            response = int(response)
    return response


def pieces():
    """Determine if player or computer goes first."""
    go_first = ask_yes_no("Do you require the first move? (y/n): ")
    if go_first == "y":
        print("\nThen take the first move.  You will need it.")
        human = X
        computer = O
    else:
        print("\nYour bravery will be your undoing... I will go first.")
        computer = X
        human = O
    return computer, human


def new_board():
    """Create new game board.  Our board is 6 rows (as normal)
    and 8 columns - one extra to facilitate user input.  Column
    0 is not used."""
    # Defines the board. This will create an empty board.
    board = []
    for j in range(NUM_ROWS):
        row = []
        board.append(row)
        for i in range(NUM_COLS):
            row.append(EMPTY)
    return board


def display_board(board):
    """Display game board on screen."""
    for r in range(NUM_ROWS):
        print_row(board, r)
    print("\n")


def print_row(board, num):
    """Print specified row from current board"""
    this_row = board[num]
    print("\n\t", this_row[1], "|", this_row[2], "|", this_row[3], "|", this_row[4], "|", this_row[5], "|", this_row[6], "|", this_row[7])
    print("\t", "--------------------------")
    

def legal_moves(board):
    """Create list of column numbers into which legal moves can be made."""
    # Any column with space still available is legal. This function makes this work.
    moves = []
    column = 0
    for i in board[0]:
        if i == EMPTY and column > 0:
            moves.append(column)
        column += 1
    return moves
 

def winner(board):
    """ Determine the game winner, using the Connect 4 board as a parameter.  
      If there is no winner, the function will return the empty string ""
      if moves are still available; else it will return TIE.  
      If the user has won, it will return 'X', and if the computer has
      won it will return 'O'."""

    # Check rows for winner.
    for i in range(NUM_ROWS):
        for j in range(1, 4):
            if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] != EMPTY:
                return board[i][j]


    # Check columns for winner.
    for j in range(NUM_COLS):
        for i in range(0, 3):
            if board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j] != EMPTY:
                return board[i][j]


    # Check diagonal (top-left to bottom-right) for winner.
    for diagrow in range(3):
        for diagcol in range(4):
            if (board[diagrow][diagcol] == board[diagrow + 1][diagcol + 1] == board[diagrow + 2][diagcol + 2] ==\
                board[diagrow + 3][diagcol + 3]) and (board[diagrow][diagcol] != " "):
                return board[diagrow][diagcol]
           
   
    # Check diagonal (bottom-left to top-right) for winner.
    for diagrow in range(5, 2, -1):
        for diagcol in range(3):
            if (board[diagrow][diagcol] == board[diagrow - 1][diagcol + 1] == board[diagrow - 2][diagcol + 2] ==\
                board[diagrow - 3][diagcol + 3]) and (board[diagrow][diagcol] != " "):
                return board[diagrow][diagcol]

            
    # Return "TIE" if game is over (board is full).
    if legal_moves(board) == []:
        return TIE


def human_move(board, human):
    # Allows the move to be globally available.
    # Allows user to choose what column they'd like to move to.
    global move
    """Get human move."""  
    legals = legal_moves(board)
    print("LEGALS:", legals)
    move = None
    while move not in legals:
        move = ask_number("Which column will you move to? (1-7): ", 1, NUM_COLS)
        if move not in legals:
            print("\nThat column is already full, nerdling.  Choose another.\n")
    print("Human moving to column", move)
    # Return the column number chosen by user.
    return move


def computer_move(board):
    # Allows the computer move to be globally available.
    # Makes the computer move somewhere between columns 1 and 7 at random.
    global comp_move
    """Make computer move."""
    legals = legal_moves(board)
    comp_move = None
    while comp_move not in legals:
        comp_move = random.randrange(1, 8)
    print("Computer moving to column", comp_move)
    return comp_move


def get_move_row(board, number):
    # Gets the move, row.
    row = []
    for i in range(NUM_ROWS):
        if board[NUM_ROWS - 1 - i][number] == EMPTY:
            return (NUM_ROWS - 1 - i)

def next_turn(turn):
    """Switch turns."""
    if turn == X:
        return O
    else:
        return X

    
def congrat_winner(the_winner, computer, human):
    """Congratulate the winner."""
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")

    if the_winner == computer:
        print("As I predicted, human, I am triumphant once more.  \n" \
              "Proof that computers are superior to humans in all regards.")

    elif the_winner == human:
        print("No, no!  It cannot be!  Somehow you tricked me, human. \n" \
              "But never again!  I, the computer, so swear it!")

    elif the_winner == TIE:
        print("You were most lucky, human, and somehow managed to tie me.  \n" \
              "Celebrate today... for this is the best you will ever achieve.")


def main():
    # Allows you to play multiple times.
    play_again = True
    
    while play_again:
        display_instruct()
        computer, human = pieces()
        turn = X
        board = new_board()
        display_board(board)

        while not winner(board):
            if turn == human:
                  human_move(board, human)
                  lowest_row = get_move_row(board, move)
                  board[lowest_row][move] = human
              
            # IT'S THE COMPUTER'S MOVE.
            else:
                 computer_move(board)
                 lowest_row = get_move_row(board, comp_move)
                 board[lowest_row][comp_move] = computer
            display_board(board)
            turn = next_turn(turn)
            print("IN NEXT_TURN ... with", turn)

        the_winner = winner(board)
        congrat_winner(the_winner, computer, human)
        play_another = input("\n\nDo you want to play again? Type \"n\" and Enter for no, otherwise just press Enter: ")
        # If you don't want to play again, choose "n" for no, otherwise you play again!
        if play_another == "n":
            play_again = False


# Start the program.
main()
input("\n\nPress the enter key to quit. ")
