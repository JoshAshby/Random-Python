#!/usr/bin/env python
"""Simple Gui that uses the parser.py module
to find the value of different tags in real
time from opt.xml. A precursor to finder-dom"""
from Tkinter import *
import tkSimpleDialog
import tkMessageBox
import parser
root = Tk()

debug = 0 #set to 1 to debug, 0 to run normally

main = Frame(root)
main.grid(column = 0, row = 0)

text = Entry(main)
text.grid(column = 0, row = 0, padx = 2, pady = 2)

textin = Label(main)
textin.grid(column = 0, row = 1, padx = 2, pady = 2)

bu = Button(main, command=root.destroy, text='Quit', width = '6')
bu.grid(column = 1, row = 0, padx = 2, pady = 2) 

def update(*ignore):
   data = text.get()
   parser.tagType = data
   parser.update()
   value = parser.tagValue
   if debug: print value #debug tag
   if data != '':
      textin['text'] = '%s : %s' %(data, value)
   else:
      textin['text'] = ''
   

root.bind('<Key>', update)

mainloop()
