import random
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

def make_move(current_board, move, player):
	token = " "
	if player == 1:
		token = "X"
	else:
		token = "O"
	#row 1
	if move == 'NW':
		current_board[0][0] = token
	if move == 'NE':
		current_board[0][2] = token
	if move == 'N':
		current_board[0][1] = token
	#row 2
	if move == "W":
		current_board[1][0] = token
	if move =="C":
		current_board[1][1] = token
	if move == "E":
		current_board[1][2] = token

	#row 3
	if move == "SW":
		current_board[2][0] = token
	if move == "S":
		current_board[2][1] = token
	if move == "SE":
		current_board[2][2] = token


#returns true if there is a three in a row anywhere on the board
#params: list of lists of tuples represinting the board
#returns a boolean 
def check_three_in_a_row(current_board):
	#checks the rows
	for row in current_board:
		if row[0] == row[1] and row[0] == row[2] and row[0] != " ":
			return True
	#checks the first column		
	if current_board[0][0] == current_board[2][0] and current_board[0][0] == current_board[1][0] and current_board[1][0] != " ":
		return True
	# checks right diagonal
	elif current_board[0][0] == current_board[1][1] and current_board[1][1] == current_board[2][2]and current_board[1][1] != " ":
		return True
	# checks left diagonal
	elif current_board[2][0] == current_board[1][1] and current_board[1][1] == current_board[0][2] and current_board[2][0] != " ":
		return True
	#check if third column has a win
	elif current_board[2][2] == current_board[1][2] and current_board[1][2] == current_board[0][2] and current_board[0][2] != " ":
		return True
	#check if second column has a win
	elif current_board[0][1] == current_board[1][1] and current_board[2][1] == current_board[1][1] and current_board[1][1] != " ":
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
	
def player_vs_ai():
	ai_moves = {
					1 : "NW",
					2 : "N",
					3 : "NE",
					4 : "W",
					5 : "C",
					6 : "E",
					7 : "SW",
					8 : "S",
					9 : "SE"
				}

	game_over = False
	current_player = 1
	next_player = 2
	while game_over == False:
		print_board(board)
		
		if(current_player == 1):
			move = input("Player's move > ").upper()
			while not is_valid_move(board, move):
				print("Sorry that's an invalid move!")
				move = input("Player's move > ").upper()
			current_player = next_player
			next_player = 1

		elif current_player == 2:
			move = ai_moves[random.randint(1,9)]
			
			while not is_valid_move(board, move):
				move = ai_moves[random.randint(1,9)]
			
			current_player = next_player
			next_player = 2

		make_move(board, move, next_player)

		if check_board_full(board):
			print_board(board)
			print("Tie!!!")
			game_over = True

		if check_three_in_a_row(board):
			print_board(board)
			if current_player == 2:
				print("Player wins!!!")
			else:
				print("AI wins!!!")
			game_over = True

def player_vs_player():
		game_over = False
		current_player = 1
		next_player = 2
		while game_over == False:
			print("\n\n\n")
			print_board(board)
			if(current_player == 1):
				move = input("X's move > ").upper()
				while not is_valid_move(board, move):
					print("Sorry that's an invalid move!")
					move = input("X's move > ").upper()
				current_player = next_player
				next_player = 1

			elif(current_player == 2):
				move = input("O's move > ").upper()
				while not is_valid_move(board, move):
					print("Sorry that's an invalid move!")
					move = input("O's move > ").upper()
				current_player = next_player
				next_player = 2

			make_move(board, move, next_player)

			if check_board_full(board):
				print_board(board)
				print("Tie!!!")
				game_over = True

			if check_three_in_a_row(board):
				print_board(board)
				if current_player == 2:
					print("X wins!!!")
				else:
					print("O wins!!!")
				game_over = True

def ai_vs_ai():
	ai_moves = {
					1 : "NW",
					2 : "N",
					3 : "NE",
					4 : "W",
					5 : "C",
					6 : "E",
					7 : "SW",
					8 : "S",
					9 : "SE"
				}

	game_over = False
	current_player = 1
	next_player = 2
	while game_over == False:
		print_board(board)
		
		if(current_player == 1):
			move = ai_moves[random.randint(1,9)]
			
			while not is_valid_move(board, move):
				move = ai_moves[random.randint(1,9)]
			
			current_player = next_player
			next_player = 1

		elif current_player == 2:
			move = ai_moves[random.randint(1,9)]
			
			while not is_valid_move(board, move):
				move = ai_moves[random.randint(1,9)]
			
			current_player = next_player
			next_player = 2

		make_move(board, move, next_player)

		if check_board_full(board):
			print_board(board)
			print("Tie!!!")
			game_over = True

		if check_three_in_a_row(board):
			print_board(board)
			if current_player == 2:
				print("AI 1 wins!!!")
			else:
				print("AI 2 wins!!!")
			game_over = True


#def make_move(current_board, )
def __main__():
	#print_board(board)
	#print(check_three_in_a_row(board))
	#print(check_board_full(board))
	#print(is_valid_move(board, 'NE'))
	# player 1 represents X, player 2 represents O
	ai_mode = 0
	ai_mode = input("press 1 to play against AI\npress 2 to play against another human: \npress 3 for AI vs AI game \n> ")
	if ai_mode == '1':
		player_vs_ai()
	if ai_mode == '2':
		player_vs_player()
	if ai_mode == '3':
		ai_vs_ai()

if __name__ == "__main__":
    __main__()