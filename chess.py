import tkinter as tk

class DragManager():
	def add_dragable(self, widget):
		widget.bind("<ButtonPress-1>", self.on_start)
		widget.bind("<B1-Motion>", self.on_drag)
		widget.bind("<ButtonRelease-1>", self.on_drop)
		widget.configure(cursor="hand1")
	
	def on_start(self, event):
		pass

	def on_drag(self, event):
		pass

	def on_drop(self, event):  
		x,y = event.widget.winfo_pointerxy()
		target = event.widget.winfo_containing(x,y)
		try:
			target.configure(image=event.widget.cget("image"))
		except:
			pass

class GameBoard(tk.Frame):
	def __init__(self, parent, rows=8, columns=8, size=72, color1="#EEEED5", color2="#7D945D"):
		'''size is the size of a square, in pixels'''
		
		self.rows = rows
		self.columns = columns
		self.size = size
		self.color1 = color1
		self.color2 = color2
		self.pieces = {}

		canvas_width = columns * size
		canvas_height = rows * size

		tk.Frame.__init__(self, parent)
		self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
    	                        width=canvas_width, height=canvas_height, background="bisque")
		self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

	def addpiece(self, name, image, row, column):
		'''Add a piece to the playing board'''
		#self.canvas.create_image(0,0, image=image, tags=(name, "piece"), anchor="c")
		self.pack()
		self.placepiece(name, row, column)

	def placepiece(self, name, row, column):
		'''Place a piece at the given row/column'''
		self.pieces[name] = (row, column)
		x0 = (column * self.size) + int(self.size/2)
		y0 = (row * self.size) + int(self.size/2)
		self.canvas.coords(name, x0, y0)	


# image comes from the silk icon set which is under a Creative Commons
# license. For more information see http://www.famfamfam.com/lab/icons/silk/
imagedata = '''R0lGODlhEAAQAOeSAKx7Fqx8F61/G62CILCJKriIHM+HALKNMNCIANKKANOMALuRK7WOVLWPV9eR
    ANiSANuXAN2ZAN6aAN+bAOCcAOKeANCjKOShANKnK+imAOyrAN6qSNaxPfCwAOKyJOKyJvKyANW0
	    R/S1APW2APW3APa4APe5APm7APm8APq8AO28Ke29LO2/LO2/L+7BM+7BNO6+Re7CMu7BOe7DNPHA
		    P+/FOO/FO+jGS+/FQO/GO/DHPOjBdfDIPPDJQPDISPDKQPDKRPDIUPHLQ/HLRerMV/HMR/LNSOvH
			    fvLOS/rNP/LPTvLOVe/LdfPRUfPRU/PSU/LPaPPTVPPUVfTUVvLPe/LScPTWWfTXW/TXXPTXX/XY
				    Xu/SkvXZYPfVdfXaY/TYcfXaZPXaZvbWfvTYe/XbbvHWl/bdaPbeavvadffea/bebvffbfbdfPvb
					    e/fgb/Pam/fgcvfgePTbnfbcl/bfivfjdvfjePbemfjelPXeoPjkePbfmvffnvbfofjlgffjkvfh
						    nvjio/nnhvfjovjmlvzlmvrmpvrrmfzpp/zqq/vqr/zssvvvp/vvqfvvuPvvuvvwvfzzwP//////
							    ////////////////////////////////////////////////////////////////////////////
								    ////////////////////////////////////////////////////////////////////////////
									    ////////////////////////////////////////////////////////////////////////////
										    ////////////////////////////////////////////////////////////////////////////
											    ////////////////////////////////////////////////////////////////////////////
												    /////////////////////////////////////////////////////yH+FUNyZWF0ZWQgd2l0aCBU
													    aGUgR0lNUAAh+QQBCgD/ACwAAAAAEAAQAAAIzAD/CRxIsKDBfydMlBhxcGAKNIkgPTLUpcPBJIUa
														    +VEThswfPDQKokB0yE4aMFiiOPnCJ8PAE20Y6VnTQMsUBkWAjKFyQaCJRYLcmOFipYmRHzV89Kkg
															    kESkOme8XHmCREiOGC/2TBAowhGcAyGkKBnCwwKAFnciCAShKA4RAhyK9MAQwIMMOQ8EdhBDKMuN
																    BQMEFPigAsoRBQM1BGLjRIiOGSxWBCmToCCMOXSW2HCBo8qWDQcvMMkzCNCbHQga/qMgAYIDBQZU
																	    yxYYEAA7'''



if __name__ == "__main__":
	root = tk.Tk()
	board = GameBoard(root)
	dm = DragManager();
	board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
	player1 = tk.Label(text="P")
	#player1 = tk.PhotoImage(data=imagedata)
	dm.add_dragable(player1)
	board.addpiece("player1", player1, 2,2)
	root.mainloop()
