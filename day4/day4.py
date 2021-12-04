# Part one
with open('day4/input.txt') as f:
    scans = f.readlines()

drawList = list(map(int, scans[0].rstrip("\n").split(',')))

list_of_boards = []

board = []
for el in scans[2:]:
    if el == "\n":
        list_of_boards.append(board)
        board = []
        continue
    el = list(map(int, el.split()))
    board.append(el)

winList = []
lastBoardDrawnNumber, lastBoardDrawnindex = -1, -1
firstBoardDrawnNumber, firstBoardDrawnindex = -1, -1

for final, num in enumerate(drawList):
    if lastBoardDrawnNumber != -1:
        break
    for index, board in enumerate(list_of_boards):
        if index in winList: # if the the the current card has already won, skip it
            continue
        for i in range(len(board)):
            for j in range(len(board)):
                if num == board[i][j]:
                    board[i][j] = -1 # leave a mark on the card

        for k in range(len(board)): # counting the numbers in row/column
            rowCounter, columnCounter = 0, 0
            for l in range(len(board)):
                if board[k][l] == -1:
                    rowCounter += 1
                if board[l][k] == -1:
                    columnCounter += 1
                if columnCounter == 5 or rowCounter == 5: # if 5 then bingo
                    if len(winList)+1 == len(list_of_boards): # remember the first winning card
                        lastBoardDrawnNumber = num
                        lastBoardDrawnindex = index
                        break
                    if index not in winList: winList.append(index) # remember the last winning card
                    if len(winList) == 1:
                        firstBoardDrawnNumber = num
                        firstBoardDrawnindex = index
                    break
        

# add the unmarked spots
total = 0
for column in list_of_boards[firstBoardDrawnindex]:
    for num in column:
        if num == -1:
            continue
        total += num
total *= firstBoardDrawnNumber  # mul by the last drawn number
print(total)

# add the unmarked spots
total = 0
for column in list_of_boards[lastBoardDrawnindex]:
    for num in column:
        if num == -1:
            continue
        total += num
total *= lastBoardDrawnNumber # mul by the last drawn number
print(total)

                    
        
                    




    