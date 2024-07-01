import random

board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-",
]

currentPlayer =  "X"
winner = None
gameRunning = True

# Print game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("-----------")

# Take player input
def playerInput(board):
    number = int(input("Enter a number from 1 - 9: "))
    if number >= 1 and number <= 9 and board[number - 1] == "-":
        board[number - 1] = currentPlayer
    else:
        print("Ooopppssss, spot unavailable!")

# Check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "-":
        winner = board[6]
        return True
    
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Hurrayyyy! It's a tie")
        gameRunning = False

def checkWin():
    global gameRunning
    if checkHorizontal(board) or checkRow(board) or checkDiagonal(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning = False

# Switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Computer
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

# Check for win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    checkWin()
    computer(board)
    checkWin()
    checkTie(board)
