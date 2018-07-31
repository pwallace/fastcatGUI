import json
import sys
import os
import fnmatch
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon

def loadRecord(self, configfile):
  loadrecord = dict()
  with open(configfile) as cf:
    loadrecord = json.load(cf)
  return loadrecord

def saveRecord(self, exportData):
  basefilename = self.currentfile_abs
  if basefilename != '':
    savefile = str(os.path.splitext(basefilename)[0])+ ".json"
  elif exportData['identifier'] != '':
    savefile = str(exportData['identifier']) + ".json"
  else:
    savefile = "noname.junk.json"
  with open(savefile, 'w') as outfile:
    json.dump(exportData, outfile)
  print(exportData)

### LOAD PROFILE SELECTOR

class LoadProfileSelector(QWidget):

  def __init__(self):
    super(LoadProfileSelector, self).__init__()
    self._profilenames = []
    self._jsonlist = fnmatch.filter(os.listdir('./defaults/'), '*.json')
    self.makeProfileList()

  def makeProfileList(self):
    for f in self._jsonlist:
      self._profilenames.append(os.path.splitext(f)[0].title())
    item, okPressed = QInputDialog.getItem(self, "Select a Collection Profile","Collection:", self._profilenames, 0, False)
    if okPressed and item:
      item = item.lower() + ".json"
      self._configfile = os.path.join('./defaults/', item)
     
  @property
  def configfile(self):
    configfile = self._configfile
    return configfile

### MAKE LISTS

class Lister():
    def __init__(self, workingpath):
      super(Lister, self).__init__()
      self._filetypes = ['.jpg', '.JPG', '.jpeg', '.JP2', '.jp2', '.tif', '.tiff', '.TIF','.TIFF']
      self._workingpath = workingpath
      self._filelist = fnmatch.filter(os.listdir(self._workingpath), '*.*')
      self._jsonlist = fnmatch.filter(os.listdir(self._workingpath), '*.json')
      self._filterlist = []
      self._imagelist = []

    def getlist(self):
      for filename in self._filelist:
        for filetype in self._filetypes:
          if filename.endswith(filetype):
            self._filterlist.append(filename)
      todolist = self._filterlist
      return todolist
      
    @property
    def imagelist(self):
      mylist = self.getlist()
      return mylist