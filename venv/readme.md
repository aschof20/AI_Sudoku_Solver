# Sudoku Solver 

Sodoku Solver is a program that identifies solutions to sudoku puzzles.

## Author
Alice Schofield, Student No.: 220192911, aschof20@une.edu.au

## Description
### General Overview
Sudoku Solver uses a goal-based agent with depth-first search to identify a solution to a sudoku puzzle. Specifically, a brute-force approach was used to identify possible candidate values for each cell. If two or more possible values are identified, one solution is chosen and the algorithm proceeds. If no possible solutions are identified in subsequent cells, the algorithm backtracks and replaces the value with an alternative. 

### Sequence of Events
1. Instantiate Goal-based Agent (GBAgent()) object with the initial board state.
2. Instantiate a Node object with the object in (1).
3. Test if goal state achieved (rows, columns and 3x3 grid contain one instance of the numbers 1-9).
   
	a) Outcome: YES - print the solution.
   
    b) Outcome: NO - proceed to (4).	   
4. Append node from (2) to the stack.
5. Pop the Node off the stack and test is goal state achieved.
   
	a) Outcome: YES - print the solution.
   
    b) Outcome: NO - proceed to (6).
6. Identify potential viable states for the first empty cell based on the state of the node in (5).
   
   a) Outcome: No viable states found - bracktrack to (5).
   
   b) Outcome: Viable states found - move to (7).
7. Create a new node/s with the potential states from (6).
8. Add new node/s to the stack.
9. Repeat steps 5-8 until the goal state is found.

## Installation

### Requirements
* Python 3.9.6

####To run Sudoku Solver:

1. Run the program by entering `python3 Solver.py` into the Linux terminal.
2. Press enter to execute the puzzle solving.
 

