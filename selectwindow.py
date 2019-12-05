# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Selection(object):
    def setupUi(self, Selection):
        Selection.setObjectName("Selection")
        Selection.resize(289, 279)
        self.centralwidget = QtWidgets.QWidget(Selection)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 291, 231))
        self.listWidget.setObjectName("listWidget")
        self.selectbutton = QtWidgets.QPushButton(self.centralwidget)
        self.selectbutton.setGeometry(QtCore.QRect(-10, 230, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.selectbutton.setFont(font)
        self.selectbutton.setObjectName("selectbutton")
        Selection.setCentralWidget(self.centralwidget)

        self.retranslateUi(Selection)
        QtCore.QMetaObject.connectSlotsByName(Selection)

    def retranslateUi(self, Selection):
        _translate = QtCore.QCoreApplication.translate
        Selection.setWindowTitle(_translate("Selection", "MainWindow"))
        self.selectbutton.setText(_translate("Selection", "Select"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Selection = QtWidgets.QMainWindow()
    ui = Ui_Selection()
    ui.setupUi(Selection)
    Selection.show()
    sys.exit(app.exec_())
