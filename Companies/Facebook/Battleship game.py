from random import randint

board = []
for i in range(0,5):
    board.append(["0"]*5)

def printBoard(board):
    for i in board:
        print(" ".join(i))

def randRow(board):
    return randint(0, len(board)-1)

def randCol(board):
    return randint(0, len(board[0]) - 1)

ship_row = randRow(board)
ship_col = randCol(board)
#print(ship_row)
#print(ship_row)
printBoard(board)

for turn in range(4):
    print("Turn:", turn)
    guess_row = int(input())
    guess_col = int(input())

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations")
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col > 5 or guess_col < 0):
            print("Oops not in Ocean")
        elif board[guess_row][guess_col] == "X":
            print("Already there")
        else:
            print("You missed")
            board[guess_row][guess_col] = "X"
            if turn == 3:
                print("Game over")
            printBoard(board)
