#!/usr/bin/env python
"""Simple Gui that uses the parserDom.py module
to find the value of different tags in real
time from opt.xml"""
from Tkinter import *
import tkSimpleDialog
import tkMessageBox
import parserDom
root = Tk()

debug = 0 #set to 1 to debug, 0 to run normally

main = Frame(root)
main.grid(column = 0, row = 0)

tagName = Entry(main)
tagName.grid(column = 0, row = 1, padx = 2, pady = 2)

tagVal = Label(main)
tagVal.grid(column = 0, row = 2, padx = 2, pady = 2)

bu = Button(main, command=root.destroy, text='Quit', width = '6')
bu.grid(column = 1, row = 0, padx = 2, pady = 2)

nextBu = Button(main, command=next(), text='Next', width='6')
nextBu.grid(column = 1, row = 0, padx = 2, pady = 2)

backBu = Button(main, command=back(), text='Back', width='6')
backBu.grid(column = 0, row = 0, padx = 2, pady = 2)

lb = Listbox(main)
lb.grid(column = 1, row = 1, padx = 2, pady = 2)

def update(*ignore):
   data = tagName.get()
   value = parserDom.findTag(data)
   if debug: print value #debug tag
   if data != '':
      tagVal['text'] = '%s : %s' %(data, value)
   else:
      tagVal['text'] = ''
   if parserDom.findNumberOfTags(data) != 0:
      num = parserDom.findNumberOfTags(data)
   num = parserDom.findTags(data)
   for a in num:
    lb.insert(END, a)
      
def next():
   data = tagName.get()
   value = parserDom.findNumberOfTags(data)
   if debug: print value #debug tag
   

def back():
   data = tagName.get()
   value = parserDom.findTag(data)
   if debug: print value #debug tag

root.bind('<Key>', update)

mainloop()
