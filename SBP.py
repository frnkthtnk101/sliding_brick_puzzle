from read_file import get_file
from puzzle_pit import puzzle_pit
from moving import predict_moves
from move import move
import argparse


def main(file_path):
    content = get_file(file_path)
    pit = puzzle_pit(content)
    if content is None:
        print("no good")
    else:         
        print(pit.to_string())
        print(pit.is_completed())
        moves = predict_moves(pit.clone(), pit.height, pit.width, pit.to_string(False))
        pit.apply_move(2,"<")
        pit.apply_move(4,"v")
        pit.apply_move(3,">")
        pit.apply_move(2,"^")
        foo = pit.apply_move_clone(2,"^")
        print(foo)
        print(pit.is_completed())


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("file", help ="file path of file", type = str)
    ARGS = PARSER.parse_args()
    main(ARGS.file)