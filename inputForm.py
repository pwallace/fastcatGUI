import sys
import os
import json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from record import Record
from fileLoader import *
from showPic import ShowPic


class InputForm(QWidget):

### BEGIN INIT
  def __init__(self, configfile, workingpath, currentfile, mode):
    super(InputForm, self).__init__()
    
    
#       formBoxLayout = self.spawnForm()
#### Makes the todo list
##### Makes form from defaults
    self.mode = mode
    if self.mode == 'new':
      self.loadWorkingRecord(configfile, workingpath, currentfile)
      formBoxLayout = self.spawnForm()
    elif self.mode == 'edit':
      self.loadWorkingRecord(configfile, workingpath, currentfile)
      self.currentfile_abs = self._currentfile_abs
      formBoxLayout = self.editForm()
    self.setLayout(formBoxLayout)

##### Draw the window
    self.show()

  def loadWorkingRecord(self, configfile, workingpath, currentfile):
    jsonfile = str(os.path.splitext(currentfile)[0]) + ".json"
    if jsonfile in os.listdir(workingpath):
      configfile = jsonfile
      loadedrecord = loadRecord(self, configfile)
    else:
      loadedrecord = loadRecord(self, configfile)
      loadedrecord['filename'] = currentfile
    self._currentfile_abs = os.path.join(workingpath, currentfile)
    self.recordData = Record(loadedrecord)
    return self.recordData
      
##### Define form fields from default configfile
  def spawnForm(self):
    fbox = QFormLayout()
    self.formkeys = dict()
    self.formvalues = dict()
    self.newlistvalue = dict()
    self.formData = self.recordData.dcrecord() #change to dcrecord for debug
    fbox.addRow(ShowPic(self._currentfile_abs))
    for key in self.formData:
      if type(self.formData[key]) == list:
        self._listedvalues = set(self.formData[key])
        for item in self._listedvalues:
          self.formkeys[key] = str(key)
          self.formvalues[key] = QLabel(item)
          fbox.addRow(self.formkeys[key], self.formvalues[key])
        self.newlistvalue[key] = QLineEdit(self)
        fbox.addRow(self.formkeys[key], self.newlistvalue[key])
      elif self.formData[key] == None or self.formData[key] == '':
        self.formkeys[key] = str(key)
        self.formvalues[key] = ''
        self.formvalues[key] = QLineEdit(self)
        fbox.addRow(self.formkeys[key], self.formvalues[key])
      elif type(self.formData[key]) != list:
        self.formkeys[key] = str(key)
        self.formvalues[key] = QLabel(self.formData[key])
        fbox.addRow(self.formkeys[key], self.formvalues[key])
    return fbox
  
    
  def editForm(self):
    fbox = QFormLayout()
    self.formkeys = dict()
    self.formvalues = dict()
    self.newlistvalue = dict()
    lockedkeys = ['idprefix', 'identifier', 'filename']
    self.formData = self.recordData.exportrecord() #change to dcrecord for debug
    fbox.addRow(ShowPic(self._currentfile_abs))
    for key in self.formData:
      if key in lockedkeys:
        self.formkeys[key] = str(key)
        self.formvalues[key] = ''
        self.formvalues[key] = QLabel(self.formData[key])
        fbox.addRow(self.formkeys[key], self.formvalues[key])
      elif type(self.formData[key]) == list:
        self._templist = str()
        self._listedvalues = set(self.formData[key])
        for item in self._listedvalues:
          self._templist = self._templist + ', ' + item
          self.formkeys[key] = str(key)
        self.formvalues[key] = QLineEdit(self)
        self.formvalues[key].setText(self._templist)
        fbox.addRow(self.formkeys[key], self.formvalues[key])
      elif self.formData[key] == None or self.formData[key] == '':
        self.formkeys[key] = str(key)
        self.formvalues[key] = ''
        self.formvalues[key] = QLineEdit(self)
        fbox.addRow(self.formkeys[key], self.formvalues[key])
      elif type(self.formData[key]) != list:
        self.formkeys[key] = str(key)
        self.formvalues[key] = QLineEdit(self)
        self.formvalues[key].setText(self.formData[key])
        fbox.addRow(self.formkeys[key], self.formvalues[key])
    return fbox

  @property
  def exportData(self):
    exportData = dict()
    if self.mode == 'edit':
      for key in self.formData:
        if type(self.formData[key]) == list:
          if self.formvalues[key].text() != '':
            self.formData[key] = []
            listdata = self.formvalues[key].text().split(',')
            for listdatum in listdata:
              self.formData[key].append(listdatum.strip())
        else:
          self.formData[key] = self.formvalues[key].text()
    elif self.mode == 'new':
      for key in self.formData:
        if type(self.formData[key]) == list:
          if self.newlistvalue[key].text() != '':
            self.formData[key].append(self.newlistvalue[key].text())
        else:
          self.formData[key] = self.formvalues[key].text()
    else:
      for key in self.formData:
        self.formData[key] = self.formvalues[key].text()
    exportData = self.formData
    return exportData
### END DEFINE ACTIONS