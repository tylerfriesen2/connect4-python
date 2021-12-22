import ai
from ref import Color, Board

next = Color.RED
board = Board()

def main():
	global next

	turns = 0
	win = False
	col = -1

	player = int(input("Which color would you like? (1 = RED / 2 = BLK): "))

	if player == 1:
		ai.opp_color = Color.RED
		ai.ai_color = Color.BLK
	else:
		ai.opp_color = Color.BLK
		ai.ai_color = Color.RED

	while not win:
		if next is Color.RED and player == 1:
			col = int(input(f"{next}'s turn: ")) - 1
		elif next is Color.BLK and player == 2:
			col = int(input(f"{next}'s turn: ")) - 1
		else:
			ai.board = board
			col = ai.ai_turn(board, (42 - turns)//2)[0]
			print("AI: Plays column: ", col+1)

		turns += 1
		win = do_turn(col)
	

def do_turn(col):
	global board, next

	valid = board.place(col, next)
	
	if valid:
		board.print_board()
		if board.check_for_win(next):
			print(next, "wins!")
			return True
		next = Color.BLK if next is Color.RED else Color.RED

main()