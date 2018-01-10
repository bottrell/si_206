#global dictionary representing the board
board = [
	#row 1
	[ ' ', ' ', ' '],
	#row2
	[ ' ', ' ', ' '],
	#row3
	[ ' ', ' ', ' ']
]
#Function that prints the board to standard output
#params: list of lists of tuples of coordinates and the moves corresponding
#returns: nothing
def print_board(current_board):
	#use count to check if it's the last row in order to avoid the
	#last line looking really ugly
	row_count = 0
	print("CURRENT BOARD: \n")
	for row in current_board:
		row_count += 1
		print(row[0], end = ' | ')
		print(row[1], end = ' | ')
		print(row[2], end = '\n')
		if row_count != 3:
			print ("---------")
	print("\n")


#returns true if there is a three in a row anywhere on the board
#params: list of lists of tuples represinting the board
#returns a boolean 
def check_three_in_a_row(current_board):
	for row in current_board:
		if row[0] == row[1] and row[0] == row[2] and row[0] != " ":
			return True
	if current_board[0][0] == current_board[2][0] and current_board[0][0] == current_board[1][0] and current_board[1][0] != " ":
		return True

	elif current_board[0][0] == current_board[1][1] and current_board[1][1] == current_board[2][2]and current_board[1][1] != " ":
		return True
	
	elif current_board[2][0] == current_board[1][1] and current_board[1][1] == current_board[0][2] and current_board[2][0] != " ":
		return True

	return False

#checks if the board is full
#params: list of lists of tuples representing the board
#returns true iff there is a full board
def check_board_full(current_board):
	for row in current_board:
		for coord in row:
			if coord == " ":
				return False

	return True

#checks if the move a user makes is valid
#params: list of lists of tuples representing the board and a string representing the user's input
#returns true iff the move does the following:
#		1) does not overwrite a previously defined square
#		2) user's input is a valid direction
def is_valid_move(current_board, input):
	valid_moves = { 'NE': current_board[0][2], 
					'N' : current_board[0][1], 
					'NW': current_board[0][0], 
					'W' : current_board[1][0], 
					'E' : current_board[1][2], 
					'C' : current_board[1][1], 
					'SW': current_board[2][0], 
					'S' : current_board[2][1], 
					'SE': current_board[2][2]
					}
	if input not in valid_moves:
		return False

	elif valid_moves[input] != " ":
		return False
	
	return True


def __main__():
	#print_board(board)
	#print(check_three_in_a_row(board))
	#print(check_board_full(board))
	#print(is_valid_move(board, 'NE'))
	game_over = False
	# player 1 represents X, player 2 represents O
	current_player = 1
	next_player = 2
	while game_over = False:
		print_board(board)


if __name__ == "__main__":
    __main__()