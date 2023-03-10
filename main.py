import matplotlib.pyplot as plt
import numpy as np

from cell_types import *
from rules import *


class Board:

    def __init__(self, board_size):
        """
        Init
        """

        self.board_size = board_size
        self.board = []

        self.max_x = board_size
        self.min_x = 0
        self.max_y = board_size
        self.min_y = 0

        cell_no = 0
        for i in range(board_size):
            cur_row = []
            for j in range(board_size):
                cur_cell = Water(cell_no, i, j)
                cell_no += 1
                cur_row.append(cur_cell)
            self.board.append(cur_row)

    def get_board(self):
        """
        Get board
        """

        return self.board

    def get_surrounding_cells(self, cur_x, cur_y):
        """
        Get Surround Cells on your baord

        xxx
        xox
        xxx
        """

        # Left
        surroundings = {
            'top_left': None,
            'top': None,
            'top_right': None,
            'left': None,
            'right': None,
            'bottom_left': None,
            'bottom': None,
            'bottom_right': None,
        }

        # Top left
        if cur_x - 1 >= self.min_x and cur_y + 1 >= self.min_y:
            surroundings['top_left'] = self.board[cur_x-1][cur_y+1]

        # Top
        if cur_y + 1 >= self.min_y:
            surroundings['top'] = self.board[cur_x-1][cur_y+1]

        # Top Right
        if cur_y + 1 >= self.min_y and cur_x + 1 < self.max_x:
            surroundings['top_right'] = self.board[cur_x-1][cur_y+1]

        # Left
        if cur_x - 1 >= self.min_x:
            surroundings['left'] = self.board[cur_x-1][cur_y]

        # Right
        if cur_x +1 < self.max_x:
            surroundings['right'] = self.board[cur_x+1][cur_y]

        # Bottom left
        if cur_y + 1 < self.max_y and cur_x - 1 >= self.min_x:
            surroundings['bottom_left'] = self.board[cur_x-1][cur_y+1]

        # Bottom
        if cur_y + 1 < self.max_y:
            surroundings['bottom'] = self.board[cur_x][cur_y+1]

        # Bottom Right
        if cur_y + 1 < self.max_y and cur_x +1 < self.max_x:
            surroundings['bottom_right'] = self.board[cur_x+1][cur_y+1]

        return surroundings


    def get_image(self):
        """
        Get image
        """

        cur_img = []
        cur_img_alpha = []
        for cur_row in self.board:
            tmp_row = []
            tmp_row_alpha = []
            for cur_cell in cur_row:
                tmp_row.append(cur_cell.color)
                tmp_row_alpha.append(cur_cell.alpha)

            cur_img.append(tmp_row)
            cur_img_alpha.append(tmp_row_alpha)

        return cur_img, cur_img_alpha



class Simulation:

    """
    Simulation
    """

    def __init__(self, board_size=10, rules=[]):
        """
        Init
        """

        self.board = Board(board_size)
        self.rules = rules

        self.next_board = None

    def introduce_cell(self, Cell):

        x_pos = Cell.x
        y_pos = Cell.y
        cur_cell_no = self.board.board[x_pos][y_pos].cell_no

        Cell.cell_no = cur_cell_no
        self.board.board[x_pos][y_pos] = Cell


    def time_step(self, time):
        """
        Runs Simulation in a single time step
        """

        # cur_board = self.board

        self.next_board = self.board

        cur_row = 0
        while cur_row < self.board.max_y:
            cur_col = 0
            while cur_col < self.board.max_x:
                self.apply_rules(cur_row, cur_col)
                cur_col += 1

            cur_row += 1

        self.board = self.next_board

        cell_scape_img, cell_scape_alpha = self.board.get_image()

        plt.imshow(cell_scape_img)

        plt.title("time: {0}".format(time))
        plt.savefig(
                "./images/{0}.jpg".format(time)
                )
        # plt.clf()
        plt.show()

    def place_rule(self, cur_x, cur_y, surroundings):
        """
        Place Rule
        """

        # Top left
        if cur_x - 1 >= self.min_x and cur_y + 1 >= self.min_y:
            self.next_board[cur_x-1][cur_y+1] = surroundings['top_left']

        # Top
        if cur_y + 1 >= self.min_y:
            self.next_board[cur_x-1][cur_y+1] = surroundings['top']

        # Top Right
        if cur_y + 1 >= self.min_y and cur_x + 1 < self.max_x:
            self.next_board[cur_x-1][cur_y+1] = surroundings['top_right']

        # Left
        if cur_x - 1 >= self.min_x:
            self.next_board[cur_x-1][cur_y] = surroundings['left']

        # Right
        if cur_x +1 < self.max_x:
            self.next_board[cur_x+1][cur_y] = surroundings['right']

        # Bottom left
        if cur_y + 1 < self.max_y and cur_x - 1 >= self.min_x:
            self.next_board[cur_x-1][cur_y+1] = surroundings['bottom_left']

        # Bottom
        if cur_y + 1 < self.max_y:
             self.next_board[cur_x][cur_y+1] = surroundings['bottom']

        # Bottom Right
        if cur_y + 1 < self.max_y and cur_x +1 < self.max_x:
             self.next_board[cur_x+1][cur_y+1] = surroundings['bottom_right']



    def apply_rules(self, cur_row, cur_col):
        """
        Apply rules to the cell
        """

        for rule in self.rules:
            lhs = self.next_board.get_surrounding_cells(
                        cur_x, cur_y
                    )
            rhs = rule(lhs)

            self.place_rule(rhs)

            # for key, value in rhs.items():
                # self.next_board[cur_row][cur_col] = rhs


def main():
    """
    Main
    """

    current_simulation = Simulation(110)

    # Setting Plasma Cell
    current_simulation.introduce_cell(Plasma(-1, 4, 4))
    current_simulation.introduce_cell(Plasma(-1, 10, 10))

    # Setting  Nk
    current_simulation.introduce_cell(Nk(-1, 100, 100))

    # Setting MKC
    current_simulation.introduce_cell(
                MegaKaryoCyte(-1, 40, 40)
            )

    # Setting T
    current_simulation.introduce_cell(
                T(-1, 50, 50)
            )

    time = 0

    max_time = 2
    while time < max_time:
        current_simulation.time_step(time)
        time += 1


if __name__ == '__main__':
    main()
