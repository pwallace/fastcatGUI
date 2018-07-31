import os
from collections import OrderedDict

class Record(object):
  
  def __init__(self, recordData):
    self._recordData = recordData
    return


  def dcrecord(self):
    dcrecord = OrderedDict()
    dcrecord['idprefix'] = self._recordData['idprefix']
    if self._recordData['filename'] == '':
      dcrecord['identifier'] = self._recordData['identifier']
    else:
      dcrecord['identifier'] = self._recordData['idprefix'] + "_" + os.path.splitext(self._recordData['filename'])[0]
  
    dcrecord['filename'] = self._recordData['filename']
    dcrecord['collection'] = self._recordData['collection']
    dcrecord['title'] = self._recordData['title']
    dcrecord['creator'] = self._recordData['creator']
    dcrecord['date'] = self._recordData['date']
    dcrecord['description'] = self._recordData['description']
    dcrecord['format'] = self._recordData['format']
    dcrecord['type'] = self._recordData['type']
    dcrecord['mediatype'] = self._recordData['mediatype']
    dcrecord['rights'] = self._recordData['rights']
    dcrecord['subject'] = self._recordData['subject']
    return dcrecord

  def exportrecord(self):
    exportrecord = OrderedDict()
    exportrecord['idprefix'] = self._recordData['idprefix']
    if self._recordData['filename'] == '':
      exportrecord['identifier'] = self._recordData['identifier']
    else:
      exportrecord['identifier'] = self._recordData['idprefix'] + "_" + os.path.splitext(self._recordData['filename'])[0]
  
    exportrecord['filename'] = self._recordData['filename']
    exportrecord['collection'] = self._recordData['collection']
    exportrecord['title'] = self._recordData['title']
    exportrecord['creator'] = self._recordData['creator']
    exportrecord['date'] = self._recordData['date']
    exportrecord['description'] = self._recordData['description']
    exportrecord['format'] = self._recordData['format']
    exportrecord['type'] = self._recordData['type']
    exportrecord['mediatype'] = self._recordData['mediatype']
    exportrecord['rights'] = self._recordData['rights']
    exportrecord['subject'] = self._recordData['subject']
    return exportrecord

  def idprefix(self):
    return self._recordData['idprefix']

  def filename(self):
    return self._recordData['filename']

  def identifier(self):
    return self._recordData['identifier']

  def collection(self):
    return self._recordData['collection']

  def title(self):
    return self._recordData['title']

  def creator(self):
    return self._recordData['creator']

  def date(self):
    return self._recordData['date']

  def description(self):
    return self._recordData['description']

  def format(self):
    return self._recordData['format']

  def dctype(self):
    return self._recordData['type']

  def mediatype(self):
    return self._recordData['mediatype']

  def rights(self):
    return self._recordData['rights']