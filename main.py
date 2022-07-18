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

BOARD_HEIGHT = 20
BOARD_WIDTH = 20


def main() -> None:
    game_board = board(BOARD_HEIGHT, BOARD_WIDTH)

    # Blinker
    game_board.flip_cell(10, 10)
    game_board.flip_cell(11, 10)
    game_board.flip_cell(12, 10)

    # Beacon
    game_board.flip_cell(0, 0)
    game_board.flip_cell(1, 0)
    game_board.flip_cell(0, 1)
    game_board.flip_cell(1, 1)
    game_board.flip_cell(2, 2)
    game_board.flip_cell(3, 2)
    game_board.flip_cell(2, 3)
    game_board.flip_cell(3, 3)

    while True:
        print("sleeping...")
        time.sleep(0.5)
        try:
            game_board.show()
            game_board.update()
        except KeyboardInterrupt as e:
            game_board.clean_up()
            sys.exit()

if __name__ == "__main__":
    main()
