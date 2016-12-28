import tkinter as tk

text_color = 'lightgoldenrod1'
bg_color = 'skyblue3'
button_bg = 'gold'
class OptionMenu:
	def __init__(self):
		self._window = tk.Tk()
		self._window.wm_title('Options Menu')
		self._window.configure(background = bg_color)
		self._window.resizable(width = False, height = False)

		self._title_label = tk.Label(master = self._window,
					text = 'Monigram!',
					background = bg_color,
					foreground = text_color,
					font = 'times 24 bold italic underline')
		self._title_label.grid(row=0, column = 1, padx = 20,
					sticky = tk.N + tk.S + tk.E + tk.W)

		self._puzzle_1 = tk.Button(master = self._window, 
					text = 'Puzzle 1!',
					font = 'times 16 bold',
					background = button_bg,
					command = self._button_1)
		
		self._puzzle_1.grid(row=1,column=0, padx=10, pady = 10,
				sticky = tk.N + tk.S + tk.E + tk.W)

		self._puzzle_2 = tk.Button(master = self._window,
					text = 'Puzzle 2!',
					font = 'times 16 bold',
					background = button_bg,
					command = self._button_2)
		
		self._puzzle_2.grid(row=1,column=1,padx = 10, pady = 10,
				sticky = tk.N + tk.S + tk.E + tk.W)

		self._puzzle_3 = tk.Button(master = self._window,
					text = 'Puzzle 3!',
					font = 'times 16 bold',
					background = button_bg,
					command = self._button_3)

		self._puzzle_3.grid(row=1,column=2,padx=10,pady=10,
				sticky = tk.N + tk.S + tk.W + tk.E)
	
		self._window.columnconfigure(0, weight=1)
		self._window.columnconfigure(0, weight=1)
		self._window.columnconfigure(0, weight=1)

		self._window.mainloop()		
		
	def _button_1(self):
		self.board = 'A'
		self._window.destroy()
	
	def _button_2(self):
		self.board = 'B'
		self._window.destroy()
	
	def _button_3(self):
		self.board = 'C'
		self._window.destroy()
