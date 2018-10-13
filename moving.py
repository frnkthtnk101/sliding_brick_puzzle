'''
    moving py: as set of funcitons that manipulate and predict
    movements for the walks
'''
from copy import deepcopy
from block import block
from move import move

def predict_moves(copy_matrix, height, width, pit_string):
    '''
        gets the moves that are currently available on the board
    '''
    blocks = get_blocks(copy_matrix, pit_string)
    moves = []
    for b_block in blocks:
        directions = [] #<∨^>
        if try_left(b_block, deepcopy(copy_matrix), height, width):
            directions.append('<')
        if try_down(b_block, deepcopy(copy_matrix), height, width):
            directions.append('v')
        if try_up(b_block, deepcopy(copy_matrix), height, width):
            directions.append('^')
        if try_right(b_block, deepcopy(copy_matrix), height, width):
            directions.append('>')
        moves.append(move(b_block.number, directions))
    return moves

def in_range(x_axis, y_axis, width, height):
    '''
        determines if the cordinates are in the proper range
    '''
    return 0 <= x_axis <= width and 0 <= y_axis <= height

def try_left(temp_block, matrix, height, width):
    '''
        check if we can move a block can move left
    '''
    for x_int in range(0, len(matrix)):
        for y_int in range(0, len(matrix[0])):
            if matrix[x_int][y_int] == temp_block.number and \
            in_range(x_int, y_int - 1, height, width):
                matrix[x_int][y_int - 1] += temp_block.number
                matrix[x_int][y_int] = 0
    return possible_move(matrix, temp_block, height, width)

def try_down(temp_block, matrix, height, width):
    '''
        check if we can move a block can move down
    '''
    for x_int in range(len(matrix) - 1, 0, -1):
        for y_int in range(len(matrix[0]) - 1, 0, -1):
            if matrix[x_int][y_int] == temp_block.number and \
            in_range(x_int + 1, y_int, height, width):
                matrix[x_int + 1][y_int] += temp_block.number
                matrix[x_int][y_int] = 0
    return possible_move(matrix, temp_block, height, width)

def try_up(temp_block, matrix, height, width):
    '''
        check if we can move a block up
    '''
    for x_int in range(0, len(matrix)):
        for y_int in range(0, len(matrix[0])):
            if matrix[x_int][y_int] == temp_block.number and \
            in_range(x_int - 1, y_int, height, width):
                matrix[x_int - 1][y_int] += temp_block.number
                matrix[x_int][y_int] = 0
    return possible_move(matrix, temp_block, height, width)

def try_right(temp_block, matrix, height, width):
    '''
        check if we can move a block can move right
    '''
    for x_int in range(len(matrix) - 1, 0, -1):
        for y_int in range(len(matrix[0]) - 1, 0, -1):
            if matrix[x_int][y_int] == temp_block.number and \
            in_range(x_int, y_int + 1, height, width):
                matrix[x_int][y_int + 1] += temp_block.number
                matrix[x_int][y_int] = 0
    return possible_move(matrix, temp_block, height, width)

def possible_move(matrix, temp_block, height, width):
    '''
        the function that sees if the move is allowed.
        under normal circumstances, the function iterates through the map
        to make sure the number of spots represented by that block's number
        are there. if the block is 2, it tries to see if the circumfrence
        of the map is completed. That is the wining move.

        for example
        5,4,
        1,-1,-1,1,1,
        1, 2, 2,4,1,
        1, 0, 0,0,1,
        1, 1, 1,1,1,

        becomes
        5,4,
        1,1,1,1,1,
        1,0,0,4,1,
        1,0,0,0,1,
        1,1,1,1,1,

        since the move is a two, it will first count the number of 1s on the
        map. then caculate the circumference if they are both the same, then
        it will return it as a valid move. if not, it will ultimately return
        invalid
    '''
    number_count = 0
    if temp_block.number == 2:
        for row in matrix:
            for number in row:
                if number == 1:
                    number_count += 1
        #subtract 4 because the corners are doubled
        if (2 * height + 2 * width) - 4 == number_count:
            return True
        number_count = 0
    for row in matrix:
        for number in row:
            if temp_block.number == number:
                number_count += 1
    return number_count == temp_block.number_of_spots

def get_blocks(matrix, pit_string):
    '''
        creates the blocks list. it will iterate
        through a copy of the map and tell the parent
        fucntion how many blocks there are
    '''
    blocks = []
    i = 2
    while str(i) in pit_string:
        j = 0
        for row in matrix:
            for attribute in row:
                if i == attribute:
                    j += 1
        blocks.append(block(j, i))
        i += 1
    return blocks

def biggest_bloc(moves):
    '''
        tells the program what block number
        is the biggest block
    '''
    biggest_number = 3
    for this_move in moves:
        if this_move.number > biggest_number:
            biggest_number = this_move.number
    return biggest_number
