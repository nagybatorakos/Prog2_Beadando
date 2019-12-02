import sys
from PyQt5 import QtWidgets, QtGui
from settingwindow import Ui_MainWindow
from ChessWindow import Ui_Gameview
import time
from Base import *
from functools import partial
from PyQt5.QtWidgets import QWidget
#from ff import Widget

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

        #self.pic={'00':'WR', '01':'WK', '02':'WB', '03':'WKing', '04':'WQ', '05':'WB' , '06':'WK' , '07':'WR' , '10':'WP' , '11':'WP' , '12':'WP' , '13':'WP' , '14': 'WP', '15': 'WP', '16':'WP' , '17':'WP' , '20':'', '21': '', '22': '', '23': '', '24': '', '25': '', '26': '', '27': '',
        #'30': '', '31': '', '32': '', '33': '', '34': '', '35': '', '36': '', '37': '', '40': '', '41': '', '42': '', '43': '', '44': '', '45': '', '46': '', '47': '', '50': '', '51': '', '52': '', '53':'', '54':'' , '55': '', '56': '', '57': '', '60': '', '61': '', '62': '', '63': '', '64': '', '65': '', '66': '', '67': '', '70': '', '71': '', '72': '', '73': '', '74': '', '75':'' , '76': '', '77': ''}
        self.pic={'WR':'WR.png'}
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

        self.ui2.label00.clicked.connect(partial(self.showMoves, '00'))
        # self.ui2.label01.clicked.connect(self.showMoves('01'))
        # self.ui2.label02.clicked.connect(self.showMoves('02'))
        # self.ui2.label03.clicked.connect(self.showMoves('03'))
        # self.ui2.label04.clicked.connect(self.showMoves('04'))
        # self.ui2.label05.clicked.connect(self.showMoves('05'))
        # self.ui2.label06.clicked.connect(self.showMoves('06'))
        # self.ui2.label07.clicked.connect(self.showMoves('07'))
        # self.ui2.label10.clicked.connect(self.showMoves('10'))
        # self.ui2.label11.clicked.connect(self.showMoves('11'))
        # self.ui2.label12.clicked.connect(self.showMoves('12'))
        # self.ui2.label13.clicked.connect(self.showMoves('13'))
        # self.ui2.label14.clicked.connect(self.showMoves('14'))
        # self.ui2.label15.clicked.connect(self.showMoves('15'))
        # self.ui2.label16.clicked.connect(self.showMoves('16'))
        # self.ui2.label17.clicked.connect(self.showMoves('17'))
        # self.ui2.label20.clicked.connect(self.showMoves('20'))
        # self.ui2.label21.clicked.connect(self.showMoves('21'))
        # self.ui2.label22.clicked.connect(self.showMoves('22'))
        # self.ui2.label23.clicked.connect(self.showMoves('23'))
        # self.ui2.label24.clicked.connect(self.showMoves('24'))
        # self.ui2.label25.clicked.connect(self.showMoves('25'))
        # self.ui2.label26.clicked.connect(self.showMoves('25'))
        # self.ui2.label27.clicked.connect(self.showMoves())
        # self.ui2.label30.clicked.connect(self.showMoves())
        # self.ui2.label31.clicked.connect(self.showMoves())
        # self.ui2.label32.clicked.connect(self.showMoves())
        # self.ui2.label33.clicked.connect(self.showMoves())
        # self.ui2.label34.clicked.connect(self.showMoves())
        # self.ui2.label35.clicked.connect(self.showMoves())
        # self.ui2.label36.clicked.connect(self.showMoves(self.ui2.label36))
        # self.ui2.label37.clicked.connect(self.showMoves(self.ui2.label37))
        # self.ui2.label40.clicked.connect(self.showMoves(self.ui2.label40))
        # self.ui2.label41.clicked.connect(self.showMoves(self.ui2.label41))
        # self.ui2.label42.clicked.connect(self.showMoves(self.ui2.label42))
        # self.ui2.label43.clicked.connect(self.showMoves(self.ui2.label43))
        # self.ui2.label44.clicked.connect(self.showMoves(self.ui2.label44))
        # self.ui2.label45.clicked.connect(self.showMoves(self.ui2.label45))
        # self.ui2.label46.clicked.connect(self.showMoves(self.ui2.label46))
        # self.ui2.label47.clicked.connect(self.showMoves(self.ui2.label47))
        # self.ui2.label50.clicked.connect(self.showMoves(self.ui2.label50))
        # self.ui2.label51.clicked.connect(self.showMoves(self.ui2.label51))
        # self.ui2.label52.clicked.connect(self.showMoves(self.ui2.label52))
        # self.ui2.label53.clicked.connect(self.showMoves(self.ui2.label53))
        # self.ui2.label54.clicked.connect(self.showMoves(self.ui2.label54))
        # self.ui2.label55.clicked.connect(self.showMoves(self.ui2.label55))
        # self.ui2.label56.clicked.connect(self.showMoves(self.ui2.label56))
        # self.ui2.label57.clicked.connect(self.showMoves(self.ui2.label57))
        # self.ui2.label60.clicked.connect(self.showMoves(self.ui2.label60))
        # self.ui2.label61.clicked.connect(self.showMoves(self.ui2.label61))
        # self.ui2.label62.clicked.connect(self.showMoves(self.ui2.label62))
        # self.ui2.label63.clicked.connect(self.showMoves(self.ui2.label63))
        # self.ui2.label64.clicked.connect(self.showMoves(self.ui2.label64))
        # self.ui2.label65.clicked.connect(self.showMoves(self.ui2.label65))
        # self.ui2.label66.clicked.connect(self.showMoves(self.ui2.label66))
        # self.ui2.label67.clicked.connect(self.showMoves(self.ui2.label67))
        # self.ui2.label70.clicked.connect(self.showMoves(self.ui2.label70))
        # self.ui2.label71.clicked.connect(self.showMoves(self.ui2.label71))
        # self.ui2.label72.clicked.connect(self.showMoves(self.ui2.label72))
        # self.ui2.label73.clicked.connect(self.showMoves(self.ui2.label73))
        # self.ui2.label74.clicked.connect(self.showMoves(self.ui2.label74))
        # self.ui2.label75.clicked.connect(self.showMoves(self.ui2.label75))
        # self.ui2.label76.clicked.connect(self.showMoves(self.ui2.label76))
        # self.ui2.label77.clicked.connect(self.showMoves(self.ui2.label77))



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


    def showMoves(self, n):
        x=int(n[0])
        y=int(n[1])
        if board[x][y]!='':
            ls=Piece(getname(x,y)).canMove(x,y)
            print(ls)




app = QtWidgets.QApplication(sys.argv)
cntrl = Setting()
sys.exit(app.exec_())
