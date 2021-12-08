import time
cells = {
    'A1': ['A4', 'D1'],
    'A4': ['A1', 'A7', 'B4'],
    'A7': ['A4', 'D7'],
    'B2': ['B4', 'D2'],
    'B4': ['B2', 'B6', 'A4', 'C4'],
    'B6': ['B4', 'D6'],
    'C3': ['C4', 'D3'],
    'C4': ['B4', 'C3', 'C5'],
    'C5': ['C4', 'D5'],
    'D1': ['A1', 'G1', 'D2'],
    'D2': ['B2', 'F2', 'D3', 'D1'],
    'D3': ['C3', 'D2', 'E3'],
    'D5': ['C5', 'D6', 'E5'],
    'D6': ['B6', 'F6', 'D5', 'D7'],
    'D7': ['A7', 'G7'],
    'E3': ['D3', 'E4'],
    'E4': ['E3', 'E5', 'F4'],
    'E5': ['D5', 'E4'],
    'F2': ['D2', 'F4'],
    'F4': ['F2', 'F6', 'E4', 'G4'],
    'F6': ['D6', 'F4'],
    'G1': ['D1', 'G4'],
    'G4': ['G1', 'G7', 'F4'],
    'G7': ['D7', 'G4']
}
a_to_i = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7}
i_to_a = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G'}


MY_SIDE = 1
ENEMY_SIDE = -MY_SIDE
DISPLAY_BOARD = {MY_SIDE:'X', ENEMY_SIDE:'O', 0:'.'}

weight_links = 1
weight_friendly_neighbors = 1
weight_enemy_neighbors = 1

# setup an empty board
def clear_board():
    board = {}
    for cell in cells:
        board[cell] = 0
    return board

# count neighbors of cell occupied by side
def get_neighbors(board, cell, side):
    neighbors = 0
    for neighbor in cells[cell]:
        if board[neighbor] == side:
            neighbors += 1
    return neighbors

# score a board
def score_board(board, side):
    score = 0
    for cell in board:
        if board[cell] == side:
            score += len(cells[cell]) * weight_links

        score += get_neighbors(board, cell, side) * weight_friendly_neighbors
        score += get_neighbors(board, cell, -side) * weight_enemy_neighbors
        
    return score

# Print the board
def print_board(board):
    for a in range(1,8):
        for b in range(1,8):
            cell = i_to_a[a]+str(b)
            if cell in board:
                print(DISPLAY_BOARD[board[cell]], end=' ')
            else:
                print(' ', end=' ')

        print()

board = clear_board()
my_hopper = 9
enemy_hopper = 9

print_board(board)
