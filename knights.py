#!/usr/bin/env python3

case_amt = int(input())

def print_board(board):
    for line in board:
        print(line)

def test_position(board, move_to):
    # check for OOB
    if (move_to[0] > 4 or move_to[0] < 0 or 
        move_to[1] > 4 or move_to[1] < 0):
        return False

    if board[move_to[0]][move_to[1]] == 'k':
        return True
    else:
        return False

def gen_moves(position):
    moves = []
    moves.append((position[0] + 1, position[1] + 2))
    moves.append((position[0] + 1, position[1] - 2))
    moves.append((position[0] - 1, position[1] + 2))
    moves.append((position[0] - 1, position[1] - 2))

    moves.append((position[0] + 2, position[1] + 1))
    moves.append((position[0] + 2, position[1] - 1))
    moves.append((position[0] - 2, position[1] + 1))
    moves.append((position[0] - 2, position[1] - 1))
    return moves

for _ in range(case_amt):
    board_rows = []
    knight_positions = []
    for i in range(5):
        board_rows.append(list(input()))
        for j in range(5):
            if board_rows[i][j] == 'k':
                knight_positions.append((i, j))
    
    if len(knight_positions) != 9:
        print('invalid')
        continue

    valid = True

    for position in knight_positions:
        moves = gen_moves(position)
        for move in moves:
            if test_position(board_rows, move):
                valid = False
    if valid: 
        print('valid')
    else:
        print('invalid')
