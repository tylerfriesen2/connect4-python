import time
import random
import math
import copy
from ref import Color, Board

ai_color = Color.RED
opp_color = Color.BLK

checked = 0
depth = 3

def ai_turn(board: Board, depth: int) -> int:
	global checked
	start = time.time()
	print("AI: Thinking...")
	checked = 0
	choice = minimax(board, depth, -math.inf, math.inf, True)
	end = time.time()
	print("\nTook %.4f seconds" % (end-start))
	return choice

def generate_moves(board: Board):
	moves = []
	for j in range(0, board.WIDTH):
		for i in range(board.HEIGHT - 1, 0, -1):
			if board.grid[i][j] is Color.NUL:
				moves.append(j)
				break
	return moves

def evaluate_window(window: list, piece: Color):
	score = 0

	opp = opp_color
	if piece is opp:
		opp = ai_color

	if window.count(piece) == 4:
		score += 100
	elif window.count(piece) == 3 and window.count(Color.NUL) == 1:
		score += 5
	elif window.count(piece) == 2 and window.count(Color.NUL) == 2:
		score += 2

	if window.count(opp) == 3 and window.count(Color.NUL) == 1:
		score -= 4

	return score

def score_position(board: Board, piece: Color):
	score = 0

	COLS = board.WIDTH
	ROWS = board.HEIGHT
	WINDOW_LENGTH = 4

	# Score center column
	center_column = [board.grid[i][COLS // 2] for i in range(0, board.HEIGHT)]
	score += center_column.count(piece) * 3

	# Score horizontals
	for r in range(ROWS):
		row = [board.grid[r][i] for i in range(0, COLS)]
		for c in range(COLS - 3):
			window = row[c:c+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	# Score vertical
	for c in range(COLS):
		col = [board.grid[i][c] for i in range(0, ROWS)]
		for r in range(ROWS - 3):
			window = col[r:r+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	# Score positive sloped diagonal
	for r in range(ROWS - 3):
		for c in range(COLS - 3):
			window = [board.grid[r+i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	# Score negative sloped diagonal
	for r in range(ROWS - 3):
		for c in range(COLS - 3):
			window = [board.grid[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	return score

def minimax(current_board: Board, depth, alpha, beta, max):
	global checked
	moves = generate_moves(current_board)
	ai_win = current_board.check_for_win(ai_color)
	opp_win = current_board.check_for_win(opp_color)
	terminal = ai_win or opp_win 

	if depth == 0 or terminal:
		if ai_win:
			return None, math.inf
		elif opp_win:
			return None, -math.inf
		else: return None, score_position(current_board, ai_color)

	print("\r", checked, " moves checked", end='', sep='')

	if max:
		value = -math.inf
		choice = random.choice(moves)

		# Check each move
		for move in moves:
			checked += 1

			# Copy board and make current move
			b_copy = Board()
			b_copy.grid = copy.deepcopy(current_board.grid)
			b_copy.place(move, ai_color)

			# Get score for next move
			new_score = minimax(b_copy, depth - 1, alpha, beta, False)[1]
			if new_score > value:
				value = new_score
				choice = move

			# Alpha Beta Pruning
			alpha = alpha if alpha > value else value
			if alpha >= beta:
				break

		return choice, value
	else:
		value = math.inf
		choice = random.choice(moves)
		# Check each move
		for move in moves:
			checked += 1

			# Copy board and make current move
			b_copy = Board()
			b_copy.grid = copy.deepcopy(current_board.grid)
			b_copy.place(move, opp_color)

			# Get score for next move
			new_score = minimax(b_copy, depth - 1, alpha, beta, True)[1]
			if new_score < value:
				value = new_score
				choice = move

			# Alpha Beta Pruning
			beta = beta if beta < value else value
			if alpha >= beta:
				break

		return choice, value