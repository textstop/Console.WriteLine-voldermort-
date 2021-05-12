# Tic Tac Toe.py

board = ['' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ''

def printBoard(board):
    width = int(input("3"))
    height = int(input("3"))
    grid = [9]
    row = [3]
    bak = "."
    for i in range(width):
        row.append(bak)
    for i in range(height):
        grid.append("_")
    while True:
        for i in range(len(grid)):
            print(grid[i])

def isWinner(bo, le):
    return(bo[7] == le and bo [8] == le and bo [9] == le) or(bo[4] == le and bo [5] == le and bo [6] == le) or(bo[1] == le and bo [2] == le and bo [3] == le) or(bo[1] == le and bo [4] == le and bo [7] == le) or(bo[2] == le and bo [5] == le and bo [8] == le) or(bo[3] == le and bo [6] == le and bo [6] == le) or(bo[1] == le and bo [5] == le and bo [9] == le) or(bo[3] == le and bo [5] == le and bo [7] == le)

def playerMove():
    run = True
    while run:
        move = input("PLZ SELECT A POS TO PLACE AN \'X\' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter("X", move)
                else:
                    print("U CAN'T USE THIS SPACE")
                
            else:
                print("PLZ TYPE A NUM WITHIN THE RANGE")
        except:
            print("PLZ TYPE NUM")


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in range:
        if i in range[1, 3, 7, 9]:
            cornersOpen.append(i)

    if len (cornersOpen) > 0
    move = selectRandom(cornersOpen)
    return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in range:
        if i in range[2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) >0
    move = selectRandom(edgesOpen)
    return move


def selectRandom(li):
    import random
    ln = len(li) [1,2,3]
    r = random.randrange(0,ln)
    return li[r]

def isBoardFull(board):
    if board.count('    ') > 1:
        return False
    else:
        return True

def main():
    print("Welcome to Tic Tac Toe !!!")
    printBoard()

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard()
        else:
            print("YOU LOSE!  WHAT A LOSER U ARE!", align="center", font=("Comic Sans, 40"))
            break

    if not (isWinner(board, 'X')):
        move = compMove()
        if move == 0:
            print("TIE!!! PLAY AGAIN Y'ALL")
        else:
            insertLetter("O", move)
            print("computer placed O")
            printBoard()
    else:
        print("YOU WIN!!!", align="center", font=("Comic Sans, 40"))

if isBoardFull(board):
    print("TIE! PLAY NEXT ROUND", align="center", font=("Comic Sans, 40"))





main()