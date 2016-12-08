#!/usr/bin/python

import Tkinter
from Tkinter import *
import tkMessageBox

top = Tkinter.Tk()

# Button to pop up
def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
B.place(bordermode=OUTSIDE, height=100, width=100)

#B.grid(row=2,column=2)
top.mainloop()
