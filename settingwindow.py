# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 446)
        MainWindow.setMaximumSize(QtCore.QSize(500, 446))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.player_add_button = QtWidgets.QPushButton(self.centralwidget)
        self.player_add_button.setGeometry(QtCore.QRect(330, 150, 31, 31))
        self.player_add_button.setObjectName("player_add_button")
        self.playername = QtWidgets.QLabel(self.centralwidget)
        self.playername.setGeometry(QtCore.QRect(20, 120, 201, 91))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.playername.setFont(font)
        self.playername.setObjectName("playername")
        self.player1 = QtWidgets.QLabel(self.centralwidget)
        self.player1.setGeometry(QtCore.QRect(20, 250, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.player1.setFont(font)
        self.player1.setAlignment(QtCore.Qt.AlignCenter)
        self.player1.setObjectName("player1")
        self.namebox = QtWidgets.QTextEdit(self.centralwidget)
        self.namebox.setGeometry(QtCore.QRect(220, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.namebox.setFont(font)
        self.namebox.setPlaceholderText("")
        self.namebox.setObjectName("namebox")
        self.player2 = QtWidgets.QLabel(self.centralwidget)
        self.player2.setGeometry(QtCore.QRect(200, 250, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.player2.setFont(font)
        self.player2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.player2.setAlignment(QtCore.Qt.AlignCenter)
        self.player2.setObjectName("player2")
        self.playingtime = QtWidgets.QLabel(self.centralwidget)
        self.playingtime.setGeometry(QtCore.QRect(20, 20, 211, 91))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.playingtime.setFont(font)
        self.playingtime.setObjectName("playingtime")
        self.playbutton = QtWidgets.QPushButton(self.centralwidget)
        self.playbutton.setGeometry(QtCore.QRect(10, 340, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.playbutton.setFont(font)
        self.playbutton.setObjectName("playbutton")
        self.timebox = QtWidgets.QComboBox(self.centralwidget)
        self.timebox.setGeometry(QtCore.QRect(220, 50, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.timebox.setFont(font)
        self.timebox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.timebox.setObjectName("timebox")
        self.timebox.addItem("")
        self.timebox.addItem("")
        self.timebox.addItem("")
        self.timebox.addItem("")
        self.timebox.addItem("")
        self.timebox.addItem("")
        self.timebox.addItem("")
        self.picture = QtWidgets.QLabel(self.centralwidget)
        self.picture.setEnabled(True)
        self.picture.setGeometry(QtCore.QRect(0, -10, 761, 571))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("background.jpg"))
        self.picture.setScaledContents(True)
        self.picture.setObjectName("picture")
        self.picture.raise_()
        self.player_add_button.raise_()
        self.playername.raise_()
        self.player1.raise_()
        self.namebox.raise_()
        self.player2.raise_()
        self.playingtime.raise_()
        self.playbutton.raise_()
        self.timebox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
##############################################################################
#my code:
        MainWindow.setWindowTitle('Settings')
        # self.player_add_button.clicked.connect(self.addPlayer)
        # self.h = 0
        # self.time = self.timebox.currentText()
        # self.timebox.currentTextChanged.connect(self.getTime)
        # from Play_Chess import Setting
        # self.player_add_button.clicked.connect(Setting.addPlayer(Setting))



##############################################################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.player_add_button.setText(_translate("MainWindow", "OK"))
        self.playername.setText(_translate("MainWindow", "Player name:"))
        self.player1.setText(_translate("MainWindow", "Player 1"))
        self.player2.setText(_translate("MainWindow", "Player 2"))
        self.playingtime.setText(_translate("MainWindow", "Playing time:"))
        self.playbutton.setText(_translate("MainWindow", "Play"))
        self.timebox.setCurrentText(_translate("MainWindow", "1"))
        self.timebox.setItemText(0, _translate("MainWindow", "1"))
        self.timebox.setItemText(1, _translate("MainWindow", "5"))
        self.timebox.setItemText(2, _translate("MainWindow", "10"))
        self.timebox.setItemText(3, _translate("MainWindow", "15"))
        self.timebox.setItemText(4, _translate("MainWindow", "20"))
        self.timebox.setItemText(5, _translate("MainWindow", "25"))
        self.timebox.setItemText(6, _translate("MainWindow", "30"))
##############################################################################
#my code:

    # def addPlayer(self):
    #     self.h+=1
    #     if self.h>2:
    #         self.h=1
    #     if self.h==1:
    #         name=self.namebox.toPlainText()
    #         self.player1.setText(name)
    #         self.namebox.clear()
    #     if self.h==2:
    #         name=self.namebox.toPlainText()
    #         self.player2.setText(name)
    #         self.namebox.clear()
    #     print("clicked")

    def getTime(self):
        print(self.timebox.currentText())






##############################################################################
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
