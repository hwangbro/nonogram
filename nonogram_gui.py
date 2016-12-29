import tkinter as tk
import logic_components
import point
import boards
import options_gui
from box import BoxGUI, InstructionGUI, create_box_points


title_color = 'SkyBlue3'
text_color = 'lightgoldenrod1'
fill_color = 'black'
blank_color = 'white'


class NonogramGUI:
	'''GUI for game board itself'''

	def __init__(self, window: tk.Tk, board: logic_components.Board) -> None:
		self._window = window
		self._board = board
		self._tiles = []

		self._rows = self._board.rows() + self._board.maxcinstr() #includes instruction
		self._cols = self._board.cols() + self._board.maxrinstr() #includes instruction
		self._canvas = tk.Canvas(
			master = self._window,
			height = 600,
			width = 600,
			background = 'light goldenrod')
		orange = '#FF943C'	
		self._canvas.grid(row = 1, column = 0,
				sticky = tk.N + tk.W + tk.S + tk.E)
		self._window.rowconfigure(1, weight = 1)
		self._window.columnconfigure(0, weight = 1)	

	def _draw_row_instr(self) -> None:
		''' Draws the row instructions on the board '''
		for i in range(len(self._board.rowinstr())):
			for j in range(len(self._board.rowinstr()[i])):
				row = self._board.maxcinstr()+i
				col = self._board.maxrinstr() - len(self._board.rowinstr()[i])+j
				cell = InstructionGUI(row,col)
				cell.draw(self._canvas,
					create_box_points(row,col,self._rows, self._cols),self._board.rowinstr()[i][j])
	
	def _draw_col_instr(self) -> None:
		''' Draws the column instructions on the board '''
		for i in range(len(self._board.colinstr())):
			for j in range(len(self._board.colinstr()[i])):
				row = self._board.maxcinstr() - len(self._board.colinstr()[i]) + j
				col = self._board.maxrinstr()+i
				cell = InstructionGUI(row,col)
				cell.draw(self._canvas,
					create_box_points(row,col, self._rows, self._cols),self._board.colinstr()[i][j])
			
	def _draw_boxes(self) -> None:
		''' Draws the rest of the board '''
		for i in range(self._board.rows()):
			self._tiles.append([])
			for j in range(self._board.cols()):
				cell = BoxGUI(i,j) #i and j are index of boxes only. first box is 0,0
				self._tiles[i].append(cell)
				row, col = self._board.trueIndex(i,j)
				cell.draw(self._canvas,
					create_box_points(row, col, self._rows, self._cols)) #draws based on location respecting instructions
				if self._board._boxes[i][j].x():
					cell.x(self._canvas)
				elif self._board._boxes[i][j].filled():
					cell.fill(self._canvas)

	def _draw_tiles(self) -> None:
		''' Draws all the tiles on the board '''
		self._tiles = []
		self.width = self._canvas.winfo_width()
		self.height = self._canvas.winfo_height()

		self._draw_row_instr()
		self._draw_col_instr()
		self._draw_boxes()

	def _draw_lines(self) -> None:
		''' Draws the lines on the board '''
		for i in range(len(self._board.rowinstr())+1):
			start = create_box_points(self._board.maxcinstr() + i, 0, self._rows, self._cols)
			end = create_box_points(self._board.maxcinstr() + i, self._cols-1, self._rows, self._cols)
			start_x, start_y = start[0].pixel(self.width, self.height)
			end_x = end[1].pixel(self.width, self.height)[0]
			w = 3 if (i==0 or i%5 == 0) else 1 #if it's a multiple of 5, bold
			self._canvas.create_line(start_x, start_y, end_x, start_y, fill = 'gray', width = w)

		for i in range(len(self._board.colinstr())+1):
			start = create_box_points(0, self._board.maxrinstr()+i, self._rows, self._cols)
			end = create_box_points(self._rows-1, self._board.maxrinstr()+i, self._rows, self._cols)
			start_x, start_y = start[0].pixel(self.width, self.height)
			end_y = end[1].pixel(self.width, self.height)[1]
			w = 3 if (i == 0 or i % 5 == 0) else 1
			self._canvas.create_line(start_x, start_y, start_x, end_y, fill = 'gray', width = w)
	
	def _draw_board(self) -> None:
		''' Call this to draw the entire board '''
		self._canvas.delete(tk.ALL)
		self._draw_tiles()
		self._draw_lines()

class NonogramApplication:
	'''Will start the entire application'''

	def __init__(self, board: logic_components.Board) -> None: 
		self._board = board
		self._stop = False
		self._root_window = tk.Tk()
		self._root_window.wm_title('Monigram!')
		self._root_window.minsize(700,700)
		self._root_window.configure(background = title_color)

		label_frame = tk.Frame(
			master = self._root_window,
			background = title_color)
		label_frame.grid(row = 0, column = 0,
				sticky = tk.N + tk.E + tk.S + tk.W)
		title_label = tk.Label(
			master = label_frame,
			text = 'Monigram! (nonogram)',
			background = title_color,
			foreground = text_color,
			font = 'times 24 bold italic underline')
		title_label.grid(row = 0, column = 1, padx = 10,
			sticky = tk.N + tk.E + tk.W + tk.S)

		self._solved = tk.StringVar()
		self._solved.set('Unsolved!')

		self._solved_label = tk.Label(
			master = label_frame,
			textvariable = self._solved,
			background = title_color,
			foreground = 'red',
			font = 'times 16 bold')

		self._solved_label.grid(row = 0, column = 2, sticky = tk.N + tk.E + tk.S + tk.W)
		self._back_button = tk.Button(master = label_frame,
					text = 'Back',
					font = 'times 14 bold',
					background = title_color,
					foreground = text_color,
					command = self._back_button_pressed)

		self._back_button.grid(row=0,column=0)# sticky = tk.W + tk.S + tk.N + tk.E)
		label_frame.columnconfigure(0, weight = 1)
		label_frame.columnconfigure(1, weight = 1)
		label_frame.columnconfigure(2, weight = 1)

		self._BoardGUI = NonogramGUI(self._root_window, self._board)

		self._BoardGUI._canvas.bind('<Configure>', self._on_canvas_resized)
		self._BoardGUI._canvas.bind('<Button-1>', self._on_button_down)
		self._BoardGUI._canvas.bind('<B1-Motion>', self._on_mouse_moved)
		self._BoardGUI._canvas.bind('<Button-3>', self._on_rclick_down)
		self._BoardGUI._canvas.bind('<B3-Motion>', self._on_rclick_held)
	
	def _on_canvas_resized(self, event: tk.Event) -> None:
		''' Re-draw the board when resized '''
		self._BoardGUI._draw_board()

	def _on_rclick_down(self, event: tk.Event) -> None:
		''' On right click, draw an X '''
		self._switch_x(event.x, event.y, True)

	def _on_rclick_held(self, event: tk.Event) -> None:
		''' On right click held, either draw or erase X's depending on first state '''
		self._switch_x(event.x, event.y, False)
				
	def _on_button_down(self, event: tk.Event) -> None:
		''' On left click, fill/unfill '''
		self.switch_tile(event.x, event.y, True)

	def _on_mouse_moved(self, event: tk.Event) -> None:
		''' On left click held, either fill or unfill X's depending on first state '''
		self.switch_tile(event.x, event.y, False)

	def _back_button_pressed(self) -> None:
		''' Go back to main menu '''
		self._root_window.destroy()
		run_nonogram()
	

	def _switch_x(self, x: int, y: int, checkState: bool) -> None:
		''' Flip the X status of a box '''
		if self._stop:
			return

		click_point = point.from_pixel(x, y, self._BoardGUI.width, self._BoardGUI.height)

		for row in range(len(self._BoardGUI._tiles)):
			for col in range(len(self._BoardGUI._tiles[row])):
				tile = self._BoardGUI._tiles[row][col]
				if tile.contains(click_point) and type(tile) is BoxGUI:
					box = self._board._boxes[row][col]
					if checkState:
						self._xmode = not box.x()
						box.switch_x()
					elif box.x() != self._xmode:
						box.switch_x()
					if box.filled():
						box.switch()
					self._BoardGUI._draw_board()


	def switch_tile(self, x: int, y: int, checkState: bool) -> None:
		''' Flip the fill status of a box '''
		if self._stop:
			return
		mouse_point = point.from_pixel(x,y,self._BoardGUI.width, self._BoardGUI.height)
		for row in range(len(self._BoardGUI._tiles)):
			for col in range(len(self._BoardGUI._tiles[row])):
				tile = self._BoardGUI._tiles[row][col]
				if tile.contains(mouse_point) and type(tile) is BoxGUI:
					box = self._board._boxes[row][col]
					if checkState:
						self._mode = not box.filled()
						box.switch()
					elif box.filled() != self._mode:
						box.switch()
					self._BoardGUI._draw_board()

		self.update_solved()

	def update_solved(self) -> None:
		''' Checks if board is solved. If solved, changes sovled text, freezes board '''
		if self._board.checkIfSolved():
			self._solved.set('Solved!!')
			self._solved_label.config(background = title_color, foreground = 'green', font = 'times 20 bold')
			self._stop = True

	def start(self) -> None:
		self._root_window.mainloop()

def run_nonogram():
	try:
		menu = options_gui.OptionMenu()
		b = menu.board
		if (b == 'A'):
			game_board = boards.boardA()
		elif (b == 'B'):
			game_board = boards.boardB()
		else:
			game_board = boards.boardD()
		app = NonogramApplication(game_board)
		app.start()
	except:
		pass

if __name__ == '__main__':
	run_nonogram()

