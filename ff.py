from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ExtendedQLabel(QLabel):
    def __init(self, parent):
        super().__init__(parent)

    clicked = pyqtSignal()

    def mousePressEvent(self, ev):
        self.clicked.emit()

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent=parent)

    def findlabel(self,n):

        hild = self.findChild(QLabel, "label{}".format(n))
        return hild

import numpy as np

