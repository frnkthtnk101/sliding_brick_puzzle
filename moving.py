from block import block
from move import move
from copy import deepcopy

def predict_moves(copy_matrix, height, width, pit_string):
    blocks = get_blocks(copy_matrix, pit_string)
    moves = []
    for b in blocks:
        directions = [False,False,False,False] #<∨^>
        directions[0] = try_left(b, deepcopy(copy_matrix), height, width)
        directions[1] = try_down(b, deepcopy(copy_matrix), height, width)
        directions[2] = try_up(b, deepcopy(copy_matrix), height, width)
        directions[3] = try_right(b, deepcopy(copy_matrix), height, width)
        moves.append(move(b.number,directions))
    return moves

def in_range(x_axis, y_axis, width, height):
    return 0 <= x_axis <= width and 0 <= y_axis <= height

def try_left( block, matrix, height, width):
    for x in range(0,len(matrix)): 
        for y in range(0,len(matrix[0])):
            if matrix[x][y] == block.number and in_range(x,y-1, height, width):
                matrix[x][y-1] += block.number
                matrix[x][y] = 0
    return possible_move(matrix, block)

def try_down( block, matrix, height, width):
    for x in range(len(matrix) - 1, 0, -1): 
        for y in range(len(matrix[0]) - 1, 0, -1):
            if matrix[x][y] == block.number and in_range(x+1,y, height, width):
                matrix[x+1][y] += block.number
                matrix[x][y] = 0
    return possible_move(matrix, block)

def try_up(block, matrix, height, width):
    for x in range(0, len(matrix)): 
        for y in range(0, len(matrix[0])):
            if matrix[x][y] == block.number and in_range(x-1, y, height, width):
                matrix[x-1][y] += block.number
                matrix[x][y] = 0
    return possible_move(matrix, block)

def try_right(block, matrix, height, width):
    for x in range(len(matrix) - 1, 0, -1): 
        for y in range(len(matrix[0]) - 1, 0, -1):
            if matrix[x][y] == block.number and in_range(x, y + 1, height, width):
                matrix[x][y + 1] += block.number
                matrix[x][y] = 0
    return possible_move(matrix, block)

def possible_move(matrix, block):
    number_count = 0
    for row in matrix:
        for number in row:
            if block.number == number:
                number_count += 1
    return number_count == block.number_of_spots

def get_blocks(matrix, pit_string):
    blocks = []
    i = 2
    while str(i) in pit_string:
        j = 0
        for b in matrix:
            for d in b:
                if i == d:
                    j += 1
        blocks.append(block(j,i))
        i += 1
    return blocks