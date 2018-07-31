from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ShowPic(QLabel):

### BEGIN INIT
    def __init__(self, currentfile):
        super(ShowPic, self).__init__()
       
##### Makes shows & scales image
        pixmap = QPixmap(currentfile)
        pixbox = pixmap.scaled(800, 400, Qt.KeepAspectRatio)
        self.setPixmap(pixbox)