#!/usr/bin/python3
from cgi import FieldStorage
import copy


class Sudoku(object):
    """
    Class to represent a Sudoku solver.
    This uses the backtracking algorithm
    """

    def __init__(self, input_file="input.txt", serverHTML=0):
        """
        Initializer for the class
        :param input_file: String --> The path to the file containing the Sudoku board.
        :param serverHTML: Int --> 0 Does not print each step.
                                   1 Prints out each step as a HTML document (This is for an API
                                     displaying each step of the algorithm).
        """
        self.serveHTML = serverHTML
        self._grid = []
        self._generate_grid(input_file)
        self._solved_grid = copy.deepcopy(self._grid)
        self.solve()

    def solve(self):
        """
        Recursive method to solve the board
        :return: Bool --> True if the board is solved.
                          False if the board is not solved (Starts the back tracking)
        """

        l = [0, 0]

        if not self._find_empty_location(l):
            return True

        row = l[0]
        col = l[1]

        for number in range(1, 10):
            if self._is_valid_move(row, col, number):
                self._solved_grid[row][col] = number

                if self.serveHTML == 1:
                    print("%d%d%d" % (row, col, number), end="")
                if self.solve():
                    return True

                self._solved_grid[row][col] = 0

        return False

    def write_to_file(self, ouput_file = "output.txt"):
        """
        Method to write the solved grid to file
        :param ouput_file: String --> Path to the output file to write to
        :return: None
        """
        fout = open(ouput_file, "w")
        for line in self._solved_grid:
            fout.write(str(line)[1:-1] + "\n")

        fout.close()

    @property
    def og_board(self):
        """
        Getter for the unsolved board
        :return: List --> representing the unsolved board
        """
        return self._grid

    @og_board.setter
    def og_board(self, grid):
        """
        Setter for the unsolved board.
        Also calls self.solve()
        :param grid: List of Lists --> Representing the board
        :return: None
        """
        self._grid = grid
        self.solve()

    @property
    def solved_board(self):
        return self._solved_grid


    def _is_valid_move(self, row, col, num):
        """
        Method to test if inserting a num at position[row][col] would be legal
        :param row: Int --> Representing the row of the position
        :param col: Int --> Representing the column of the position
        :param num: Int --> The number to be tested if it was valid
        :return: Bool --> True if the move is valid.
                          False if the move is not valid.
        """
        valid = True
        if self._used_in_row(row, num):
            valid = False

        if valid and self._used_in_column(col, num):
            valid = False

        if valid and self._used_in_box(row - row % 3, col - col % 3, num):
            valid = False

        return valid

    def _find_empty_location(self, l):
        """
        Finds the next empty position after the current position.
        The location is stored in the local variable l.
        :param l: List --> Containing the position of the current location. [row, col]
        :return: Bool --> True if an empty location was found.
                          False if no empty location is found.
        """
        for r in range(9):
            for c in range(9):
                if self._solved_grid[r][c] == 0:
                    l[0] = r
                    l[1] = c
                    return True
        return False

    def _generate_grid(self, input_file):
        """
        Method to generate the 2D matrix of the unsolved board from the file.
        The 2D matrix is stored in self._grid and self._solved_grid attributes.
        :param input_file: String --> Representing the path to the to the input file
        :return: None.
        """
        if input_file.endswith(".txt"):
            self._generate_grid_txt_file(input_file)

    def _generate_grid_txt_file(self, input_file):
        """
        Method to generate the 2D matrix of the unsolved board from the file.
        The 2D matrix is stored in self._grid and self._solved_grid attributes.
        :param input_file: String --> Representing the path to the to the input file
        :return: None.
        """
        file = open(input_file, "r")

        for line in file:
            l = list(map(int, line.strip().split(",")))
            self._grid.append(l)

    def _used_in_row(self, row, num):
        """
        Method to check if a number is used in the row
        :param row: Int --> Representing the row to be checked
        :param num: Int --> Representing the number to be checked
        :return: Bool --> True if the number is used in the row.
                          False if the number is not used in the row.
        """
        used = False
        for i in range(9):
            if self._solved_grid[row][i] == num:
                used = True
                break
        return used

    def _used_in_column(self, col, num):
        """
            Method to check if a number is used in the column
            :param col: Int --> Representing the column to be checked
            :param num: Int --> Representing the number to be checked
            :return: Bool --> True if the number is used in the column.
                              False if the number is not used in the column.
        """
        used = False
        for i in range(9):
            if self._solved_grid[i][col] == num:
                used = True
                break
        return used

    def _used_in_box(self, row, col, num):
        """
            Method to check if a number is used in the row
            :param row: Int --> Representing the row to be checked
            :param col: Int --> Representing the column to be checked
            :param num: Int --> Representing the number to be checked
            :return: Bool --> True if the number is used in the box.
                              False if the number is not used in the box.
        """
        used = False
        for i in range(3):
            for j in range(3):
                if self._solved_grid[i+row][j+col] == num:
                    used = True
                    break

        return used

    def _print_solved_grid(self):
        """
        Method to print the solved grid. In the following format
        [1,2,3,4,5,6,7,8,9]
        [1,2,3,4,5,6,7,8,9]
        [1,2,3,4,5,6,7,8,9]
        [1,2,3,4,5,6,7,8,9]
        [1,2,3,4,5,6,7,8,9]
        [1,2,3,4,5,6,7,8,9]
        [1,2,3,4,5,6,7,8,9]
        [1,2,3,4,5,6,7,8,9]
        [1,2,3,4,5,6,7,8,9]
        [1,2,3,4,5,6,7,8,9]
        :return: None
        """
        for row in self._solved_grid:
            print(row)

        print()

    def _print_og_grid(self):
        """
       Method to print the original unsolved grid. In the following format
       [1,2,3,4,5,6,7,8,9]
       [1,2,3,4,5,6,7,8,9]
       [1,2,3,4,5,6,7,8,9]
       [1,2,3,4,5,6,7,8,9]
       [1,2,3,4,5,6,7,8,9]
       [1,2,3,4,5,6,7,8,9]
       [1,2,3,4,5,6,7,8,9]
       [1,2,3,4,5,6,7,8,9]
       [1,2,3,4,5,6,7,8,9]
       [1,2,3,4,5,6,7,8,9]
       :return: None
       """
        for row in self._grid:
            print(row)

        print()

    def __str__(self):
        """
        String method for the class. It will have the following format.
         _____________________________
        | 4  8  3 | 9  2  1 | 6  5  7 |
        | 9  6  7 | 3  4  5 | 8  2  1 |
        | 2  5  1 | 8  7  6 | 4  9  3 |
         _____________________________
        | 5  4  8 | 1  3  2 | 9  7  6 |
        | 7  2  9 | 5  6  4 | 1  3  8 |
        | 1  3  6 | 7  9  8 | 2  4  5 |
         _____________________________
        | 3  7  2 | 6  8  9 | 5  1  4 |
        | 8  1  4 | 2  5  3 | 7  6  9 |
        | 6  9  5 | 4  1  7 | 3  8  2 |
         _____________________________
        :return: String --> Representing the solved board if the board has been solved.
                            Else the unsolved board.
        """
        m = ""
        m += "\n _____________________________\n|"
        for i in range(9):
            for k in range(9):
                m += " " + str(self._solved_grid[i][k]) + " "
                if (k+1) % 3 == 0:
                    m+="|"

            if (i+1) % 3 ==0:
                m += "\n _____________________________\n|"
            else:
                m+="\n|"
        return m[0:-1]

    def __hash__(self):
        """
        Hash method for the class.
        :return: Hash of the unsolved board
        """

        return hash(str(self._grid))

    def __eq__(self, other):
        """
        Method to test if 2 unsolved boards are the same.
        :param other: Sudoku class one to test
        :return: Bool --> True if the boards are the same
                          False if the boards are not the same.
        """

if __name__ == "__main__":
    form_data = FieldStorage()
    mode = int(form_data.getfirst("mode", "0").strip())
    if mode == 0:
        s = Sudoku()
        s.solve()
        print(s)

    elif mode == 1:
        print('Content-Type: text/html')
        print()
        s = Sudoku(serverHTML=1)
