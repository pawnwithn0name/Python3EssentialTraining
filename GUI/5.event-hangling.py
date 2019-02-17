''' 
After the root window loads on the system, it waits for the occurence of some event. These events can be button clicks, motion of the mouse, button release, etc. These events are handled by defining functions that are executed in case an event occurs.
'''

from tkinter import *

def handler1():
	print('White')

def handler2():
	print('Orange')

def handler3():
	print('Red')

root = Tk(className = 'Event')
Button(root, text='White', bg='white',fg='black', command = handler1).pack(fill = X, padx = 15)
Button(root, text='Orange', bg='orange',fg='brown', command = handler2).pack(fill = X, padx = 15, pady =15)
Button(root, text='Red', bg='red',fg='black', command = handler3).pack( fill = X, padx = 15)

root.mainloop()
