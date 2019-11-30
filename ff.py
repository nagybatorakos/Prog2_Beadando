from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ExtendedQLabel(QLabel):
    def __init(self, parent):
        super().__init__(parent)

    clicked = pyqtSignal()

    def mousePressEvent(self, ev):
        self.clicked.emit()
