from tkinter import *
from tkinter.filedialog import askopenfilename

def handler():
	print(askopenfilename())


root = Tk(className = 'File Open Dialog')
root.geometry('250x30')
Button(root, text='Open File', bg='orange',fg='brown', command = handler).pack()
root.mainloop() 
