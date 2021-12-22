from enum import Enum

class Color(Enum):
	RED = 1
	BLK = 2
	NUL = 0

class Board:

	WIDTH = 7
	HEIGHT = 6

	grid = []

	def __init__(self):
		for i in range(0, self.HEIGHT):
			row = []
			for j in range(0, self.WIDTH):
				row.append(Color.NUL)
			self.grid.append(row)

	def place(self, column, color):
		if column < 0 or column > 6: return False

		for i in range(self.HEIGHT - 1, 0, -1):
			if (self.grid[i][column] is Color.NUL):
				self.grid[i][column] = color
				return True

		return False

	def print_board(self):
		print('----------')
		for i in range (0, self.WIDTH):
			print("   ", i+1, "   ", end='\t')
		print()

		for i in range(0, self.HEIGHT):
			for j in range(0, self.WIDTH):
				if self.grid[i][j] is not Color.NUL:
					print("   RED   " if self.grid[i][j] is Color.RED else "   BLK   " if self.grid[i][j] is Color.BLK else "         ", '\t', sep='', end='')
				else:
					print("         ", '\t', sep='', end='')
			print()
		print('----------')

	def check_for_win(self, color):
		for i in range(0, self.HEIGHT):
			for j in range(0, self.WIDTH):
				if self.check_up(i, j, color): return True
				if self.check_down(i, j, color): return True
				if self.check_left(i, j, color): return True
				if self.check_right(i, j, color): return True
				if self.check_up_right(i, j, color): return True
				if self.check_up_left(i, j, color): return True

		return False

	def check_up(self, row, col, color):
		if row > 2: return False
		for k in range(0, 4):
			if self.grid[row+k][col] is not color:
				return False

		return True

	def check_down(self, row, col, color):
		if row < 3: return False

		for k in range(0, 4):
			if self.grid[row-k][col] is not color:
				return False

		return True

	def check_left(self, row, col, color):
		if col < 3: return False

		for k in range(0, 4):
			if self.grid[row][col-k] is not color:
				return False

		return True

	def check_right(self, row, col, color):
		if col > 3: return False

		for k in range(0, 4):
			if self.grid[row][col+k] is not color:
				return False

		return True

	def check_up_right(self, row, col, color):
		if row > 2 or col > 3: return False
		for k in range(0, 4):
			if self.grid[row+k][col+k] is not color:
				return False

		return True

	def check_up_left(self, row, col, color):
		if row > 2 or col < 3: return False
		for k in range(0, 4):
			if self.grid[row+k][col-k] is not color:
				return False

		return True