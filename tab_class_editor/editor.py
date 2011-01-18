#!/usr/bin/python
import sys, os
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, Qsci
from PyQt4.Qsci import QsciScintilla, QsciScintillaBase, QsciLexerPython

class editor(QtGui.QWidget):
   def __init__(self, parent, main):
       QtGui.QWidget.__init__(self)

       self.__Dir = os.path.dirname(sys.argv[0])
       self.icons =  os.path.join(self.__Dir, 'icons/')

       self.main = main

       mainLayout = QtGui.QVBoxLayout()
       mainLayout.setContentsMargins(0, 0, 0, 0)
       mainLayout.setSpacing(0)
       self.setLayout(mainLayout)

       self.editor = QsciScintilla(self)

       self.font = QtGui.QFont()
       self.font.setFamily("Consolas")
       self.font.setFixedPitch(True)
       self.font.setPointSize(10)
       self.fm = QtGui.QFontMetrics(self.font)
       self.editor.setFont(self.font)
       self.editor.setMarginsFont(self.font)
       self.editor.setMarginWidth(0, self.fm.width( "0000" ))

       self.editor.setMarginLineNumbers(0, True)
       self.editor.setUtf8(True)
       self.editor.setFolding(QsciScintilla.BoxedTreeFoldStyle)
       self.editor.setBraceMatching(QsciScintilla.SloppyBraceMatch)
       self.editor.setCaretLineVisible(True)
       self.editor.setCaretLineBackgroundColor(QtGui.QColor('#bfbfbf'))
       self.editor.setMarginsBackgroundColor(QtGui.QColor('#3e3e3e'))
       self.editor.setMarginsForegroundColor(QtGui.QColor('#aaff00'))
       self.editor.setFoldMarginColors(QtGui.QColor('#ff0000'),QtGui.QColor('#000000'))
       lexer = QsciLexerPython()
       self.editor.setLexer(lexer)

       fileBox = QtGui.QHBoxLayout()
       mainLayout.addLayout(fileBox, 0)

       self.saveAsButton = QtGui.QPushButton(self)
       self.saveAsButton.setText("Save As")
       self.saveAsButton.setIcon(QtGui.QIcon(self.icons+'save.png')) 
       fileBox.addWidget(self.saveAsButton)
       self.connect(self.saveAsButton, QtCore.SIGNAL("clicked()"), self.saveAs)

       self.saveButton = QtGui.QPushButton(self)
       self.saveButton.setText("Save")
       self.saveButton.setIcon(QtGui.QIcon(self.icons+'save.png')) 
       fileBox.addWidget(self.saveButton)
       self.connect(self.saveButton, QtCore.SIGNAL("clicked()"), self.save)

       self.openButton = QtGui.QPushButton(self)
       self.openButton.setText("Open") 
       self.openButton.setIcon(QtGui.QIcon(self.icons+'open.png')) 
       fileBox.addWidget(self.openButton)
       self.connect(self.openButton, QtCore.SIGNAL("clicked()"), self.openFile)

       mainLayout.addWidget(self.editor, 200)

       self.CurrentfileName = ''

   def openFile(self):
      self.fn = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home', '')
      if self.fn.isEmpty():
          return
      self.fileName = str(self.fn)
      try:
          self.f = open(self.fileName,'r').read()
          self.editor.setText(self.f)
      except:
          return
      self.CurrentfileName = self.fileName

   def openArg(self, fileName):
      self.f = open(self.fileName,'r').read()
      self.editor.setText(self.f)

   def saveAs(self):
      self.fn = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '')
      try:
          self.f = open(str(self.fn),'w+r')
      except:
          return
      self.f.write(str(self.editor.text()))
      self.f.close()

   def getTitle(self):
      return self.CurrentfileName

   def save(self):
      try:
          self.f = open(self.CurrentfileName,'w+r')
      except:
          return
      self.f.write(str(self.editor.text()))
      self.f.close()

   def closeEvent(self, event):
      if (self.editor.isModified() == True):
          if (self.filename == ""):
              ret = QtGui.QMessageBox.warning(self, "PyTe",
                          "The Code has been modified.\n"
                          "Do you want to save your changes?",
                          QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard |
                          QtGui.QMessageBox.Cancel)
              if ret == QtGui.QMessageBox.Save:
                  self.fn = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '')
                  try:
                     self.f = open(str(self.fn),'w+r')
                  except:
                     return
                  self.f.write(str(self.text()))
                  self.f.close()
                  event.accept()
              elif ret == QtGui.QMessageBox.Cancel:
                  event.ignore()
      else:
          try:
              self.f = open(self.CurrentfileName,'w+r')
          except:
              return
          self.f.write(str(self.text()))
          self.f.close()
          event.accept()

