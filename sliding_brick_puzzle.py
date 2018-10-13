'''
    The main function: SBP will read files into the walk.
'''
from read_file import get_file
from walks import random_walk, breadth_search, depth_search, iterative_search

def main():
    '''
        main function
    '''
    random_walk(get_file('SBP-level0.txt'))
    breadth_search(get_file('SBP-level1.txt'))
    depth_search(get_file('SBP-level1.txt'))
    iterative_search(get_file('SBP-level1.txt'))

main()
