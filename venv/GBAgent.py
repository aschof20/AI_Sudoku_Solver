import copy


class GBAgent(object):
    """
    Goal-based Agent Class
    - class simulates a goal-based agent to solve the sudoku puzzle
    """

    def __init__(self, initial):
        """

        :param initial: the initial state of the sudoku board.
        """
        self.initial = initial  # State of the graph when first start
        self.grid = range(0, 9)
        self.value_set = range(1, 10)  # Set of valid values on the sudoku board.

    def goal_state_test(self, state):
        """
        Function that iterates over the board and identifies if the board is solved.
            - Analyses rows, columns and 3x3 grids to determine if there are invalid entries (cell=0)
            or if the sum of the number is not equal to 45 (i.e. sum of values 1->9).
        :param state: current state of the sudoku board.
        :return: True - if all rows, columns and 3x3 grids are validly completed
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
        :return: the empty cell row and column.
        """
        for row in self.grid:
            for column in self.grid:
                if state[row][column] == 0:
                    return row, column

    def potential_values(self, values, invalid):
        """
        Helper function to determine potential values of a cell.
        Function identifies a subset of potential values
        :param values:
        :param invalid: values that have been identified as not in the solution space.
        :return: list of potential values for a given cell.
        """
        number = []  # Empty list to store potential values of cell.
        for num in values:
            if num not in invalid:
                number.append(num)
        return number

    """
    Function to determine is values are valid for a row in the grid
    Determine list of valid values of a cell based on row totals/number appearances.
    :return list of values that don't already appear in the row.
    """

    # Filter valid values based on row
    def row_complement(self, state, row):
        used_values = []  # Empty list to store potential values of cell.
        # Loop over the rows and add values already in the row to a list.
        for num in state[row]:
            if num != 0:
                used_values.append(num)
        return self.potential_values(self.value_set, used_values)

    # Filter valid values based on column
    def column_complement(self, values, state, column):
        used_values = []  # Empty list to store potential values of cell.
        for i in self.grid:
            if state[i][column] != 0:
                used_values.append(state[i][column])
        return self.potential_values(values, used_values)

    # Filter valid values based on quadrant
    def grid_complement(self, values, state, row, column):
        # List of values already appearing in the 3x3 grid.
        used_values = []

        # Variables to define the location of the respective 3x3 grids.
        grid_row = int(row / 3) * 3
        grid_column = int(column / 3) * 3

        # Loop over cells in the 3x3 grids and determine the values already appearing.
        for rows in range(0, 3):
            for columns in range(0, 3):
                used_values.append(state[grid_row + rows][grid_column + columns])
        return self.potential_values(values, used_values)

    def actions(self, state):
        """
        Function to define the actions of the agents based on the current state of the
        grid.
        :param state:
        :return:
        """
        # Identify the first empty cell in the grid.
        row, column = self.empty_cell(state)

        # Create a list of potential values for the cell by calling the
        # row, column and grid complement functions.
        valid_values = self.row_complement(state, row)
        valid_values = self.column_complement(valid_values, state, column)
        valid_values = self.grid_complement(valid_values, state, row, column)

        # Generate new state for each valid value option
        for num in valid_values:
            # Create a copy of the new state.
            new_state = copy.deepcopy(state)
            # Assign the number to the new state.
            new_state[row][column] = num
            # Statement to print the cell being modified and the value being added.
            print(
                "\t| Modifying - Row: " + str(row) + ", Column: " + str(column) + ", Value: " + str(new_state[row][column]) + "\t\t\t\t   |\t")
            yield new_state

    def print_board(self, board):
        """
        Function to print the sukodu board to the console.
        :param board: the sudoku board to be printed
        :return:
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
                    print("\t|\t\t\t\t\t-----------------------\t\t\t\t   |")
                print("\t|\t\t\t\t\t" + " " + str(new_board[i][j]) + " " + str(new_board[i][j + 1]) + " " + str(
                    new_board[i][j + 2]) + " " + "|" + " " + str(new_board[i][j + 3]) + " " + str(
                    new_board[i][j + 4]) + " " + str(new_board[i][j + 5]) + " " + "|" + " " + str(
                    new_board[i][j + 6]) + " " + str(new_board[i][j + 7]) + " " + str(
                    new_board[i][j + 8]) + "\t\t\t\t   |\t")
        print("\t|                                                          |")
        print("\t------------------------------------------------------------")
