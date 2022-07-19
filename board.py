
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
plt.ion()

import numpy as np
import os
import ipdb

class board:

    def __init__(self, width: int, height: int) -> None:
        self.height = height
        self.width = width
        self.board = np.zeros((self.height, self.width), dtype=bool)
        # two instances - so we don't need to create a new matrix every update
        self.generation = 0

        # Matplotlib specific fields
        self.fig = plt.figure(figsize=(12,8))
        self.ax = self.fig.add_subplot()
        # This is set in the show call
        self.imshow = None
        self.initialize_plot()
        os.makedirs("./images", exist_ok=True)

    def __str__(self) -> str:
        # TODO: print the game board
        pass

    def initialize_plot(self) -> None:
        xticks = np.arange(0, self.width  + 1) - 0.5
        yticks = np.arange(0, self.height + 1) - 0.5
        self.ax.grid(alpha=0.5)
        self.ax.set_xticks(xticks)
        self.ax.set_yticks(yticks)
        self.ax.axes.xaxis.set_ticklabels([])
        self.ax.axes.yaxis.set_ticklabels([])
        self.ax.tick_params(axis='y', colors='white')
        self.ax.tick_params(axis='x', colors='white')
        self.fig.tight_layout(rect=[0, 0.03, 1, 0.95])


    def show(self, save: bool = False) -> None:
        if self.imshow is None:
            self.imshow = self.ax.imshow(self.board, cmap="gray_r")
        else:
            self.imshow.set_data(self.board)
        self.fig.suptitle(f"Gen #: {self.generation}", fontsize=20)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        if save:
            self.fig.savefig(f"./images/{self.generation:03d}.pdf")


    def update(self) -> None:
        # Update each cell
        buff = np.array([self.update_cell(col, row)
                            for row in range(self.height)
                            for col in range(self.width)]
                       ).reshape(self.height, self.width)
        self.board = np.array(buff).reshape(self.height, self.width)
        self.generation += 1


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

    def clean_up(self) -> None:
        plt.close(self.fig)
