############## DAY 6 ##############

next_symbol = {
    '<':'^',
    '^':'>',
    '>':'v',
    'v':'<'
}

def compute_next_pos(symbol, row_index, col_index):
    next_pos = []
    if symbol == '<':
        next_pos = [row_index, col_index - 1]
    if symbol == '>':
        next_pos = [row_index, col_index + 1]
    if symbol == '^':
        next_pos = [row_index - 1, col_index]
    if symbol == 'v':
        next_pos = [row_index + 1, col_index]
    return next_pos

def get_starting_position(board):
    for row_index, row in enumerate(board):
        for col_index, value in enumerate(row):
            if value in next_symbol.keys():
                next_pos = compute_next_pos(value, row_index, col_index)
                return [row_index, col_index], next_pos

def guard_path(board):
    curr_pos, next_pos = get_starting_position(board)
    while (next_pos[0] not in [-1, len(board)]) and (next_pos[1] not in [-1, len(board[0])]):
        symbol = board[curr_pos[0]][curr_pos[1]]
        board[curr_pos[0]][curr_pos[1]] = 'X'
        curr_pos = next_pos
        next_pos = compute_next_pos(symbol, curr_pos[0], curr_pos[1])
        while (next_pos[0] not in [-1, len(board)]) and (next_pos[1] not in [-1, len(board[0])]) and board[next_pos[0]][next_pos[1]] == '#':
            symbol = next_symbol[symbol]
            next_pos = compute_next_pos(symbol, curr_pos[0], curr_pos[1])
        board[curr_pos[0]][curr_pos[1]] = symbol
    board[curr_pos[0]][curr_pos[1]] = 'X'
    return sum(1 for row in board for element in row if element == 'X')


f = open('input day 6.txt', 'r')
board = []
for line in f:
    board.append(list(line[:-1] if line[-1] == '\n' else line))  

print(guard_path(board))