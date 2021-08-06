from GBAgent import GBAgent
import copy

# Initial state of the sudoku board.
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
    """
    Node class
    Description: Class that creates node objects to store possible states in the
    depth-first tree based on the current state of the board.
    Methods: expand()
    """
    def __init__(self, state):
        self.state = state

    def expand(self, problem):
        """
        Function to retrieve actions based on the current state of the board, create a new
        node based on the action and append it to the state list.
        :param problem:
        :return: list of possible actions based on the current state.
        """
        state_list = [] # Empty list to store possible states.
        # Loop over possible actions and append valid actions to the state list.
        for state in problem.actions(self.state):
            state_list.append(Node(state))
        return state_list


def depth_first_search(problem):
    """
    Function that performs depth-first search on the sudoku puzzle using state Nodes generated
    from the goal-based agent.
    :param problem: the current state of the sudoku problem.
    :return:
    """
    start = Node(problem.initial) # Create node object to store board start state.

    # Test if the goal state reached with the initial sudoku board state.
    if problem.isGoal(start.state):
        return start.state

    stack = [start]  # Create list and append start state node of sudoku board.

    # Iterate over the state nodes.
    while stack:
        # Pop-off the last-in node from the tree.
        node = stack.pop()
        # Test if the node is the goal state and return the node if true.
        if problem.isGoal(node.state):
            return node.state
        # If goal state not reached expand the node by finding other possible actions.
        viable_states = node.expand(problem)
        stack.extend(viable_states)  # Add possible states onto the stack.
        problem.print_board(node.state)
    return None



def solve_sudoku(board):
    """
    Function to solve the sudoku puzzle using .
    :param board: the initial state of the sudoku board.
    :return: the solution.
    """
    print("\t------------------------------------------------------------")
    # Instantiate the Goal-base Agent (GBAgent()) with the initial board.
    problem = GBAgent(board)
    # Find the solution using the Goal-based Agent with depth-first search.
    solution = depth_first_search(problem)

    # Print the solution if it is found.
    if solution:
        print("\t------------------------------------------------------------")
        print(
            "\t|\t\t\tFINAL SOLUTION" + "\t\t\t   |\t")
        problem.print_board(solution)
    else:
        print("No solution was found.")

if __name__ == "__main__":
    print("\t------------------------------------------------------------")
    print("\t|                       SUDOKU SOLVER                      |")
    print("\t------------------------------------------------------------")
    print("\t| Author: Alice Schofield                                  |")
    print("\t| Student No.: 220192911                                   |")
    print("\t| Description:                                             |")
    print("\t| The Sudoku Solver uses a goal-based agent with           |")
    print("\t| depth-first search to identify potential cell values and |")
    print("\t| update search tree nodes with states corresponding to    |")
    print("\t| values identified.                                       |")
    print("\t| Further details of the program can viewed in the readme  |")
    print("\t| file.                                                    |")
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
                print("\t|\t\t----------------------- \t\t   |")
            print("\t|\t\t" + " " + str(new_board[i][j]) + " " + str(new_board[i][j + 1]) + " " + str(
                new_board[i][j + 2]) + " " + "|" + " " + str(new_board[i][j + 3]) + " " + str(
                new_board[i][j + 4]) + " " + str(new_board[i][j + 5]) + " " + "|" + " " + str(
                new_board[i][j + 6]) + " " + str(new_board[i][j + 7]) + " " + str(new_board[i][j + 8]) + "\t\t\t   |\t")
    print("\t|                                                          |")
    print("\t------------------------------------------------------------")
    input("\tPress Enter to Solve the Sukodu Puzzle...")
    solve_sudoku(board)
