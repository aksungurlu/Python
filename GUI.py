#!/usr/bin/python

import Tkinter
from Tkinter import *
import tkMessageBox

speed = 0
direction = 0

top = Tkinter.Tk()

# Button to pop up
def upMessage():
	global speed
	if speed < 1:
		speed += 0.1
   
def leftMessage():
	global direction
	if direction > -1:
		direction -= 0.1
   
def downMessage():
	global speed
	if speed > -1:
		speed -= 0.1
   
def rightMessage():
	global direction
	if direction < 1:
		direction += 0.1
   
def showMessage():
   tkMessageBox.showinfo( "Hello Python", "Speed:"+str(speed)+" Direction:"+str(direction))

B_up = Tkinter.Button(top, text = u'\u25b2', command = upMessage).grid(row=1,column=2)
B_left = Tkinter.Button(top, text = u'\u25c0', command = leftMessage).grid(row=2,column=1)
B_down = Tkinter.Button(top, text = u'\u25bc', command = downMessage).grid(row=2,column=2)
B_right = Tkinter.Button(top, text = u'\u25b6', command = rightMessage).grid(row=2,column=3)
B_show = Tkinter.Button(top, text = "Show", command = showMessage).grid(row=4,column=2,rowspan=3)

#B_up.pack()
#B.place(bordermode=OUTSIDE, relheight=0.2, relwidth=0.5)

#B.grid(row=2,column=2)
top.mainloop()
