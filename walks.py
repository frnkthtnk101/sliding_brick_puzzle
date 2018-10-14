'''
    walks.py
'''
import random
import time
from copy import deepcopy
from puzzle_pit import puzzle_pit
from moving import predict_moves, biggest_bloc
from state_comparison import normalize

def random_walk(content):
    '''
        random walk: picks a random block and random valid
        direction
    '''
    if content is None:
        raise Exception('the content given is no good')
    pit = puzzle_pit(content)
    pit.matrix = normalize(pit.clone())
    print(pit.to_string())
    while True:
        moves = predict_moves(pit.clone(), pit.height, pit.width, pit.to_string(False))
        random_number = random.randint(2, biggest_bloc(moves))
        for move_tuple in moves:
            if move_tuple.number == random_number:
                if move_tuple.directions:
                    pick_direction = random.randint(0, len(move_tuple.directions) - 1)
                    print("\n(" + str(move_tuple.number) + "," +\
                        move_tuple.directions[pick_direction]\
                    .replace('>', 'right').replace('<', 'left')\
                    .replace('^', 'up').replace('v', 'down') + ")\n")
                    pit.apply_move(move_tuple.number, move_tuple.directions[pick_direction])
                    print(pit.to_string())
                    if pit.is_completed():
                        return True
                break

def breadth_search(content):
    '''
        breadth search: goes through each level
    '''
    if content is None:
        raise Exception('the content given is no good')
    begining = time.time()
    pit = puzzle_pit(content)
    iterations = 0
    new_states = 0
    directions = list()
    directions_drag = list()
    fringe = list()
    states = list()
    past_states = list()
    pit.matrix = normalize(pit.clone())
    past_states.append(pit.to_string(False))
    for move_tuple in predict_moves(pit.clone(), pit.height, pit.width, pit.to_string(False)):
        for directions_tuple in move_tuple.directions:
            fringe.append(move_tuple.number)
            directions.append(directions_tuple)
            temp_drag = list()
            temp_drag.append('(' + str(move_tuple.number) + ',' + directions_tuple\
            .replace('>', 'right').replace('<', 'left')\
            .replace('^', 'up').replace('v', 'down') + ')')
            directions_drag.append(temp_drag)
            states.append(deepcopy(pit.clone()))
    while fringe:
        temp_directions_drag = directions_drag.pop(0)
        pit.matrix = states.pop(0)
        pit.apply_move(fringe.pop(0), directions.pop(0))
        if pit.is_completed():
            print('\n'.join(temp_directions_drag))
            print(pit.to_string())
            print(iterations, time.time() - begining, len(temp_directions_drag))
            break
        if pit.to_string(False) not in past_states:
            for move_tuple in predict_moves(pit.clone(), \
            pit.height, pit.width, pit.to_string(False)):
                for directions_tuple in move_tuple.directions:
                    copy_temp_directions_drag = deepcopy(temp_directions_drag)
                    fringe.append(move_tuple.number)
                    directions.append(directions_tuple)
                    states.append(deepcopy(pit.clone()))
                    copy_temp_directions_drag.append('(' + str(move_tuple.number) + ',' +\
                    directions_tuple.replace('>', 'right').replace('<', 'left')\
                    .replace('^', 'up').replace('v', 'down') + ')')
                    directions_drag.append(copy_temp_directions_drag)
            past_states.append(pit.to_string(False))
            new_states += 1
        iterations += 1

def depth_search(content):
    '''
        goes down the rabbit hole
    '''
    if content is None:
        raise Exception('the content given is no good')
    begining = time.time()
    pit = puzzle_pit(content)
    begining = time.time()
    iterations = 0
    new_states = 0
    directions = list()
    directions_drag = list()
    fringe = list()
    states = list()
    past_states = list()
    pit.matrix = normalize(pit.clone())
    past_states.append(pit.to_string(False))
    for move_tuple in predict_moves(pit.clone(), pit.height, pit.width, pit.to_string(False)):
        for directions_tuple in move_tuple.directions:
            fringe.append(move_tuple.number)
            directions.append(directions_tuple)
            temp_drag = list()
            temp_drag.append('(' + str(move_tuple.number) + ',' + \
            directions_tuple.replace('>', 'right')\
            .replace('<', 'left').replace('^', 'up')\
            .replace('v', 'down') + ')')
            directions_drag.append(temp_drag)
            states.append(deepcopy(pit.clone()))
    while fringe:
        temp_directions_drag = directions_drag.pop(-1)
        pit.matrix = states.pop(-1)
        pit.apply_move_clone(fringe.pop(-1), directions.pop(-1))
        if pit.is_completed():
            print('\n'.join(temp_directions_drag))
            print(pit.to_string())
            print(iterations, time.time()-begining, len(temp_directions_drag))
            break
        if pit.to_string(False) not in past_states:
            for move_tuple in predict_moves(pit.clone(), pit.height, \
            pit.width, pit.to_string(False)):
                for directions_tuple in move_tuple.directions:
                    copy_temp_directions_drag = deepcopy(temp_directions_drag)
                    fringe.append(move_tuple.number)
                    directions.append(directions_tuple)
                    states.append(deepcopy(pit.clone()))
                    copy_temp_directions_drag.append('(' + str(move_tuple.number) + ',' + directions_tuple\
                    .replace('>', 'right').replace('<', 'left').replace('^', 'up')\
                    .replace('v', 'down') + ')')
                    directions_drag.append(copy_temp_directions_drag)
            past_states.append(pit.to_string(False))
            new_states += 1
        iterations += 1

def iterative_search(content):
    '''
     an iterative walk
    '''
    begining = time.time()
    pit = puzzle_pit(content)
    if content is None:
        print("no good")
    else:
        iterations = 0
        new_states = 0
        directions = list()
        directions_drag = list()
        fringe = list()
        states = list()
        past_states = list()
        level_list = list()
        pit.matrix = normalize(pit.clone())
        past_states.append(pit.to_string(False))
        level = 0
        for move_tuple in predict_moves(pit.clone(), pit.height, pit.width, pit.to_string(False)):
            level_directions = 0
            for directions_tuple in move_tuple.directions:
                fringe.append(move_tuple.number)
                directions.append(directions_tuple)
                temp_drag = list()
                temp_drag.append('('+str(move_tuple.number)+','+str(directions_tuple)+')')
                directions_drag.append(temp_drag)
                states.append(deepcopy(pit.clone()))
                level_list.append([level, level_directions])
                level_directions += 1
        pointer = 0
        while fringe:
            move_on = True
            for i in range(0, len(level_list)):
                if level_list[i][0] == level + 1 and pointer == level_list[i][1]:
                    temp_directions_drag = directions_drag.pop(i)
                    temp_move = fringe.pop(i)
                    temp_direction = directions.pop(i)
                    pit.matrix = states.pop(i)
                    level_list.pop(i)
                    pointer += 1
                    move_on = False
                    break
            if move_on:
                level_list.pop(0)
                temp_directions_drag = directions_drag.pop(0)
                temp_move = fringe.pop(0)
                temp_direction = directions.pop(0)
                pit.matrix = states.pop(0)
                level += 1
                pointer = 0

            pit.apply_move_clone(temp_move, temp_direction)
            if pit.is_completed():
                print('\n'.join(temp_directions_drag))
                print(pit.to_string())
                print(iterations, time.time()-begining, len(temp_directions_drag))
                break
            if pit.to_string(False) not in past_states:
                for move_tuple in predict_moves(pit.clone(), pit.height, \
                pit.width, pit.to_string(False)):
                    level_directions = 0
                    for directions_tuple in move_tuple.directions:
                        copy_temp_directions_drag = deepcopy(temp_directions_drag)
                        fringe.append(move_tuple.number)
                        directions.append(directions_tuple)
                        states.append(deepcopy(pit.clone()))
                        copy_temp_directions_drag.append\
                        ('('+str(move_tuple.number)+','+str(directions_tuple)+')')
                        directions_drag.append(copy_temp_directions_drag)
                        level_list.append([level + 1, level_directions])
                        level_directions += 1
                past_states.append(pit.to_string(False))
                new_states += 1
            iterations += 1
            