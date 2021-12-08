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

mills = (
    ['A1', 'A4', 'A7'],
    ['B2', 'B4', 'B6'],
    ['C3', 'C4', 'C5'],
    ['D1', 'D2', 'D3'],
    ['E3', 'E4', 'E5'],
    ['F2', 'F4', 'F6'],
    ['G1', 'G4', 'G7'],
    ['D5', 'D6', 'D7'],
    ['A1', 'D1', 'G1'],
    ['B2', 'D2', 'F2'],
    ['C3', 'D3', 'E3'],
    ['A4', 'B4', 'C4'],
    ['E4', 'F4', 'G4'],
    ['C5', 'D5', 'E5'],
    ['B6', 'D6', 'F6'],
    ['A7', 'D7', 'G7'] 
)


MY_SIDE = 0
ENEMY_SIDE = 1
EMPTY = 2
OTHER = { MY_SIDE: ENEMY_SIDE, ENEMY_SIDE: MY_SIDE }

DISPLAY_BOARD = {MY_SIDE:'X', ENEMY_SIDE:'O', EMPTY:'.'}

weight_links = 1
weight_friendly_neighbors = 1
weight_enemy_neighbors = 1

# setup an empty board
def clear_board():
    board = {}
    for cell in cells:
        board[cell] = EMPTY
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
        score += get_neighbors(board, cell, OTHER[side]) * weight_enemy_neighbors
        
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

# check if won by virtue of oppening having only 2 pieces
def check_win(board, side):
    return count_side(board, OTHER[side]) <= 2

# Count side pieces on the board
def count_side(board, side):
    count = 0
    for cell in board:
        if board[cell] == side:
            count += 1
    return count


# check if move completes a line
def check_move_is_mill(board, side, from_cell, to_cell):
    new_board = {}
    for cell in board: new_board[cell] = board[cell] # copy the board
    new_board[from_cell] = EMPTY
    new_board[to_cell] = side
    for m in mills:
        if to_cell in m:
            cnt = 0
            for c in m:
                if new_board[c] == side:
                    cnt += 1
            if cnt == 3:
                return True
    return False

# get potential takes
def get_takes(board, side):
    takes = []
    for cell in board:
        if board[cell] == side:
            for neighbor in cells[cell]:
                if board[neighbor] == OTHER[side]:
                    takes.append(cell)
                    break
    return takes

# Find all valid from cells
def get_occupied_cells(board, side, empty_neighbors_only = True):
    occupied_cells = []
    for cell in board:
        if board[cell] == side:
            if empty_neighbors_only:
                for neighbor in cells[cell]:
                    if board[neighbor] == EMPTY:
                        occupied_cells.append(cell)
                        break
            else:
                occupied_cells.append(cell)
    return occupied_cells

def get_moves(board, side, hopper):
    if hopper > 0:
        moves = []
        for cell in board:
            if board[cell] == EMPTY:
                moves.append('PLACE;' + cell)
        return moves

    if count_side(board, side) <= 3:
        moves = []
        occupied_cells = get_occupied_cells(board, side, False)  # all not just with empty neighbors
        for cell in board:
            if board[cell] == side:
                for f in occupied_cells:
                    moves.append('MOVE;' + f + "," + cell)
        return moves

    moves = []
    potential_takes = get_takes(board, side)
    occupied_cells = get_occupied_cells(board, side) # just those with empty neighbors
    for cell in board:
        if board[cell] == side:
            for f in cells[cell]:
                if board[f] == EMPTY:
                    if check_move_is_mill(board, side, cell, f):
                        for take in potential_takes:
                            moves.append('MOVE&TAKE;' + f + "," + cell + "," + take)
                    else:
                        moves.append('MOVE;' + f + "," + cell)
                    moves.append('MOVE;' + cell + "," + f)
    return moves

def score_moves(board, side, moves):
    scores = {}
    for move in moves:
        new_board = {}
        for cell in board: new_board[cell] = board[cell] # copy the board
        scores[move] = score_board(new_board, side)
    return scores

board = clear_board()
my_hopper = 9
enemy_hopper = 9
move = 0

while(move < 1):
    print_board(board)
    print('Move:', move)
    print('My hopper:', my_hopper)
    print('Enemy hopper:', enemy_hopper)
    move += 1

    moves = get_moves(board, MY_SIDE, my_hopper)
    print(moves)
    scores = score_moves(board, MY_SIDE, moves)

