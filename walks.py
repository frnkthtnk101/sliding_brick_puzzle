from puzzle_pit import puzzle_pit
from moving import predict_moves, biggest_bloc
from move import move
from state_comparison import normalize, compare
from copy import deepcopy
import random

def random_walk(content):
    pit = puzzle_pit(content)
    if content is None:
        print("no good")
    else:
        pit.matrix = normalize(pit.clone())
        while True:
            moves = predict_moves(pit.clone(),pit.height,pit.width,pit.to_string(False))
            random_number = random.randint(2,biggest_bloc(moves))
            for m in moves:
                if m.number == random_number:
                    if len(m.directions) > 0:
                        pick_direction = random.randint(0,len(m.directions)-1)
                        print("("+str(m.number) + "," + m.directions[pick_direction] + ")")
                        pit.apply_move(m.number,m.directions[pick_direction])
                        #print(pit.to_string(False))
                        if pit.is_completed():
                            print(pit.to_string())
                            return True
                    break

def breadth_search(content):
    pit = puzzle_pit(content)
    if content is None:
        print("no good")
    else:
        iterations = 0
        new_states = 0
        directions = list()
        directions_drag =list()
        fringe = list()
        states = list()
        past_states = list()
        pit.matrix = normalize(pit.clone())
        past_states.append(pit.to_string(False))
        for m in predict_moves(pit.clone(),pit.height,pit.width,pit.to_string(False)):
            for d in m.directions:
                fringe.append(m.number)
                directions.append(d)
                directions_list = list()
                directions_list.append('('+str(m.number)+','+str(d)+')')
                directions_drag.append(directions_list)
                states.append(deepcopy(pit.clone()))
        while len(fringe) > 0:
            temp_directions_drag = directions_drag.pop(0)
            temp_move = fringe.pop(0)
            temp_direction = directions.pop(0)
            pit.matrix = states.pop(0)
            temp_state = pit.apply_move_clone(temp_move, temp_direction)
            if pit.is_completed():
                print ('\n'.join(temp_directions_drag))
                print (pit.to_string())
                print ('iterations      : '+str(iterations))
                print ('new states found: '+str(new_states))
                break
            if pit.to_string(False) not in past_states:
                temp_directions_drag.append('('+str(m.number)+','+str(d)+')')
                for m in predict_moves(pit.clone(),pit.height,pit.width,pit.to_string(False)):
                    for d in m.directions:
                        fringe.append(m.number)
                        directions.append(d)
                        states.append(deepcopy(pit.clone()))
                        directions_drag.append(temp_directions_drag)
                past_states.append(pit.to_string(False))
                new_states +=1
            iterations += 1

def depth_search(content):
    pit = puzzle_pit(content)
    if content is None:
        print("no good")
    else:
        iterations = 0
        new_states = 0
        directions = list()
        directions_drag =list()
        fringe = list()
        states = list()
        past_states = list()
        pit.matrix = normalize(pit.clone())
        past_states.append(pit.to_string(False))
        for m in predict_moves(pit.clone(),pit.height,pit.width,pit.to_string(False)):
            for d in m.directions:
                fringe.append(m.number)
                directions.append(d)
                directions_list = list()
                directions_list.append('('+str(m.number)+','+str(d)+')')
                directions_drag.append(directions_list)
                states.append(deepcopy(pit.clone()))
        while len(fringe) > 0:
            temp_directions_drag = directions_drag.pop(-1)
            temp_move = fringe.pop(-1)
            temp_direction = directions.pop(-1)
            pit.matrix = states.pop(-1)
            temp_state = pit.apply_move_clone(temp_move, temp_direction)
            if pit.is_completed():
                print ('\n'.join(temp_directions_drag))
                print (pit.to_string())
                print ('iterations      : '+str(iterations))
                print ('new states found: '+str(new_states))
                break
            if pit.to_string(False) not in past_states:
                temp_directions_drag.append('('+str(m.number)+','+str(d)+')')
                for m in predict_moves(pit.clone(),pit.height,pit.width,pit.to_string(False)):
                    for d in m.directions:
                        fringe.append(m.number)
                        directions.append(d)
                        states.append(deepcopy(pit.clone()))
                        directions_drag.append(temp_directions_drag)
                past_states.append(pit.to_string(False))
                new_states +=1
            iterations += 1

