from read_file import get_file
from puzzle_pit import puzzle_pit
from moving import predict_moves
from move import move
from state_comparison import normalize
import argparse


def main(file_path, walk):
    content = get_file(file_path)
    pit = puzzle_pit(content)
    if content is None:
        print("no good")
    else:         
        print(normalize(pit.clone()))


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("file", help ="file path of file", type = str)
    PARSER.add_argument("walk", help ="what kind of walk would you like to do? random")
    ARGS = PARSER.parse_args()
    main(ARGS.file, ARGS.walk)