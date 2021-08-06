import copy


class GBAgent(object):
    """
    Goal-based Agent Class
    Description: Class that simulates a goal-based agent to solve the sudoku puzzle.
    Methods:    isGoal()
                empty_cell()
                potential_values()
                row_complement()
                column_complement()
                grid_complement()
                action()
                print_board()
    """
    def __init__(self, initial):
        """
        Defining constant values.
        :param initial: the initial state of the sudoku board.
        """
        self.initial = initial  # State of the graph when first start
        self.grid = range(0, 9)
        self.value_set = range(1, 10)  # Set of valid values on the sudoku board.

    def isGoal(self, state):
        """
        Function that iterates over the board and identifies if the board is solved.
            - Analyses rows, columns and 3x3 grids to determine if there are invalid entries (cell=0)
            or if the sum of the number is not equal to 45 (i.e. sum of values 1->9).
        :param state: current state of the sudoku board.
        :return: True  - if all rows, columns and 3x3 grids are validly completed
                 False - if there are rows, columns or 3x3 grids with entries missing or
                         the sum of the cells is invalid.
        """
        # Expected sum of each row, column or quadrant.
        sum_grid_element = sum(self.value_set)

        # Check that there are no empty values in the rows and that the row totals equal 45.
        for row in self.grid:
            for column in self.grid:
                if state[row][column] == 0 or sum(state[row]) != sum_grid_element:
                    return False

        # Check that there are no empty values in the columns and that the column totals equal 45.
        for row in self.grid:
            for column in self.grid:
                # Variable to store column totals.
                column_total = 0
                # Iterate over the columns and calculate the sum of the cells.
                for rows in self.grid:
                    column_total += state[rows][column]
                if state[column][row] == 0 or column_total != sum_grid_element:
                    return False

        # Check that there are no empty values in the 3x3 grids and that the sum of the grid is 45.
        for grid in range(0, 9, 3):
            for i in range(0, 9, 3):
                # Variable to store the grid total.
                grid_total = 0
                # Calculate the sum of grid elements.
                for grid_row in range(0, 3):
                    for grid_column in range(0, 3):
                        grid_total += state[i + grid_row][grid + grid_column]
                if state[grid][i] == 0 or grid_total != sum_grid_element:
                    return False

        return True

    def empty_cell(self, state):
        """
        Function that iterates over the board and identifies cells with not entries.
        :param state: list of lists that represent the current state of the sudoku grid.
        :return: the row and column indices of the empty cell.
        """
        for row in self.grid:
            for column in self.grid:
                if state[row][column] == 0:
                    return row, column

    def potential_values(self, values, invalid):
        """
        Function that identifies a subset of potential values based on the current
        state of the board.
        :param values: all possible values (1-9).
        :param invalid: values that have been identified as not in the solution space.
        :return: list of potential values for a given cell.
        """
        number = []  # Empty list to store potential values of cell.
        for num in values:
            if num not in invalid:
                number.append(num)
        return number

    def row_complement(self, state, row):
        """
        Function that determines the values in a row that have not been used.
        :param state: current state of the sudoku board.
        :param row: that row to be evaluated.
        :return: list of values that are not currently present in the row.
        """
        used_values = []  # Empty list to store potential values of cell.
        # Loop over the rows and add values already in the row to a list.
        for num in state[row]:
            if num != 0:
                used_values.append(num)
        return self.potential_values(self.value_set, used_values)

    def column_complement(self, values, state, column):
        """
        Function that determines the values for a cell in a row and a column that have not been used.
        :param values: row values for a cell that have not been used.
        :param state:  the current state of the sudoku board.
        :param column: the column to be evaluated.
        :return: potential values for a cell based on unused row and column values.
        """
        used_values = []  # Empty list to store potential values of cell.
        # Loop over the column and add values to the list of unused column values.
        for i in self.grid:
            if state[i][column] != 0:
                used_values.append(state[i][column])
        return self.potential_values(values, used_values)

    def grid_complement(self, values, state, row, column):
        """
        Function to identify potential cell values based on the associate row, column and 3x3 grid.
        :param values: cell values that are not used in the associate row or column.
        :param state:  current state of the sudoku board.
        :param row:    row of the cell being evaluated.
        :param column: column of the cell being evaluated.
        :return: potential values of a cell based on unused row, column and grid numbers.
        """
        used_values = [] # List of values already appearing in the 3x3 grid.

        # Variables to define the location of the respective 3x3 grids.
        grid_row = int(row / 3) * 3
        grid_column = int(column / 3) * 3

        # Loop over cells in the 3x3 grids and determine the unused values.
        for rows in range(0, 3):
            for columns in range(0, 3):
                used_values.append(state[grid_row + rows][grid_column + columns])
        return self.potential_values(values, used_values)

    def actions(self, state):
        """
        Function to define the actions of the agent based on the current state of the
        grid.
        :param state: the current state of the sudoku grid.
        :return: a new state based on the addition of potential cell values identified in potential_values().
        """
        row, column = self.empty_cell(state) # Identify the first empty cell in the grid.

        # Create a list of potential values for the cell by sucessively calling the
        # row, column and grid complement functions.
        valid_values = self.row_complement(state, row)
        valid_values = self.column_complement(valid_values, state, column)
        valid_values = self.grid_complement(valid_values, state, row, column)

        # Print the cells being evaluated
        print("\t| Possible Value/s for Cell: [row = " + str(row) + "][column = " + str(column) + "]" + "  \t   |")

        # If not potential values found backtrack to previous state where greater than one potential value identified.
        if len(valid_values) == 0:
            print("\t| NO POTENTIAL VALUES FOUND - Backtracking to the cell \t   |\n\t| with 2 or more possible states. \t\t\t   |")

        # Loop over the list of potential values for a cell and generate new state for each.
        for num in valid_values:
            # Create new state by copying the current state.
            new_state = copy.deepcopy(state)
            # Assign a potential cell value to the new state.
            new_state[row][column] = num
            # Statement to print the cell being modified and the value being added.
            print(
                "\t| Value:" + str(new_state[row][column]) + "\t\t\t\t\t\t   |\t")
            yield new_state

    def print_board(self, board):
        """
        Function to print the sukodu board to the console.
        :param board: the sudoku board state to be printed.
        """
        new_board = board
        for i in range(0, 9):
            for j in range(0, 9):
                if new_board[i][j] == 0:
                    new_board[i][j] = str(new_board[i][j])
                    new_board[i][j] = " "
        print("\t------------------------------------------------------------")
        print("\t|                                                          |")
        for i in range(0, 9):
            for j in range(0, 1):
                if i == 3 or i == 6:
                    print("\t|\t\t   -----------------------     \t\t   |")
                print("\t|\t\t   " + " " + str(new_board[i][j]) + " " + str(new_board[i][j + 1]) + " " + str(
                    new_board[i][j + 2]) + " " + "|" + " " + str(new_board[i][j + 3]) + " " + str(
                    new_board[i][j + 4]) + " " + str(new_board[i][j + 5]) + " " + "|" + " " + str(
                    new_board[i][j + 6]) + " " + str(new_board[i][j + 7]) + " " + str(
                    new_board[i][j + 8]) + "\t\t   |\t")
        print("\t|                                                          |")
        print("\t------------------------------------------------------------")
