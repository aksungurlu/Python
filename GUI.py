#!/usr/bin/python

import Tkinter
from Tkinter import *
import tkMessageBox

top = Tkinter.Tk()

# Button to pop up
def upMessage():
   tkMessageBox.showinfo( "Hello Python", "Up Button Pressed")
   
def leftMessage():
   tkMessageBox.showinfo( "Hello Python", "Left Button Pressed")
   
def downMessage():
   tkMessageBox.showinfo( "Hello Python", "Down Button Pressed")
   
def rightMessage():
   tkMessageBox.showinfo( "Hello Python", "Right Button Pressed")

B_up = Tkinter.Button(top, text = u'\u25b2', command = upMessage).pack()
B_left = Tkinter.Button(top, text = u'\u24b2', command = leftMessage).pack()
B_down = Tkinter.Button(top, text = u'\u23b2', command = downMessage).pack()
B_right = Tkinter.Button(top, text = u'\u22b2', command = rightMessage).pack()

#B_up.pack()
#B.place(bordermode=OUTSIDE, relheight=0.2, relwidth=0.5)

#B.grid(row=2,column=2)
top.mainloop()
