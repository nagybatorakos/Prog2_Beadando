import sys
from PyQt5 import QtWidgets
from settingwindow import Ui_MainWindow
from ChessWindow import Ui_Gameview
import time
import Base





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
        self.newWindow=QtWidgets.QMainWindow()
        self.ui2=Ui_Gameview()
        self.ui2.setupUi(self.newWindow)
        self.ui2.whiteTimer.setText(self.time+':00')
        self.ui2.blackTimer.setText(self.time+':00')
        #self.ui2.gameoverbutton.clicked.connect(self.openWinnerWindow)
###############################################################
        self.ui2.label00.clicked.connect(self.showMoves)
        self.ui2.label01.clicked.connect(self.showMoves)
        self.ui2.label02.clicked.connect(self.showMoves)
        self.ui2.label03.clicked.connect(self.showMoves)
        self.ui2.label04.clicked.connect(self.showMoves)
        self.ui2.label05.clicked.connect(self.showMoves)
        self.ui2.label06.clicked.connect(self.showMoves)
        self.ui2.label07.clicked.connect(self.showMoves)
        self.ui2.label10.clicked.connect(self.showMoves)
        self.ui2.label11.clicked.connect(self.showMoves)
        self.ui2.label12.clicked.connect(self.showMoves)
        self.ui2.label13.clicked.connect(self.showMoves)
        self.ui2.label14.clicked.connect(self.showMoves)
        self.ui2.label15.clicked.connect(self.showMoves)
        self.ui2.label16.clicked.connect(self.showMoves)
        self.ui2.label17.clicked.connect(self.showMoves)
        self.ui2.label20.clicked.connect(self.showMoves)
        self.ui2.label21.clicked.connect(self.showMoves)
        self.ui2.label22.clicked.connect(self.showMoves)
        self.ui2.label23.clicked.connect(self.showMoves)
        self.ui2.label24.clicked.connect(self.showMoves)
        self.ui2.label25.clicked.connect(self.showMoves)
        self.ui2.label26.clicked.connect(self.showMoves)
        self.ui2.label27.clicked.connect(self.showMoves)
        self.ui2.label30.clicked.connect(self.showMoves)
        self.ui2.label31.clicked.connect(self.showMoves)
        self.ui2.label32.clicked.connect(self.showMoves)
        self.ui2.label33.clicked.connect(self.showMoves)
        self.ui2.label34.clicked.connect(self.showMoves)
        self.ui2.label35.clicked.connect(self.showMoves)
        self.ui2.label36.clicked.connect(self.showMoves)
        self.ui2.label37.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label.clicked.connect(self.showMoves)
        self.ui2.label71.clicked.connect(self.showMoves)


###############################################################
        self.newWindow.show()


    def timer(self):
        stop=int(self.time)*60
        while stop>0:
            min,sec=divmod(stop, 60)
            time_left=str(min).zfill(2)+':'+str(sec).zfill(2)
            print(time_left+'\r', end="")
            time.sleep(1)
            stop-=1
        return None


    def showMoves(self):
        print('clicked')




app = QtWidgets.QApplication(sys.argv)
cntrl = Setting()
sys.exit(app.exec_())
