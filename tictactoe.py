"""
Script file: tictactoe.py


Purpose: This program uses a non-OOP tit-tac-toe game

Date: 08/22/21

Author: Mr. Asiamah

"""

ALL_SPACES = list('123456789')  #The keys for a TTT board dictionary
X, O, BLANK = 'X', 'O', ' '     # Constants for string values

def main():
    """Runs a game of tic-tac-toe."""
    print("Welcome to tic-tac-toe!")
    gameBoard = getBlankBoard()     # Create a TTT board dictionary
    currentPlayer, nextPlayer = X, O,  # X goes first, 0 goes next


    while True:
        print(getBoardStr(gameBoard))   # Display the board on the screen

        # Keep asking the player they enter a number 1 - 9

        move = None
        while not isValidSpace(gameBoard, move):
            print(f'What is {currentPlayer}\'s move? (1-9)')
            move = input()
        updateBoard(gameBoard, move, currentPlayer) # Make the move

        # check if the game is over:
        if isWinner(gameBoard, currentPlayer): ## First check for victory
            print(getBoardStr(gameBoard))
            print(currentPlayer + ' has won the game!')
            break
        elif isBoardFull(gameBoard):   # Next check for a tie
            print(getBoardStr(gameBoard))
            print('The game is a tie!')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer   # swap turns
    print('Thanks for playing!')


def getBlankBoard():
        """Create a new, blank tic-tac-toe board"""

        board  = {}  # The board is represented as a Python dictionary
        for space in ALL_SPACES:
            board[space] = BLANK    # All spaces start as blank
        return board

def getBoardStr(board):
    """Return a text-representation of the board."""
    return f'''
        {board['1']}|{board['2']}|{board['3']} 1 2 3
        -+-+-
        {board['4']}|{board['5']}|{board['6']} 4 5 6
        -+-+-
        {board['7']}|{board['8']}|{board['9']} 7 8 9'''


def isValidSpace(board, space):
    """Returns True if the space on the board is a valid space number
    and the space is blank."""
    return space in ALL_SPACES or board[space] == BLANK


def isWinner(board, player):
    """ Returns True if player is a winner on this TTTBoard """
    b, p = board, player  # Shorter names as "syntatic sugar"
        # Check for 3 marks across the 3 row, 3 columns, an 2 diagonals
    return ((b['1'] == b['2'] == b['3'] == p) or # ACross the top
            (b['4'] == b['5'] == b['6'] == p) or # ACross the middle
            (b['7'] == b['8'] == b['9'] == p) or # ACross the bottom
            (b['1'] == b['4'] == b['7'] == p) or # Down the left
            (b['2'] == b['5'] == b['8'] == p) or # Down the middel
            (b['3'] == b['6'] == b['9'] == p) or # Down the right
            (b['3'] == b['5'] == b['7'] == p) or # Diagonal
            (b['1'] == b['5'] == b['9'] == p))  # Diagonal


def isBoardFull(board):
    """Return if every space on the board has been taken."""
    for space in ALL_SPACES:
        if board[space]== BLANK:
            return False #If a single is blank, return False.
    return True  # No spaces are blank, so return True

def updateBoard(board, space, mark):
    """Set the space on the board to mark"""
    board[space] = mark
    

if __name__ == '__main__':
    main()      # Call the main is this module is run, but  when imported


















            
