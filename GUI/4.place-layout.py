'''
Place Layout Manager
	The place layout or geometry manager arranges the widgets of the GUI at specific positions that are provided by the programmer as absolute values. The 'place()' method is used to access this layout manager. This method takes certain options such as X, Y, width etc. that describe the positioning and size of the widget.

Syntax of Place Manager
<widget name>.place(options...)
'''

from tkinter import *

root = Tk(className = 'Layout')

Button(root, text = 'White', bg = 'white', fg = 'black').place(x = 20, y = 30, width = 160, height = 30)
Button(root, text = 'Orange', bg = 'orange', fg = 'brown').place(x = 20, y = 70, width = 160, height = 30)
Button(root, text = 'Red', bg = 'red', fg = 'black').place(x = 20, y = 110, width = 160, height = 30)

root.mainloop()
