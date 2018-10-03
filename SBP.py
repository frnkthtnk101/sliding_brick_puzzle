from read_file import get_file
from puzzle_pit import puzzle_pit
import argparse


def main(file_path):
    content = get_file(file_path)
    pit = puzzle_pit(content)
    if content is None:
        print("no good")
    else:         
        print(pit.to_string())
        print(pit.is_completed())
        print(pit.predict_moves(pit.clone()))


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("file", help ="file path of file", type = str)
    ARGS = PARSER.parse_args()
    main(ARGS.file)