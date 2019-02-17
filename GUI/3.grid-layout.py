''' 
Grid Layout Manager
	The grid layout manager arranges widget in a two-dimensional table that consists of several rows and columns. The table acts as a template for the widgets to be placed into. The grid layout can be accessed by using the 'grid()' method. Thus, using the grid layout means that the programmer specifies the row and column number where he/she needs the widget to be placed in the root window.

Syntax:
<widget name>.grid(row=<row number>, column=<column number>)

'''

from tkinter import *

l = ['Name', 'Country', 'Contact', 'Parentage', 'District', 'Address']

root = Tk(className = "Layout")

i = 0
for x in l:
	Label(text = x, width = 10).grid(row = i, column = 0)
	Entry(width = 20).grid(row = i, column = 1)
	i += 1
Button(text='Submit', width=17).grid(row = i, column = 1)
root.mainloop()
