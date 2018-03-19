from random import *


class Board(object):
	"""docstring for Board"""
	def __init__(self):
		super(Board, self).__init__()
		self.gameBoard = []
		self.boardSize = 10
		for x in range(0,self.boardSize):
			new = []
			for y in range(0,self.boardSize):
				new.append(0)
			self.gameBoard.append(new)
		

	def initSnake(self, x, y):
		self.gameBoard[int(y)][int(x)] = 3

	def placeApple(self):
		ranX = randint(0,self.boardSize - 1)
		ranY = randint(0,self.boardSize - 1)
		while self.gameBoard[ranY][ranX] != 0:
			ranX = randint(0,self.boardSize -1)
			ranY = randint(0,self.boardSize - 1)
		self.gameBoard[ranY][ranX] = 2

	def numZeroes(self):
		numZeroes = 0
		for y in range(0,self.boardSize):
			for x in range(0,self.boardSize):
				if(self.gameBoard[y][x] == 0):
					numZeroes = numZeroes + 1
		return(numZeroes)


	def drawBoard(self):
		for y in range(0,self.boardSize):
			for x in range(0,self.boardSize):
				print(self.gameBoard[y][x], end ='')
			print()



class Snake(object):
		"""docstring for Snake"""
		def __init__(self, newBoard):
			super(Snake, self).__init__()
			self.currentBoard = newBoard
			self.currentBodyX = []
			self.currentBodyY = []
			self.currentBodyX.append( int(self.currentBoard.boardSize/2))
			self.currentBodyY.append(  int(self.currentBoard.boardSize/2))
			self.currentBoard.initSnake(self.currentBodyX[0], self.currentBodyY[0])
			self.futureMoveX = self.currentBodyX[0]
			self.futureMoveY = self.currentBodyY[0]
			self.snakeLength = 1
			self.currentBoard.placeApple()
			self.score = 0
				
		def increaseScore(self,scoreCondition):
			if(scoreCondition == 2):
				self.score = self.score + 200
			elif(scoreCondition == 1):
				self.score = self.score - 1;


		def checkBoard(self,x,y):

			if(x < 0 or y < 0 or x >= self.currentBoard.boardSize or y >= self.currentBoard.boardSize):
				#outOfBounds
				return(0)
			elif( self.currentBoard.gameBoard[y][x] == 1):
				#runs into self
				return(0)
			elif( self.currentBoard.gameBoard[y][x] == 0):
				#goodpiece
				return 1
			elif( self.currentBoard.gameBoard[y][x] == 2):
				#getapple
				return(2)

		def isGoalState(self):
			 numZeroes = self.currentBoard.numZeroes()
			 if(numZeroes == 0):
			 	return(True)
			 return(False)

		def gameLoop(self):
			nextMove = ""
			while(nextMove != "q"):

				self.currentBoard.drawBoard()
				nextMove = input()
				if(nextMove == "w"):
					self.futureMoveY = self.futureMoveY - 1
				elif(nextMove == "s"):
					self.futureMoveY = self.futureMoveY + 1
				elif(nextMove == "d"):
					self.futureMoveX = self.futureMoveX + 1
				elif(nextMove == "a"):
					self.futureMoveX = self.futureMoveX - 1
				action = self.checkBoard(self.futureMoveX, self.futureMoveY)
				if(action == 0):
					nextMove = "q"
				elif(action == 1):
					self.increaseScore
					self.moveSnake()
				elif(action == 2):
					self.growSnake()
					self.increaseScore(action)
					if(not self.isGoalState()):
						self.currentBoard.placeApple()
					else:
						nextMove = "q"
			
			print("thank for playing");
		

		def growSnake(self):
			self.currentBoard.gameBoard[self.futureMoveY][self.futureMoveX] = 3
			self.currentBoard.gameBoard[self.currentBodyY[0]][self.currentBodyX[0]] = 1
			self.currentBodyX.insert(0,self.futureMoveX)
			self.currentBodyY.insert(0,self.futureMoveY)
			self.snakeLength = self.snakeLength + 1

		def moveSnake(self):
			self.currentBoard.gameBoard[self.futureMoveY][self.futureMoveX] = 3
			self.currentBoard.gameBoard[self.currentBodyY[self.snakeLength - 1]][self.currentBodyX[self.snakeLength -1]] = 0
			replaceX = self.currentBodyX[0]
			replaceY = self.currentBodyY[0]
			self.currentBodyX[0] = self.futureMoveX
			self.currentBodyY[0] = self.futureMoveY
			for x in range(0,self.snakeLength - 1):
				replaceXNext = self.currentBodyX[x+1]
				replaceYNext = self.currentBodyY[x+1]
				self.currentBodyX[x + 1] = replaceX
				self.currentBodyY[x + 1] = replaceY
				self.currentBoard.gameBoard[replaceY][replaceX] = 1
				replaceX = replaceXNext
				replaceY = replaceYNext




def main():
	#startGame = input("start game")
	#if(startGame == "y"):
	newBoard = Board()
	runGame = Snake(newBoard)
	runGame.gameLoop()
	print(runGame.score)




if __name__ == '__main__':
	main()