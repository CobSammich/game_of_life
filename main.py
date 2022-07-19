"""
Driver for the

TODO:
* Read in file that defines the initial state
* Animate with matlpotlib or another framework?
* Function docstrings
"""
from board import board
import sys
import time
import random

BOARD_HEIGHT = 100
BOARD_WIDTH = 100
SAVE_IMAGES = True
N_GENERATIONS = 50


def main() -> None:
    game_board = board(BOARD_HEIGHT, BOARD_WIDTH)

    # Blinker
    # game_board.flip_cell(10, 10)
    # game_board.flip_cell(11, 10)
    # game_board.flip_cell(12, 10)

    # Beacon
    # game_board.flip_cell(0, 0)
    # game_board.flip_cell(1, 0)
    # game_board.flip_cell(0, 1)
    # game_board.flip_cell(1, 1)
    # game_board.flip_cell(2, 2)
    # game_board.flip_cell(3, 2)
    # game_board.flip_cell(2, 3)
    # game_board.flip_cell(3, 3)

    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            if random.randint(0, 2) == 2:
                game_board.flip_cell(row, col)

    game_board.show(save=SAVE_IMAGES)
    user_input = 'n'
    while user_input.lower() != 'y':
        user_input = input("Type 'y' to start simulation\n")


    while game_board.generation < N_GENERATIONS:
        #print("sleeping...")
        time.sleep(0.1)
        try:
            game_board.update()
            game_board.show(SAVE_IMAGES)
        except KeyboardInterrupt as _:
            game_board.clean_up()
            sys.exit()

if __name__ == "__main__":
    main()
