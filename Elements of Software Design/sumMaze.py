#  File: sumMaze.py
#  Description: Depth First Searc
#  Student's Name: Tam Dan Tran
#  Student's UT EID: tvt287
#  Course Name: CS 313E 
#  Unique Number: 51470
#  Date Created: 11/16/17
#  Date Last Modified: 11/17/17

# create a State class
class State():

	def __init__(self, grid, history, start_row, start_col, c_sum):
		self.grid = grid
		self.history = history
		self.start_row = start_row
		self.start_col = start_col
		self.sum = c_sum
	# display current State
	def __str__(self):
		string = "  Grid:"

		for i in range(len(self.grid)):
			string += "\n   "
			for j in range(len(self.grid[0])):
				string += "{:4}".format(str(self.grid[i][j])) 

		string += "\n  history: " + str(self.history)
		string += "\n  start point: (" + str(self.start_row) + "," + str(self.start_col) + ")"
		string += "\n  sum so far: " + str(self.sum)

		return string 

# recurse and find solution
def solve(state):
	# display current state
	print(state)
	print()
	print("Is this a goal state?")
	# base case: reached goal state
	if state.sum == TARGET_VALUE and (state.start_row == END_ROW and state.start_col == END_COL):
		print("Solution found!")
		return state.history
	# base case: exceeded target value.. abandon path
	elif state.sum > TARGET_VALUE:
		print("No. Target exceeded: abandoning path")
		return None
	# move through the grid
	else:
		# create a copy of the grid
		newGrid = []
		for i in range(len(state.grid)):
			newGrid.append(state.grid[i])

		print("No. Can I move right?")
		# try moving right
		# create a new state and move right
		if isValid(state.grid, state.start_row, state.start_col + 1):
			print("Yes!")
			value = state.grid[state.start_row][state.start_col + 1]
			newSum = state.sum + value
			newHistory = state.history + [value]
			newGrid[state.start_row][state.start_col + 1] = "X"
			newStart_col = state.start_col + 1
			newState = State(newGrid, newHistory, state.start_row, newStart_col, newSum)
			input("Paused...")
			print()
			print("Problem is now:")
			result = solve(newState)
			# if recursion achieved goal state
			# return results
			if result != None:
				return result
			# return to original state 
			# to continue moving
			else:
				newGrid[state.start_row][state.start_col + 1] = newHistory.pop()
				newSum -= value
		print("No. Can I move up?")
		# try moving up
		# create a new state and move up
		if isValid(state.grid, state.start_row - 1, state.start_col):
			print("Yes!")
			value = state.grid[state.start_row - 1][state.start_col]
			newSum = state.sum + value
			newGrid[state.start_row - 1][state.start_col] = "X"
			newHistory = state.history + [value]
			newStart_row = state.start_row - 1
			newState = State(newGrid, newHistory, newStart_row, state.start_col, newSum)
			input("Paused...")
			print()
			print("Problem is now:")
			result = solve(newState)
			# if recursion achieved goal state
			# return results 
			if result != None:
				return result
			# return to original state
			# to continue moving 
			else:
				newGrid[state.start_row - 1][state.start_col] = newHistory.pop()
				newSum -= value
		print("No. Can I move down?")
		# try moving down
		# create a new state and move down
		if isValid(state.grid, state.start_row + 1, state.start_col):
			print("Yes!")
			value = state.grid[state.start_row + 1][state.start_col]
			newGrid[state.start_row + 1][state.start_col] = "X"
			newSum = state.sum + value
			newHistory = state.history + [value]
			newStart_row = state.start_row + 1
			newState = State(newGrid, newHistory, newStart_row, state.start_col, newSum)
			input("Paused...")
			print()
			print("Problem is now:")
			result = solve(newState)
			# if recursion achieved goal state
			# return results
			if result != None:
				return result
			# return to original state
			# to continue moving
			else:
				newGrid[state.start_row + 1][state.start_col] = newHistory.pop()
				newSum -= value
		print("No. Can I move left?")
		# try moving left
		# create a new state and move left
		if isValid(state.grid, state.start_row, state.start_col - 1):
			print("Yes!")
			value = state.grid[state.start_row][state.start_col -1]
			newGrid[state.start_row][state.start_col - 1] = "X"
			newSum = state.sum + value
			newHistory = state.history + [value]
			newStart_col = state.start_col - 1
			newState = State(newGrid, newHistory, state.start_row, newStart_col, newSum)
			input("Paused...")
			print()
			print("Problem is now:")
			result = solve(newState)
			# if recursion achived goal state
			# return results
			if result != None:
				return result
			# return to orginal state
			# to continue moving
			else:
				newGrid[state.start_row][state.start_col - 1] = newHistory.pop()
				newSum -= value
		# can't move in any direction
		# return None
		else:
			print("Couldn't move in any direction. Backtracking")
			return None

# checks if move is valid
def isValid(grid, row, col):

	try:
		if grid[row][col] != "X":
			return True 
		elif row < 0 or col < 0:
			return False
		else:
			return False

	except IndexError:
		return False

# open file
F = open("mazedata3.txt", "r")
# create global variables
# from first line of data
LINE1 = F.readline().strip().split()

TARGET_VALUE = int(LINE1[0])
GRID_ROW = int(LINE1[1])
GRID_COL = int(LINE1[2])
START_ROW = int(LINE1[3])
START_COL = int(LINE1[4])
END_ROW = int(LINE1[5])
END_COL = int(LINE1[6])

# make the first move and call start the recursion process
def main():

	grid = []

	for line in F:
		line = line.strip().split()
		line = list(map(int, line))
		grid.append(line)

	history = [grid[START_ROW][START_COL]]
	grid[START_ROW][START_COL] = "X"
	myState = State(grid, history, START_ROW, START_COL, history[0])
	print(solve(myState))

	F.close()
main()
