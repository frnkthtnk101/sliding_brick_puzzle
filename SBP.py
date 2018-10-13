from read_file import get_file
from walks import *
import argparse


def main():
    random_walk(get_file('SBP-level0.txt'))
    breadth_search(get_file('SBP-level1.txt'))
    depth_search(get_file('SBP-level1.txt'))
    iterative_search(get_file('SBP-level1.txt'))

main()
'''if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("levels_directory", help ="file path of file", type = str)
    ARGS = PARSER.parse_args()
    main(ARGS.levels_directory)'''