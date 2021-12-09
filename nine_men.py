import time
import sys

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
a_to_i = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7}
i_to_a = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G'}

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
OTHER = {MY_SIDE: ENEMY_SIDE, ENEMY_SIDE: MY_SIDE}
DISPLAY_BOARD = {MY_SIDE: 'X', ENEMY_SIDE: 'O', EMPTY: '.'}

MY_DEPTH = 3
OTHER_DEPTH = 3
MAX_DEPTH = {
    MY_SIDE: MY_DEPTH,
    ENEMY_SIDE: OTHER_DEPTH
}
CULL = 6
TIME_LIMIT = 0.035

weight_links = 0
weight_friendly_neighbors = 1.0
weight_enemy_neighbors = -.5
weight_mills = 1.0

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
    score = count_side(board, side)

    for cell in board:
        if board[cell] == side:
            score += len(cells[cell]) * weight_links
            score += get_neighbors(board, cell, side) * weight_friendly_neighbors
            score += get_neighbors(board, cell, OTHER[side]) * weight_enemy_neighbors

    # calc connected mills
    for m in mills:
        if board[m[0]] == side and board[m[1]] == side and board[m[2]] == side:
            score += weight_mills

    return score


# Print the board
def print_board(board):
    print('  A B C D E F G')
    for b in range(7, 0, -1):
        print(b, end=' ')
        for a in range(1, 8):
            cell = i_to_a[a] + str(b)
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
    for cell in board: new_board[cell] = board[cell]  # copy the board
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
                    takes.append(neighbor)
                    break
    return takes


# Find all valid from cells
def get_occupied_cells(board, side, empty_neighbors_only=True):
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
    potential_takes = get_takes(board, side)

    if hopper > 0:
        moves = []
        for place_to in board:
            if board[place_to] == EMPTY:
                if check_move_is_mill(board, side, place_to, place_to):
                    for take in potential_takes:
                        moves.append('PLACE&TAKE;' + place_to + ';' + take)
                else:
                    moves.append('PLACE;' + place_to)
        return moves

    if count_side(board, side) <= 3:
        moves = []
        occupied_cells = get_occupied_cells(board, side, False)  # all not just with empty neighbors
        for move_from in board:
            if board[move_from] == side:
                for move_to in occupied_cells:
                    moves.append('MOVE;' + move_to + ";" + move_from)
        return moves

    moves = []
    occupied_cells = get_occupied_cells(board, side)  # just those with empty neighbors
    for move_from in occupied_cells:
        for move_to in cells[move_from]:
            if board[move_to] == EMPTY:
                if check_move_is_mill(board, side, move_from, move_to):
                    for take in potential_takes:
                        moves.append('MOVE&TAKE;' + move_from + ";" + move_to + ";" + take)
                else:
                    moves.append('MOVE;' + move_from + ";" + move_to)
    return moves


def apply_move(board, side, move):
    new_board = {}
    for cell in board: new_board[cell] = board[cell]  # copy the board
    action = move.split(';')
    # print(move, action, parts)
    if action[0] == 'PLACE':
        new_board[action[1]] = side
    elif action[0] == 'PLACE&TAKE':
        new_board[action[1]] = side
        new_board[action[2]] = EMPTY
    elif action[0] == 'MOVE':
        new_board[action[2]] = side
        new_board[action[1]] = EMPTY
    elif action[0] == 'MOVE&TAKE':
        new_board[action[2]] = side
        new_board[action[1]] = EMPTY
        new_board[action[3]] = EMPTY
    return new_board


def score_moves(board, side, moves):
    scores = {}
    for move in moves:
        new_board = apply_move(board, side, move)
        scores[move] = score_board(new_board, side)
    return scores


def filter_scores(scores, cull):
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_scores[:cull]


def get_move(depth, cull, board, side, hopper, other_hopper, total_tries, start_ms):
    moves = get_moves(board, side, hopper)
    return get_next_move(depth, cull, board, side, moves, hopper, other_hopper, total_tries, start_ms)


def get_next_move(depth, cull, board, side, moves, hopper, other_hopper, total_tries, start_ms):
    if len(moves) == 0:
        print("End found no moves for side", side, depth, file=sys.stderr, flush=True)
        return ('endgame;', -100), total_tries  # this is a lose scenario

    scores = score_moves(board, side, moves)
    best = filter_scores(scores, cull)

    total_tries += len(moves)

    # done at DEPTH or if we reach the TIME_LIMIT
    if depth == MAX_DEPTH[side]:
        #print("Depth Limit reached", depth, MAX_DEPTH[side], file=sys.stderr, flush=True)
        return best[0], total_tries
    if time.perf_counter() - start_ms > TIME_LIMIT:
        #print("Time Limit reached", file=sys.stderr, flush=True)
        return best[0], total_tries

    scores = {}
    # Iterate depth on the culled best moves
    for b in best:
        new_board = apply_move(board, side, b[0])  # Apply the move
        if 'PLACE' in b:
            new_hopper = hopper - 1
        else:
            new_hopper = hopper

        # Get next move for opponent
        other_move, total_tries = get_move(depth + 1, cull, new_board, OTHER[side], other_hopper, new_hopper,
                                           total_tries, start_ms)
        if 'PLACE' in other_move[0]:
            new_other_hopper = other_hopper - 1
        else:
            new_other_hopper = other_hopper

        new_board = apply_move(board, OTHER[side], other_move[0])  # Apply the best opponent move

        # recurse down
        next, total_tries = get_move(depth + 1, cull, new_board, side, new_hopper, new_other_hopper, total_tries,
                                     start_ms)
        scores[b[0]] = next[1]

    if depth == 0:
        print("After sim: depth=", depth, "tries=", total_tries, "scores=", scores, file=sys.stderr, flush=True)
    best = filter_scores(scores, 1)
    # print("Best", best)
    return best[0], total_tries  # return the best move


def run_game():
    board = clear_board()
    my_hopper = 9
    enemy_hopper = 9
    turn = 0

    while (turn < 200):
        depth = 0
        print('Turn:', turn)
        print('My hopper:', my_hopper)
        print('Enemy hopper:', enemy_hopper)
        turn += 1

        start_ms = time.perf_counter()
        move, tries = get_move(depth, CULL, board, MY_SIDE, my_hopper, enemy_hopper, 0, start_ms)
        print("move=", move, "tries=", tries, "time=" + str(time.perf_counter() - start_ms))
        if "end" in move[0]:
            print("I lose - no moves")
            return

        board = apply_move(board, MY_SIDE, move[0])
        if 'PLACE' in move[0]:
            my_hopper -= 1
        print_board(board)

        move, tries = get_move(depth, CULL, board, OTHER[MY_SIDE], enemy_hopper, my_hopper, 0, time.perf_counter())
        print("other_move=", move, "tries=", tries, "time=" + str(time.perf_counter() - start_ms))
        if "end" in move[0]:
            print("I win - no moves")
            return

        board = apply_move(board, OTHER[MY_SIDE], move[0])
        if 'PLACE' in move[0]:
            enemy_hopper -= 1
        print_board(board)

        if my_hopper == 0 and check_win(board, MY_SIDE):
            print("I win")
            return
        elif enemy_hopper == 0 and check_win(board, ENEMY_SIDE):
            print("I Lose")
            return


def online_loop():
    player_id = int(input())  # playerId (0,1)
    fields = int(input())  # number of fields
    for i in range(fields):
        neighbors = input()  # neighbors of a field (ex: A1:A4;D1)

    # game loop
    turn = 0
    while True:
        op_move = input()  # The last move executed from the opponent

        board = {}
        board_line = input()  # Current Board and state(0:Player0 | 1:Player1 | 2:Empty) in format field:state and separated by ;
        parts = board_line.split(';')
        for part in parts:
            pieces = part.split(':')
            board[pieces[0]] = int(pieces[1])
        print(board, file=sys.stderr, flush=True)

        nbr = int(input())  # Number of valid moves proposed.
        # print('moves', nbr, file=sys.stderr, flush=True)
        commands = []
        for i in range(nbr):
            commands.append(input())  # An executable command line
            # print(i, commands[i], file=sys.stderr, flush=True)
        print(i, commands, file=sys.stderr, flush=True)

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)
        hopper = 0
        if turn < 9:
            hopper =  9 - turn
        start_ms = time.perf_counter()
        move, tries = get_next_move(0, CULL, board, player_id, commands, hopper, hopper, 0, start_ms)
        print("My Move: ", move, "tries=", tries, "time=", time.perf_counter() - start_ms, file=sys.stderr, flush=True)
        print(move[0])


online_loop()
