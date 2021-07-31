from GBAgent import GBAgent
import copy

board = [[9, 0, 0, 1, 7, 0, 4, 0, 2],
         [1, 6, 0, 0, 4, 0, 0, 9, 5],
         [0, 0, 8, 0, 0, 3, 0, 0, 0],
         [0, 1, 0, 9, 0, 0, 5, 7, 3],
         [0, 4, 0, 0, 0, 0, 0, 2, 0],
         [5, 8, 9, 0, 0, 7, 0, 1, 0],
         [0, 0, 0, 4, 0, 0, 7, 0, 0],
         [6, 7, 0, 0, 2, 0, 0, 5, 8],
         [3, 0, 1, 0, 5, 8, 0, 0, 6]]


class Node:
    """ Node class that creates node objects. """

    def __init__(self, state):
        self.state = state

    def expand(self, problem):
        """
        Function to retrieve actions based on the current state of the board.
        :param problem:
        :return:
        """
        # Return list of valid states

        state_list = []
        for state in problem.actions(self.state):
            state_list.append(Node(state))
        return state_list


def DFS(problem):
    """
    Function that performs depth-first search on the sudoku puzzle.
    :param problem:
    :return:
    """
    # Create a Node that stores the initial state of the sudoku grid
    start = Node(problem.initial)

    # Test to see if the initial state is the goal state, if it is return the initial state.
    if problem.goal_state_test(start.state):
        return start.state

    # Create a list and append the initial state of the sudoku grid.
    stack = []
    stack.append(start)  # Place initial node onto the stack

    # Iterate over the stack which stores the Nodes of the different states
    while stack:
        #
        node = stack.pop()
        # If the node.state is the goal state then return the goal state
        if problem.goal_state_test(node.state):
            return node.state
        # Add new states to the list as they are generated.
        viable_states = node.expand(problem)
        stack.extend(viable_states)  # Add viable states onto the stack
        problem.print_board(node.state)
    return None


""" 
Function to solve the sudoku puzzle with the depth-first search.
"""


def solve_sudoku(board):
    """
    Function to solve the sudoku puzzle.
    :param board:
    :return:
    """

    print("\t------------------------------------------------------------")
    problem = GBAgent(board)
    solution = DFS(problem)

    if solution:
        print("\t------------------------------------------------------------")
        print(
            "\t|\t\t\t\t\t\t FINAL SOLUTION" + "\t\t\t\t\t   |\t")
        problem.print_board(solution)





if __name__ == "__main__":
    # initial = GBAgent(board)
    # initial.print_board(board)
    # first = GBAgent(board)
    #printing(board)
    #input("Press Enter to continue...")
    print("\t------------------------------------------------------------")
    print("\t|                       SUDOKU SOLVER                      |")
    print("\t|                                                          |")
    print("\t|                                                          |")
    print("\t------------------------------------------------------------")
    print("\t|                       SUDOKU PUZZLE                      |")
    print("\t------------------------------------------------------------")
    print("\t|                                                          |")
    new_board = copy.deepcopy(board)
    for i in range(0, 9):
        for j in range(0, 9):
            if new_board[i][j] == 0:
                new_board[i][j] = str(new_board[i][j])
                new_board[i][j] = " "
    for i in range(0, 9):
        for j in range(0, 1):
            if i == 3 or i == 6:
                print("\t|\t\t\t\t\t-----------------------")
            print("\t|\t\t\t\t\t" + " " + str(new_board[i][j]) + " " + str(new_board[i][j + 1]) + " " + str(
                new_board[i][j + 2]) + " " + "|" + " " + str(new_board[i][j + 3]) + " " + str(
                new_board[i][j + 4]) + " " + str(new_board[i][j + 5]) + " " + "|" + " " + str(
                new_board[i][j + 6]) + " " + str(new_board[i][j + 7]) + " " + str(new_board[i][j + 8]) + "\t\t\t\t   |\t")
    print("\t|                                                          |")
    print("\t------------------------------------------------------------")
    input("\tPress Enter to Solve the Sukodu Puzzle...")
    solve_sudoku(board)
