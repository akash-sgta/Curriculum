# indentation problem faced use sublime text to edit

from multipledispatch import dispatch
import os
import platform
from time import sleep

def mult(*argv):
		ans = 1
		for i in argv:
			ans *= i
		return ans

class Board(object):

    def __init__(self, n=9, player_values=(3,5)):
        self.__size = n
        self.__board = [2 for _ in range(self.__size)]
        self.__turns = 0
        self.__vals = player_values

    def get_values(self):
    	return self.__vals
 
    def get_turn_number(self):
    	return self.__turns

    def increment_turn(self):
    	self.__turns += 1
    	return True
    
    def __str__(self):
    	row_width = int(self.__size**(1/2))
    	string = str("BOARD : {}\n".format(self.__turns))
    	for i in range(row_width):
    		for j in range(row_width):
    			if self.__board[i*row_width + j] == 2:
    				string += "[ ] "
    			elif self.__board[i*row_width + j] == 5:
    				string += "[O] "
    			else:
    				string += "[X] "
    		string += "\n"
    	return string

    @dispatch(int, int)
    def set_board(self, pos, val):
    	if self.__board[pos-1] != 2:
    		return False
    	else:
    		self.__board[pos-1] = val
	    	return True

    def get_size(self):
    	return self.__size

    @dispatch()
    def get_board(self):
    	return tuple(self.__board)

    @dispatch(int)
    def get_board(self, pos):
    	pos -= 1
    	return self.__board[pos]

    #experimental
    @dispatch(list)
    def set_board(self, tup):
    	self.__board = tup.copy()

    def check_winner(self, val):
    	row_width = int(self.__size**(1/2))
    	#rows 1 2 3
    	for i in range(row_width):
    		if mult(self.__board[i*row_width + 0],self.__board[i*row_width + 1],self.__board[i*row_width + 2]) == val**3:
    			return True
    	#cols 4 5 6
    	for i in range(row_width):
    		if mult(self.__board[i + row_width*0],self.__board[i + row_width*1],self.__board[i + row_width*2]) == val**3:
    			return True
    	#diagonals 7 8
    	if mult(self.__board[0 + row_width*0],self.__board[1 + row_width*1],self.__board[2 + row_width*2]) == val**3:
    		return True
    	if mult(self.__board[row_width*1 - 1],self.__board[row_width*2 - 2],self.__board[row_width*3 - 3]) == val**3:
    		return True

    	return False

class TTT_Bot(object):

	def __init__(self, val = 5):
		self.value = val

	def set_val(self, val):
		self.value = val

	def get_check_for(self, player=0):
		if player == 0:
			if self.value == 5:
				return 3
			if self.value == 3:
				return 5
		else:
			return self.value

	def possWin(self, board, choice):

		check_for = self.get_check_for(choice)
		row_width = int(board.get_size() ** (1/2))
		board_ = board.get_board()
		win = list()
		#rows 1 2 3
		for i in range(row_width):
			if mult(board_[i*row_width + 0],board_[i*row_width + 1],board_[i*row_width + 2]) == check_for*check_for*2:
				if board_[i*row_width + 0] == 2:
					pos = i*row_width + 0
				elif board_[i*row_width + 1] == 2:
					pos = i*row_width + 1
				else:
					pos = i*row_width + 2
				win.append((i+1, pos))
		#cols 4 5 6
		for i in range(row_width):
			if mult(board_[i + row_width*0],board_[i + row_width*1],board_[i + row_width*2]) == check_for*check_for*2:
				if board_[i + row_width*0] == 2:
					pos = i + row_width*0
				elif board_[i + row_width*1] == 2:
					pos = i + row_width*1
				else:
					pos = i + row_width*2
				win.append((i+4, pos))
		#diagonals 7 8
		if mult(board_[0 + row_width*0],board_[1 + row_width*1],board_[2 + row_width*2]) == check_for*check_for*2:
			if board_[0 + row_width*0] == 2:
				pos = 0 + row_width*0
			elif board_[1 + row_width*1] == 2:
				pos = 1 + row_width*1
			else:
				pos = 2 + row_width*2
			win.append((7, pos))
		if mult(board_[row_width*1 - 1],board_[row_width*2 - 2],board_[row_width*3 - 3]) == check_for*check_for*2:
			if board_[row_width*1 - 1] == 2:
				pos = row_width*1 - 1
			elif board_[row_width*2 - 2] == 2:
				pos = row_width*2 - 2
			else:
				pos = row_width*3 - 3
			win.append((8, pos))

		

		if len(win) == 0:
			return 0
		else:
			win = win[0][1] + 1
			return win

	def go(self, board, pos):
		return board.set_board(pos, self.value)

	def make(self, board, flag=True):
		board_tuple = board.get_board()
		if board_tuple[5-1] == 2:
			return board.set_board(5, self.value)
		else:
			if flag == True:
				for i in [1,3,5,7]:
					if board_tuple[i] == 2:
						return board.set_board(i+1, self.value)
			else:
				for i in range(0,9):
					if board_tuple[i] == 2:
						return board.set_board(i+1, self.value)



	def __str__(self):
		return "BOT says,'There is nothing to see here!'"

def main(platf):
	board = Board()
	bot = TTT_Bot()
	print("------Tik Tak Toe------")
	print("[.] Use 'q' to quit anytime.")
	print("[?] Would you like to play first(0/1) ?")
	while True:
		ans = input("[<] ")
		if ans == 'q':
			print("[.] Thank you for playing  :)")
			return
		ans = int(ans)
		if ans == 0 or ans == 1:
			break
		else:
			print("[.] Options : 0 and 1")

	if ans == 1:
		# stategy 2(1) 4(3) 6(5) 8(7)
		while True:
			
			if platf == "Windows":
				command = "cls"
			else:
				command = "clear"
			os.system(command)

			cheksum = board.get_turn_number()
			if cheksum  % 2 == 0:
				print("[>] ---------- ")
				print(str(board))
				print("[?] position to enter")
				while True:
					position = input("[<] ")
					if position == 'q':
						print("[.] Thank you for playing  :)")
						return
					position = int(position)
					if position < 1 or position > 9:
						print("[.] Range 1,2,3,4,5,6,7,8,9")
						continue
					if board.set_board(position, 3):
						break
					else:
						print("[.] Something already placed at position.")
						continue
				board.increment_turn()
				sleep(0.25)
			else:
				print("[>] ---------- ")
				print(str(board))	
				if cheksum == 1:
					if board.get_board(5) == 2:
						bot.go(board, 5)
					else:
						bot.go(board, 1)
				elif cheksum == 3:
					opponent_possibility = bot.possWin(board, 0)
					if opponent_possibility != 0:
						bot.go(board, opponent_possibility)
					else:
						bot.make(board, True)
				elif cheksum == 5:
					self_possibility = bot.possWin(board, 1)
					if self_possibility != 0:
						bot.go(board, self_possibility)
					else:
						opponent_possibility = bot.possWin(board, 0)
						if opponent_possibility != 0:
							bot.go(board, opponent_possibility)
						else:
							bot.make(board, True)
				else:
					self_possibility = bot.possWin(board, 1)
					if self_possibility != 0:
						bot.go(board, self_possibility)	
					else:
						opponent_possibility = bot.possWin(board, 0)
						if opponent_possibility != 0:
							bot.go(board, opponent_possibility)
						else:
							bot.make(board, False)
				board.increment_turn()

			if board.check_winner(3) :
				if platf == "Windows":
					command = "cls"
				else:
					command = "clear"
				os.system(command)
				print("[.] --- Player Won --- :)")
				break
			if board.check_winner(5) :
				if platf == "Windows":
					command = "cls"
				else:
					command = "clear"
				os.system(command)
				print("[.] --- Bot Won --- :(")
				break
			if board.get_turn_number() == 10:
				if platf == "Windows":
					command = "cls"
				else:
					command = "clear"
				os.system(command)
				print("[.] --- D R A W --- :P")
				break
	else:
		# stategy 1(0) 3(2) 5(4) 7(6) 9(8)
		while True:

			if platf == "Windows":
				command = "cls"
			else:
				command = "clear"
			os.system(command)

			cheksum = board.get_turn_number()
			if cheksum  % 2 != 0:
				print("[>] ---------- ")
				print(str(board))
				print("[?] position to enter")
				while True:
					position = int(input("[<] "))
					if position < 1 or position > 9:
						print("[.] Range 1,2,3,4,5,6,7,8,9")
						continue
					if board.set_board(position, 3):
						break
					else:
						print("[.] Something already placed at position.")
						continue
				board.increment_turn()
				sleep(0.25)
			else:
				print("[>] ---------- ")
				print(str(board))	
				if cheksum == 0:
					bot.go(board, 1)
				elif cheksum == 2:
					if not bot.go(board,9):
						bot.go(board,3)
				elif cheksum == 4:
					self_possibility = bot.possWin(board, 1)
					if self_possibility != 0:
						bot.go(board, self_possibility)
					else:
						opponent_possibility = bot.possWin(board, 0)
						if opponent_possibility != 0:
							bot.go(board, opponent_possibility)
						else:
							if not bot.go(board, 7):
								bot.go(board, 3)
				elif cheksum == 6:
					self_possibility = bot.possWin(board, 1)
					if self_possibility != 0:
						bot.go(board, self_possibility)
					else:
						opponent_possibility = bot.possWin(board, 0)
						if opponent_possibility != 0:
							bot.go(board, opponent_possibility)
						else:
							bot.make(board, False)

				else:
					self_possibility = bot.possWin(board, 1)
					if self_possibility != 0:
						bot.go(board, self_possibility)
					else:
						opponent_possibility = bot.possWin(board, 0)
						if opponent_possibility != 0:
							bot.go(board, opponent_possibility)
						else:
							bot.make(board, False)
				board.increment_turn()

			if board.check_winner(3) :
				if platf == "Windows":
					command = "cls"
				else:
					command = "clear"
				os.system(command)
				print("[.] --- Player Won --- :)")
				break
			if board.check_winner(5) :
				if platf == "Windows":
					command = "cls"
				else:
					command = "clear"
				os.system(command)
				print("[.] --- Bot Won --- :(")
				break
			if board.get_turn_number() == 10:
				if platf == "Windows":
					command = "cls"
				else:
					command = "clear"
				os.system(command)
				print("[.] --- D R A W --- :P")
				break

	print(str(board))

if __name__ == "__main__":
    platf = str(platform.system())
    while True:
        try:
            if platf == "Windows":
                command = "cls"
            else:
                command = "clear"
            os.system(command)
            main(platf)
        except:
            print("[x] Why you do this? try again..")
            input("[Press Enter]")
        else:
            break
    input("[Press Enter]")

# pyinstaller TicTakToe.py -n TTT --onefile