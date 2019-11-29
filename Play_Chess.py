import sys
from PyQt5 import QtWidgets
from settingwindow import Ui_MainWindow
from asd import Ui_Gameview
import time


class Setting:
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.ui.player_add_button.clicked.connect(self.addPlayer)
        self.h=0
        self.time="10"
        self.ui.timebox.currentTextChanged.connect(self.getTime)
        self.ui.playbutton.clicked.connect(self.openChessWindow)

        self.MainWindow.show()

    def addPlayer(self):
        self.h+=1
        if self.h>2:
            self.h=1
        if self.h==1:
            name=self.ui.namebox.toPlainText()
            self.ui.player1.setText(name)
            self.ui.namebox.clear()
        if self.h==2:
            name=self.ui.namebox.toPlainText()
            self.ui.player2.setText(name)
            self.ui.namebox.clear()
        print("clicked")


    def getTime(self):
        self.time=self.ui.timebox.currentText()


    def openChessWindow(self):
        self.newWindow=QtWidgets.QMainWindow
        self.ui2=Ui_Gameview()
        self.ui2.setupUi(self.newWindow)
        self.ui2.whiteTimer.setText(self.timer)
        #self.ui2.gameoverbutton.clicked.connect(self.openWinnerWindow)




        self.newWindow.show()


    def timer(self):
        stop=int(self.time)*60
        while stop>0:
            min,sec=divmod(stop, 60)
            time_left=str(min).zfill(2)+':'+str(sec).zfill(2)
            print(time_left+'\r', end="")
            time.sleep(1)
            stop-=1

app = QtWidgets.QApplication(sys.argv)
cntrl = Setting()
sys.exit(app.exec_())
