from read_file import get_file
from walks import *
import argparse


def main(levels_directory):
    random_walk(get_file(levels_directory+'SBP-level0.txt'))


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("levels_directory", help ="file path of file", type = str)
    ARGS = PARSER.parse_args()
    main(ARGS.levels_directory)