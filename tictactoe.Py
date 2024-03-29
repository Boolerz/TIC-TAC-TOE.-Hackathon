import random 

board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]
currentPlayer = "X"
Winner = None
gameRunning = True

#print the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("__|___|___")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("__|___|___")
    print(board[6] + " | " + board[7] + " | " + board[8])
#take player input
def playerInput(board):
    inp = int(input("Enter a number 1-9:"))
    if inp >= 1 and inp <= 9 and board[inp-1] == "_":
        board[inp-1] = currentPlayer
    else:
        print("Ooops ! Spot is already in Occupied.")
#check for win or tie
def checkHorizotle(board):
    global Winner
    if board[0] == board[1] == board[2] and board[0] != "_":
        Winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        Winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        Winner = board[6]
        return True
    
def checkRow(board):
    global Winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        Winner = board[0]
        return True
    elif board[1] == board[4] ==board[7] and board[1] != "_":
        Winner = board[1]
        return True
    elif board[2] == board[5] ==board[8] and board[2] != "_":
        Winner = board[2]
        return True
    
def checkDiag(board):
    global Winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        Winner = board[0]
        return True
    elif board[2] == board[4] ==board[6] and board[2] != "_":
        Winner = board[2]
        return True
    
def checkTie (board):
    global gameRunning
    if "_" not in board:
        printBoard(board)
        print("It is a tie")
        gameRunning = False
        exit()
        
def checkWin():
    if checkDiag(board) or checkHorizotle(board) or checkRow(board):
        print(f"The winner is {Winner}")
        exit()

        
#swith the player
def switchPlayer ():
    global currentPlayer
    if currentPlayer =="X":
        currentPlayer = "O"
    else: 
        currentPlayer = "X"
        
#computer
def computer(board):
    while currentPlayer == "0":
        position = random.randint(0,8)
        if board[position] == "_":
            board[position] = "0"
            switchPlayer()
#check for win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)