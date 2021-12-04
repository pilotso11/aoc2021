import re

draws = []
boards = []
with open("day4.input") as f:
    l = f.readline().strip()
    draws = l.split(",")
    f.readline() # skip blank line

    while True:
        board = []
        for row in range(5):
            l = f.readline().strip()
            if len(l) == 0:
                break
            row = re.split('[ ]+', l)
            board.append(row)
        if len(board) == 5:
            #print(board)
            boards.append(board)
        else:
            break
        f.readline() # skip blank line

def checkBoard(board, draws):
    # print("check board",board)
    for row in range(5):
        win = True
        for col in range(5):
            if board[row][col] not in draws:
                # print("stop row on ", row, col, "val=", board[row][col])
                win = False
                break
        # row win
        if win:
            return ("row", row)
    for col in range(5):
        win = True
        for row in range(5):
            if board[row][col] not in draws:
                # print("stop col on ", row, col, "val=", board[row][col])
                win = False
                break
        # col win
        if win:
            return ("col", col)
    return ("", -1)

def calcUnmarked(board, draws):
    sum = 0
    for row in board:
        for col in row:
            if col not in draws:
                sum += int(col)
    return sum

drawn = [] 
wins = []
for draw in draws:
    #print("draw ", draw)
    drawn.append(draw)
    #print(drawn)
    for b in range(len(boards)):
        if b not in wins:
            result = checkBoard(boards[b], drawn)
            if result[0] != "":
                print("Win on board", b, " ", result[0], " at ", result[1])
                print("last draw=", draw)
                sum = calcUnmarked(boards[b], drawn)
                print("sum=", sum, "score=", sum * int(draw))
                wins.append(b)





