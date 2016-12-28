#Logical classes for monigram

class Box:
	'''Box object for the logic'''

	def __init__(self, row: int, col: int) -> None:

		self._row = row
		self._col = col
		self._filled = False
		self._x = False

	def row(self) -> int:
		''' Get method for rows '''
		return self._row

	def col(self) -> int:
		''' Get method for columns '''
		return self._col

	def filled(self) -> bool:
		''' Returns True if box is filled '''
		return self._filled

	def switch(self) -> None:
		''' Changes state of box '''
		self._filled = not self._filled

	def x(self) -> bool:
		''' Returns if box is X'd out '''
		return self._x

	def switch_x(self) -> None:
		''' Changes X state of box '''
		self._x = not self._x

	def __str__(self) -> str:
		''' Overwrites str method for printing '''
		return "X" if self._filled else "O"

class Board:
	'''Puzzle object for the logic'''

	def __init__(self, t_rows: int, t_cols: int, rows: [[int]], cols: [[int]], solution: [[bool]]) -> None:
		self._boxes = []
		self._rows = t_rows #in boxes
		self._cols = t_cols #in boxes
	
		self.createBoard()
 
		self._rowinstr = rows
		self._colinstr = cols

		self._maxrinstr = max([len(r) for r in self._rowinstr])
		self._maxcinstr = max([len(c) for c in self._colinstr])
		self._solution = solution
		self._solved = False


	def createBoard(self) -> None:
		''' Creates array of boxes to represent board '''
		for row in range(self._rows):
			self._boxes.append([])
			for col in range(self._cols):
				self._boxes[row].append(Box(row, col))

	def changeBox(self, row, col) -> None:
		''' Changes the state of the specified box '''
		self._boxes[row][col].switch()
	
	def checkIfSolved(self) -> bool:
		''' Checks if board is in solved state '''
		for r in range(self._rows):
			for c in range(self._cols):
				if self._solution[r][c] != self._boxes[r][c].filled():
					return False
		return True

	def printBoard(self) -> None:
		''' Prints out simplistic view of board '''
		for r in range(self._rows):
			for c in range(self._cols):
				print(self._boxes[r][c], end = ' ')
			print()

	def printSolution(self) -> None:
		''' Prints out simplistic view of solution '''
		for r in range(self._rows):
			for c in range(self._cols):
				print('t' if self.solution()[r][c] else 'f', end= ' ')
			print()

	def trueIndex(self, row, col) -> (int, int):
		''' Returns row/col of box, when grid contains instr '''
		return (row+self._maxcinstr, col+self._maxrinstr)

	def rows(self) -> int:
		''' Get method for rows '''
		return self._rows

	def cols(self) -> int:
		''' Get method for cols '''
		return self._cols

	def maxrinstr(self) -> int:
		''' Get method for max # of instr '''
		return self._maxrinstr

	def maxcinstr(self) -> int:
		''' Get method for max # of instr '''
		return self._maxcinstr
	
	def rowinstr(self) -> [[int]]:
		''' Get method for row instructions '''
		return self._rowinstr

	def colinstr(self) -> [[int]]:
		''' Get method for column instructions '''
		return self._colinstr

	def solution(self) -> [[int]]:
		''' Get method for solution '''
		return self._solution
