"""First Milestone, create a function called random state"""

from pprint import pprint
import numpy as np


# Creates the starting board game state.

def random_state(board_height, board_width):
    """Creates an array [m][n] dimension array, randomized with 0 or 1.
    Returns the array as a python list."""

    board_state = np.random.randint(2, size=(board_height, board_width))

    board_state_list = board_state.tolist()
    return board_state_list


def render(board_state):
    """"Prints the list in an [m][n] array format"""
    pprint(board_state)

"""must follow these rules:
Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation.
Any live cell with 2 or 3 live neighbors stays alives, because its neighborhood is just right.
Any live cell with more than 3 live neighbors becomes dead, because of overpopulation.
Any dead cell with exactly 3 live neighbors beceoms alive, by reproduction."""

def next_board_state(board_state):
    #TODO: make a copy of the board_state set to zero
    next_board = [[0]*10]*10
    #TODO: take the value at the first index, and compare it with values around it
    cur_index = board_state[0][0]
    neighbor_right = board_state[0][0+1]

    if cur_index == neighbor_right:
        print('MATCH')
    else:
        print('No Match')
    return next_board




