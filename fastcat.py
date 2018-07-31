import sys
import os
import json
import glob
from collections import OrderedDict
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from record import Record
from inputForm import InputForm
from fileLoader import *

class MyMainWindow(QMainWindow):

  def __init__(self, parent=None):


    self.configfile = ""
    self.workingpath = "."

    super(MyMainWindow, self).__init__(parent)
    self.statusBar()
    self.myMenuBar()
    self.recordMenu.setDisabled(True)
    
  def loadDefaults(self):
    self.profile_widget = LoadProfileSelector()
    self.configfile = self.profile_widget.configfile

  def nextBtnAction(self):
    try:
      self.workingpath
    except AttributeError:
      return
    else:
      if self.todolist_index == len(self.todolist) - 1:
        return
      else:
        self.todolist_index += 1
        self.setNextFile()

  def prevBtnAction(self):
    try:
      self.workingpath
    except AttributeError:
      return
    else:
      if self.todolist_index == 0:
        return
      else:
        self.todolist_index -= 1
        self.setNextFile()
  
  def setNextFile(self):
    self.form_widget.setParent(None)
    self.currentfile = self.todolist[self.todolist_index]
    self.currentfile_abs = os.path.join(self.workingpath, self.currentfile)
    self.makeNewForm()

  def makeNewForm(self):
    self.form_widget = InputForm(self.configfile, self.workingpath, self.currentfile, mode='new') 
    self.setCentralWidget(self.form_widget)
    self.setWindowTitle(self.currentfile_abs)
  
  def editForm(self):
    exportdata = self.form_widget.exportData
    self.form_widget = InputForm(self.configfile, self.workingpath, self.currentfile, mode='edit') 
    self.setCentralWidget(self.form_widget)
    self.setWindowTitle(self.currentfile_abs)
  
  def saveCloseForm(self):
    print(self.form_widget.exportData)
    exportdata = self.form_widget.exportData
    saveRecord(self, exportdata)
    self.form_widget.setParent(None)
    self.currentfile = self.todolist[self.todolist_index]
    self.currentfile_abs = os.path.join(self.workingpath, self.currentfile)
    self.makeNewForm()

  def openPath(self):
    self.workingpath = QFileDialog.getExistingDirectory(None, 'Select a folder:', '.', QFileDialog.ShowDirsOnly)
    self.todolist = Lister(self.workingpath).imagelist
    self.todolist_index = 0
    self.recordMenu.setDisabled(False)
    self.todolist = Lister(self.workingpath).imagelist
    self.currentfile = self.todolist[self.todolist_index]
    self.currentfile_abs = os.path.join(self.workingpath, self.currentfile)
    self.makeNewForm()
  

  def myMenuBar(self):
    
    exitAct = QAction('&Exit', self)        
    exitAct.setShortcut('Ctrl+Q')
    exitAct.setStatusTip('Exit application')
    exitAct.triggered.connect(qApp.quit)
    
    loadDirAct = QAction('&Open Working Directory', self)
    loadDirAct.setShortcut('Ctrl+O')
    loadDirAct.setStatusTip('Open a working directory')
    loadDirAct.triggered.connect(self.openPath)
    
    loadDefaultsAct = QAction('&Load Default Profile', self)
    loadDefaultsAct.setShortcut('Ctrl+D')
    loadDefaultsAct.setStatusTip('Load a JSON file to set a default profile')
    loadDefaultsAct.triggered.connect(self.loadDefaults)
    
    nextImgAct = QAction('&Next Image in Working Directory', self)
    nextImgAct.setShortcut('Ctrl+N')
    nextImgAct.setStatusTip('Load the next image in the todo list')
    nextImgAct.triggered.connect(self.nextBtnAction)
    
    
    prevImgAct = QAction('&Prev Image in Working Directory', self)
    prevImgAct.setShortcut('Ctrl+P')
    prevImgAct.setStatusTip('Load the previous image in the todo list')
    prevImgAct.triggered.connect(self.prevBtnAction)
    
    saveRecordAct = QAction('&Save Current Record', self)
    saveRecordAct.setShortcut('Ctrl+S')
    saveRecordAct.setStatusTip('Save JSON record')
    saveRecordAct.triggered.connect(self.saveCloseForm)
    
    editRecordAct = QAction('&Edit Current Record', self)
    editRecordAct.setShortcut('Ctrl+E')
    editRecordAct.setStatusTip('Edit Record')
    editRecordAct.triggered.connect(self.editForm)
    
    self.menubar = self.menuBar()
    self.fileMenu = self.menubar.addMenu('&File')
    self.recordMenu = self.menubar.addMenu('&Record')
    self.recordMenu.addAction(nextImgAct)
    self.recordMenu.addAction(prevImgAct)
    self.recordMenu.addAction(editRecordAct)
    self.fileMenu.addAction(loadDefaultsAct)
    self.fileMenu.addAction(saveRecordAct)
    self.fileMenu.addAction(loadDirAct)
    self.fileMenu.addAction(exitAct)

app = QApplication([])
foo = MyMainWindow()
foo.show()
sys.exit(app.exec_())