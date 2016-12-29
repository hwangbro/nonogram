# GUI for box and instructions

import tkinter as tk
import point


title_color = 'SkyBlue3'

text_color = 'lightgoldenrod1'

fill_color = 'black'
blank_color = 'white'

class BoxGUI:
	'''GUI for box'''

	def __init__(self, row: int, col: int) -> None:
		self._row = row
		self._col = col
		self._tl, self._br = None,None
		self._filled = False

	def contains(self, p: point.Point) -> (point.Point):
		''' Returns true if the point is in the box '''
		px,py = p.frac()
		tl_x, tl_y = self._tl.frac()
		br_x, br_y = self._br.frac()
		return (px <= br_x and px >= tl_x) and (py <= br_y and py >= tl_y)
	
	def draw(self, canvas: tk.Canvas, points) -> None:
		''' Draws the box onto the canvas '''
		self._tl, self._br = points
		
		width = canvas.winfo_width()
		height = canvas.winfo_height()
		self._tl_x, self._tl_y = self._tl.pixel(width, height)
		self._br_x, self._br_y = self._br.pixel(width, height)
		
		self._rect = canvas.create_rectangle(self._tl_x, self._tl_y,
							self._br_x, self._br_y,
							fill = blank_color)

	def fill(self, canvas: tk.Canvas) -> None:
		''' Fills in the box on the canvas '''
		canvas.itemconfig(self._rect, fill = fill_color)
		self._filled = True

	def unfill(self, canvas: tk.Canvas) -> None:
		''' Unfills the box on the canvas '''
		canvas.itemconfig(self._rect, fill = blank_color)
		self._filled = False
	
	def x(self, canvas: tk.Canvas) -> None:
		''' Draws an X on the box '''
		canvas.create_line(self._tl_x, self._tl_y, self._br_x, self._br_y, width = 3)
		canvas.create_line(self._tl_x, self._br_y, self._br_x, self._tl_y, width = 3)


class InstructionGUI(BoxGUI):
	'''GUI for instruction'''
	
	def __init__(self, row: int, col: int) -> None:
		super().__init__(row,col)

	def draw(self, canvas: tk.Canvas, points, instr: int) -> None:
		''' Draws the instruction box onto the canvas '''
		self._tl, self._br = points

		width = canvas.winfo_width()
		height = canvas.winfo_height()

		tl_x, tl_y = self._tl.pixel(width, height)
		br_x, br_y = self._br.pixel(width, height)

		center_x = (tl_x + br_x) / 2
		center_y = (tl_y + br_y) / 2
		
		canvas.create_text(center_x, center_y, text = str(instr), font = 'times 12 bold')



def create_box_points(row: int, col: int, total_row: int, total_col: int) -> (point.Point):
	'''Returns the top-left and bottom-right points of box'''

	buf = .95
	x = buf/total_col
	y = buf/total_row
	pad = (1-buf)/2
	return (point.from_frac(pad+(x*col), pad+(y*row)),
		point.from_frac(pad+(x*(col+1)), pad+(y*(row+1))))


