'''
The Pack Layout Manager
Simlest to implement out of all the three managers and arranges the widgets relative to each other

syntax of pack() method
<widget name>.pack(options...)
Button.pack(fill=X, padx = 15)
'''

from tkinter import *

root = Tk()
Button(root, text='White', bg='white',fg='black').pack()
Button(root, text='Orange', bg='orange',fg='brown').pack()
Button(root, text='Red', bg='red',fg='black').pack()
root.mainloop()
