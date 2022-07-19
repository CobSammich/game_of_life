"""
Driver for the

TODO:
* Read in file that defines the initial state
* Function docstrings
* board has two instances known - no need to create a new large array every time
  (takes ~0.34 seconds before, 16.83 seconds for 50 generations) - this doesn't speed it up
* Animate with another framework?
"""
from board import board
import sys
import time
import random

BOARD_HEIGHT = 100
BOARD_WIDTH = 100
SAVE_IMAGES = False
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


    t0 = time.perf_counter()
    while game_board.generation < N_GENERATIONS:
        try:
            t0_0 = time.perf_counter()

            game_board.update()
            game_board.show(SAVE_IMAGES)

            t1_0 = time.perf_counter()
            print(f"Time for single generation: {t1_0 - t0_0:.5f}")
        except KeyboardInterrupt as _:
            game_board.clean_up()
            sys.exit()
    game_board.clean_up()
    t1 = time.perf_counter()
    print(f"Time for {game_board.generation} generations: {t1 - t0:.5f}")

if __name__ == "__main__":
    main()
