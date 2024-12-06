

################# DAY4 ################
##PART1
def word_search(board):
    occ = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            print(i,j)
            if board[i][j] == "X":
                if j+3 <= len(board[0])-1:
                    if board[i][j] + board[i][j+1]+board[i][j+2]+board[i][j+3] == "XMAS":
                        occ += 1
                if i+3 <= len(board)-1 and j+3 <= len(board[0])-1:
                    if board[i][j] + board[i+1][j+1]+board[i+2][j+2]+board[i+3][j+3] == "XMAS":
                        occ += 1
    return occ

#### part 2
def word_search(board):
    occ = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "A":

                if j>0 and i > 0 and  (j+1 <= len(board[0])-1 and i+1 <= len(board) -1) :
                    if board[i-1][j-1] == "M" and board[i-1][j+1] == "M" and board[i+1][j-1] == "S" and board[i+1][j+1] == "S":
                        print(i,j)
                        occ += 1
    return occ

f = open('input day 4.txt', 'r')
board = []
for line in f:
    board.append(list(line))  

i = 0
tot = 0
while i<4:
    tot += word_search(board)
    board = list(zip(*board[::-1]))
    i+=1

print(tot)
