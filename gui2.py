#!/usr/bin/env python
#import all needed libraries
from Tkinter import *
import sys
root = Tk()
y=0
x=0
def decease():
    x=y-1
    
def increase():
    x=y+1

if (len(sys.argv) > 1):
    fn = sys.argv[1]

toolbar = Frame(root)#create the tool bar
main = Frame(root)#create the main text area

bu = Button(toolbar, text="increase", width=6, command=increase, fg ="green", bg ="black",)#close button
bu.grid(column = 0, row = 0, padx=2, pady=2)

bu = Button(toolbar, text="decease", width=6, command=decease, fg ="green", bg ="black",)#close button
bu.grid(column = 1, row = 0, padx=2, pady=2)

toolbar.grid(column = 0, row = 0)#place the toolbar on a grid cell

la = Label(text=x)
la.grid(column = 2, row = 0, padx=2, pady=2)

mainloop()#loop the program