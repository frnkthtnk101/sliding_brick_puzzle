from puzzle_pit import puzzle_pit
from moving import predict_moves, biggest_bloc
from move import move
from state_comparison import normalize
import random

def random_walk(content):
    pit = puzzle_pit(content)
    if content is None:
        print("no good")
    else:
        pit.matrix = normalize(pit.clone())
        current_fringe = 0
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