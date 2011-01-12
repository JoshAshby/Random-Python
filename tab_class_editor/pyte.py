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
       fileBox.addWidget(self.saveAsButton)
       self.connect(self.saveAsButton, QtCore.SIGNAL("clicked()"), self.saveAs)

       self.saveButton = QtGui.QPushButton(self)
       self.saveButton.setText("Save") 
       fileBox.addWidget(self.saveButton)
       self.connect(self.saveButton, QtCore.SIGNAL("clicked()"), self.save)

       self.openButton = QtGui.QPushButton(self)
       self.openButton.setText("Open") 
       fileBox.addWidget(self.openButton)
       self.connect(self.openButton, QtCore.SIGNAL("clicked()"), self.openFile)

       mainLayout.addWidget(self.editor, 200)

       CurrentfileName = ''

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
          event.accept()


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.__Dir = os.path.dirname(sys.argv[0])
        self.icons =  os.path.join(self.__Dir, 'icons/')

        self.resize(640, 480)
        self.setWindowTitle('PyTe v2')
        self.setWindowIcon(QtGui.QIcon(self.icons+'pyte.png'))


        self.mainTabWidget = QtGui.QTabWidget(self)
        self.mainTabWidget.setTabsClosable(True)
        self.mainTabWidget.setMovable(True)
        self.setCentralWidget(self.mainTabWidget)

        newEditor = editor(self, self)
        newTab = self.mainTabWidget.addTab(newEditor, QtGui.QIcon(self.icons+'pyte.png'), "Pyte")
        self.mainTabWidget.setCurrentIndex(newTab)

        self.statusBar()

        closeTab = QtGui.QAction(QtGui.QIcon(self.icons+'exit.png'), 'Close Tab', self)
        closeTab.setStatusTip('Close Tab')
        self.connect(closeTab, QtCore.SIGNAL('triggered()'), self.closetab)

        newtab = QtGui.QAction(QtGui.QIcon(self.icons+'add.png'), 'Add Tab', self)
        newtab.setStatusTip('Add Tab')
        newtab.connect(newtab,QtCore.SIGNAL('triggered()'), self.codetab)

        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(newtab)
        file.addAction(closeTab)

        #if there is a argument passed then try to open it as a file
        if (len(sys.argv) > 1):
            fn = sys.argv[1]

            fileName = str(fn)

            try:
                self.editor.openArg(fileName)
                self.editor.title(fileName)
            except:
                return

            self.setWindowTitle(fileName+" - PyTe v2")

        else:
            pass

    def closetab(self):
        self.mainTabWidget.removeTab(self.mainTabWidget.currentIndex())

    def codetab(self):
        newEditor = editor(self, self)
        newTab = self.mainTabWidget.addTab(newEditor, QtGui.QIcon(self.icons+'tex.png'), "Code Editor")
        self.mainTabWidget.setCurrentIndex(newTab)

#start the app
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
