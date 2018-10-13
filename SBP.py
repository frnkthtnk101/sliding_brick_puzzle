from read_file import get_file
from walks import *
import argparse


def main(file_path, walk):
    if walk == 'random':
        random_walk(get_file(file_path))
    elif walk == 'breadth':
        breadth_search(get_file(file_path))
    elif walk == 'depth':
        depth_search(get_file(file_path))
    elif walk == 'iterative':
        iterative_search(get_file(file_path))


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("file", help ="file path of file", type = str)
    PARSER.add_argument("walk", help ="what kind of walk would you like to do? random")
    ARGS = PARSER.parse_args()
    main(ARGS.file, ARGS.walk)