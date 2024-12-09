##### Part 1 ##### 
from itertools import combinations

f = open('input day 8.txt', 'r')

def get_freq_points(board):
    freq_points = {}
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != '.':
                if freq_points.get(board[row][col]):
                    freq_points[board[row][col]].append([row, col])
                else:
                    freq_points[board[row][col]] = [[row,col]]
    return freq_points

def generate_pairs(board):
    freq_points = get_freq_points(board)
    freq_pairs = {}
    for key in freq_points.keys():
        freq_pairs[key] = list(combinations(freq_points[key], 2))
    return freq_pairs

def calculate_resonance_points(board):
    freq_pairs = generate_pairs(board)
    resonance_points = []
    for freq in freq_pairs.keys():
        for pair in freq_pairs[freq]:
            dist = []
            first_point = pair[0]
            second_point = pair[1]
            dist.append(second_point[0] - first_point[0])
            dist.append(second_point[1] - first_point[1])
            resonance_points.append([k + v for k,v in zip(second_point,dist)])
            resonance_points.append([k - v for k,v in zip(first_point,dist)])
    resonance_points = [rp for rp in resonance_points if rp[0] >= 0 and rp[0] < len(board) and rp[1] >= 0 and rp[1] < len(board[0])]
    num_of_unique_pts = 0
    for pt in resonance_points:
        if board[pt[0]][pt[1]] != '#':
            num_of_unique_pts += 1
            board[pt[0]][pt[1]] = '#'
    return num_of_unique_pts

board = []
for line in f:
    board.append(list(line.strip()))  
x = calculate_resonance_points(board)
print(x)

######### PART 2 #############

from itertools import combinations

f = open('input day 8.txt', 'r')

def get_freq_points(board):
    freq_points = {}
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != '.':
                if freq_points.get(board[row][col]):
                    freq_points[board[row][col]].append([row, col])
                else:
                    freq_points[board[row][col]] = [[row,col]]
    return freq_points

def generate_pairs(board):
    freq_points = get_freq_points(board)
    freq_pairs = {}
    for key in freq_points.keys():
        freq_pairs[key] = list(combinations(freq_points[key], 2))
    return freq_pairs

def calculate_resonance_points(board):
    freq_pairs = generate_pairs(board)
    freq_points = get_freq_points(board)
    resonance_points = []
    for freq in freq_pairs.keys():
        for pair in freq_pairs[freq]:
            dist = []
            first_point = pair[0]
            second_point = pair[1]
            dist.append(second_point[0] - first_point[0])
            dist.append(second_point[1] - first_point[1])
            new_pos_point = [k + v for k,v in zip(second_point,dist)]
            new_neg_point = [k - v for k,v in zip(first_point,dist)]
            while new_pos_point[0] >= 0 and new_pos_point[0] < len(board) and new_pos_point[1] >= 0 and new_pos_point[1] < len(board[0]):
                resonance_points.append(new_pos_point)
                new_pos_point = [k + v for k,v in zip(new_pos_point,dist)]
            while new_neg_point[0] >= 0 and new_neg_point[0] < len(board) and new_neg_point[1] >= 0 and new_neg_point[1] < len(board[0]):
                resonance_points.append(new_neg_point)
                new_neg_point = [k - v for k,v in zip(new_neg_point,dist)]
    resonance_points = [rp for rp in resonance_points if rp[0] >= 0 and rp[0] < len(board) and rp[1] >= 0 and rp[1] < len(board[0])]
    num_of_unique_pts = 0
    for pt in resonance_points:
        if board[pt[0]][pt[1]] == '.':
            num_of_unique_pts += 1
            board[pt[0]][pt[1]] = '#'

    for key in freq_points.keys():  
        num_of_unique_pts += len(freq_points[key]) if len(freq_points[key]) > 1 else 0
    return num_of_unique_pts

board = []
for line in f:
    board.append(list(line.strip()))  
x = calculate_resonance_points(board)
print(x)