## Program Run
To run the program execute the following commmand in the bash terminal:

```python <filname>```

# The name of the source code file should be in the form of your UNE username followed by the appropriate extension for the programming language used (like .py, .java, .c, or .cpp). 

Your program should be terminal based and when runs, should provide all information about the author, what it does, a concise description of the method you have chosen to solve the puzzle, a list of parameters if they exist that can be used, etc. 

# What the Program does:

1. A goal-based agent object is instantiated with the initial sudoku puzzle.
2. The object is then passed to the depth-first search algorithm function.
	- In the DFS:
	1. A node object is created with the initial state of the sudoku puzzle.
		1. Check if the sudoku puzzle is solved - i.e. reached goal state
			- if not proceed
		2. Append the Node to the stack
		3. Iterate over the stack
			1. pop off the first node on the stack
				1. Check to see if its the goal state
				2. If not goal state
					1. Call expand function which retrieves possible actions (solutions) based on the current state of the board (can be > than 1). 
						1. Actions: 
					2. Poosible solution state nodes added to the stack 