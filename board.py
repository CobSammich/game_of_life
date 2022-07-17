import numpy as np
import matplotlib.pyplot as plt
import ipdb

class board:

    def __init__(self, width: int, height: int) -> None:
        self.height = height
        self.width = width
        self.board = np.zeros((self.height, self.width), dtype=bool)

    def __str__(self) -> str:
        pass

    def show(self) -> None:
        fig, ax = plt.subplots()
        xticks = np.arange(0, self.width  + 1) - 0.5
        yticks = np.arange(0, self.height + 1) - 0.5
        ax.imshow(self.board, cmap="gray")
        ax.grid()
        ax.set_xticks(xticks)
        ax.set_yticks(yticks)
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])
        plt.show()
        plt.close(fig)

    def update(self) -> None:
        new_board = np.zeros((self.height, self.width), dtype=bool)
        for row in range(self.height):
            for col in range(self.width):
                new_board[row, col] = self.update_cell(col, row)
        self.board = new_board

    def update_cell(self, x: int, y: int) -> bool:
        live_cell = self.board[y, x]
        n_live_neighbors = self.get_neighbors(x, y)

        # Any live cell with two or three live neighbours survives.
        if live_cell and n_live_neighbors in [2, 3]:
            return live_cell

        # Any dead cell with three live neighbours becomes a live cell.
        if not live_cell and n_live_neighbors == 3:
            return self.get_reversed_state(x, y)

        # All other live cells die in the next generation. Similarly, all other dead cells
        # stay dead.
        if live_cell:
            return self.get_reversed_state(x, y)
        # At this point all other cells are dead
        return live_cell


    def get_neighbors(self, x: int, y: int) -> int:
        # Returns the number of live cells
        y_lower_bound, y_upper_bound = np.clip([y - 1, y + 2], a_min=0, a_max=self.height)
        x_lower_bound, x_upper_bound = np.clip([x - 1, x + 2], a_min=0, a_max=self.width)

        neighbors = self.board[y_lower_bound: y_upper_bound, x_lower_bound: x_upper_bound]

        n_live = np.sum(neighbors)
        # If this cell is live, let's subtract one from the count
        if self.board[y, x]:
            return n_live - 1
        return np.sum(neighbors)

    def flip_cell(self, x: int, y: int) -> bool:
        """
        Reverses the current state of the cell

        Parameters
        ----------
        x : int
            x position of cell
        y : int
            y position of cell

        Returns
        -------
        bool
            The new value of the cell
        """
        self.board[y, x] = not self.board[y, x]
        return self.board[y, x]

    def get_reversed_state(self, x: int, y: int) -> bool:
        return not self.board[y, x]
