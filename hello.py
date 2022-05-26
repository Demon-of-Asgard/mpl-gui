from argparse import Action
from tkinter import *


root = Tk()

def print_name():
    return print ('Hello Manu !!!')



mylabel = Label(root, text = 'Hello!!!')
button = Button(root, text= 'press', command=print_name)

mylabel.grid(row = 0, column = 1)
button.grid(row = 1, column = 1)

root.mainloop()