                                                                                             
    _                                                                                      _   
  _| |_ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ __________ _| |_ 
 |_   _|______|______|______|______|______|______|______|______|______|______|__________|_   _|
   |_|_____ _ _     _ _               ____       _      _      _____               _      |_|  
   | |/ ____| (_)   | (_)             |  _ \     (_)    | |    |  __ \             | |    | | 
   | | (___ | |_  __| |_ _ __   __ _  | |_) |_ __ _  ___| | __ | |__) |   _ _______| | ___| | 
   | |\___ \| | |/ _` | | '_ \ / _` | |  _ <| '__| |/ __| |/ / |  ___/ | | |_  /_  / |/ _ \ | 
   | |____) | | | (_| | | | | | (_| | | |_) | |  | | (__|   <  | |   | |_| |/ / / /| |  __/ | 
   | |_____/|_|_|\__,_|_|_| |_|\__, | |____/|_|  |_|\___|_|\_\ |_|    \__,_/___/___|_|\___| | 
   | |                          __/ |                                                     | | 
   |_|                         |___/                                                      |_| 
  _| |_ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ___ _| |_ 
 |_   _|______|______|______|______|______|______|______|______|______|______|______|___|_   _|
   |_|                                                                                    |_|  
                                                                                             
                                                                                             
 Created by Franco Pettigrosso
 for CS-510-900
 created in a virtual python environment version 3.3

Table of contents
1) Goal
2) Rules of the game
3) Scripts
4) Assignments requirements

Goal
    The goal of this program is to create a puzzle game that a computer can solve.

Rules
    the goal of the game is to get a disignated block (goal bock), labeled 2, into the goal, labeled -1.
    There is a map with a specific height and width. This map can contain walls, a goal, a goal block,
    and other blocks. All blocks are allowed to go up, down, left, and right. All blocks cannot go through
    walls and other blocks. Normal blocks are not allowed to go through the goal. The goal block is the
    only block allowed to go through the goal.

    Rules of the map
    The map needs to meet the following requirements to be process by the machine.
    - .txt file only.
    - the map needs to be in this format (W = Width, H = Height, M = Map).
    W,H,
    M,M,M,M,
    M,M,M,M,
    M,M,M,M,
    - The map needs a goal block and goal. Smallest map possible is 1,2 or 2,1.

scripts


Assignments and requirements
    Assignement 1 
    P1
        1) Create the ground work for the Sliding Brick Puzzle.
        2) State Representation: The program needs to read a file and outputs the game state
        to the terminal. The program needs to clones as state. The clone state needs to return
        the state of the game identical to the current instance. [done]
        3) Puzzle Complete Check: the program needs to check if the puzzle is solved. [done]
        4) Move Generation: The Program needs the ability to move blocks.
            -The program needs to return all available moves that one piece can perform [done]
            -The program needs to return all abailable moves that can happen on the board [done]
            -ApplyMove() performs the move given the state of the board [done]
            -ApplyuMoveCloning() clones the state of the map and then applies the move [done]
        5) State Comparison: the program needs to compare the state of machine to the previous
            state. [done]
        6) Normalization: follow pdf [done]
        7) Random Walks: the program needs to do
            -generate all moves that can be executed on the board in its current state.
            -select one at random.
            -execute the path.
            -normalizes the cosequences of that action to the state
            -see if it reached the goal
    P2
        - write a function that solves SBP using a breadth-first search.
        - write a function that solves SBP using a depth-first search.
        - write a function that solves SBP using a iterative deepenign search.
        - the main fucniton will call these function to accomplish
            -load SBP-level0.txt and execute a rando walk
            -load SBP-Level1.txt and execute breadth-first search
            -load SBP-Level1.txt and execute depth-first search
            -load SBP-Level1.txt and execute iterative-deepening search
        - EXTRA CREDIT A * search
