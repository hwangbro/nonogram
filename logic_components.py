#Logical classes for monigram

class Box:
	'''Box object for the logic'''

	def __init__(self, row: int, col: int):
		self._row = row
		self._col = col
		self._filled = False
		self._x = False

	def row(self):
		return self._row

	def col(self):
		return self._col

	def filled(self):
		return self._filled

	def switch(self):
		self._filled = not self._filled

	def x(self):
		return self._x

	def switch_x(self):
		self._x = not self._x

	def __str__(self):
		return "X" if self._filled else "O"

class Board:
	'''Puzzle object for the logic'''

	def __init__(self, t_rows: int, t_cols: int, rows: [[int]], cols: [[int]], solution: [[bool]]):
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


	def createBoard(self):
		for row in range(self._rows):
			self._boxes.append([])
			for col in range(self._cols):
				self._boxes[row].append(Box(row, col))

	def changeBox(self, row, col):
		self._boxes[row][col].switch()
	

	def checkIfSolved(self):
		for r in range(self._rows):
			for c in range(self._cols):
				if self._solution[r][c] != self._boxes[r][c].filled():
					return False
		return True

	def printBoard(self):
		for r in range(self._rows):
			for c in range(self._cols):
				print(self._boxes[r][c], end = ' ')
			print()

	def printSolution(self):
		for r in range(self._rows):
			for c in range(self._cols):
				print('t' if self.solution()[r][c] else 'f', end= ' ')
			print()

	def trueIndex(self, row, col) -> (int, int):
		return (row+self._maxcinstr, col+self._maxrinstr)

	def rows(self):
		return self._rows

	def cols(self):
		return self._cols

	def maxrinstr(self):
		return self._maxrinstr

	def maxcinstr(self):
		return self._maxcinstr

	def boxWithTrueIndex(self, row: int, col: int):
		return self._boxes[row - self._maxcinstr][col-self._maxrinstr]

	def rowinstr(self):
		return self._rowinstr

	def colinstr(self):
		return self._colinstr

	def solution(self):
		return self._solution
