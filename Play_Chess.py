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
        self.pic={'WR':'WR.png', 'WK':'WK.png' , 'WKing':'WKing.png', 'WB':'WB.png', 'WP':'WP.png' , 'WQ':'WQ.png',
                  'BR':'BR.png', 'BK':'BK.png' , 'BKing':'BKing.png', 'BB':'BB.png', 'BP':'BP.png' , 'BQ':'BQ.png'}
        self.zold=False
        self.prevLab=None
        self.prevLs=[]
        self.prevN=''

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

        self.poz={'00': self.ui2.label00,'01': self.ui2.label01, '02':self.ui2.label02, '03':self.ui2.label03, '04':self.ui2.label04, '05':self.ui2.label05, '06':self.ui2.label06, '07':self.ui2.label07,
                  '10':self.ui2.label10, '11':self.ui2.label11, '12':self.ui2.label12, '13':self.ui2.label13, '14':self.ui2.label14, '15':self.ui2.label15, '16':self.ui2.label16, '17':self.ui2.label17,
        '20':self.ui2.label20, '21':self.ui2.label21, '22':self.ui2.label22, '23':self.ui2.label23, '24':self.ui2.label24, '25':self.ui2.label25, '26':self.ui2.label26, '27':self.ui2.label27,
        '30':self.ui2.label30, '31':self.ui2.label31, '32':self.ui2.label32, '33':self.ui2.label33, '34':self.ui2.label34, '35':self.ui2.label35, '36':self.ui2.label36, '37':self.ui2.label37,
         '40':self.ui2.label40, '41':self.ui2.label41, '42':self.ui2.label42, '43':self.ui2.label43, '44':self.ui2.label44, '45':self.ui2.label45,'46':self.ui2.label46, '47':self.ui2.label47,
        '50':self.ui2.label50, '51':self.ui2.label51, '52':self.ui2.label52, '53':self.ui2.label53, '54':self.ui2.label54, '55':self.ui2.label55, '56':self.ui2.label56, '57':self.ui2.label57,
        '60':self.ui2.label60, '61':self.ui2.label61, '62':self.ui2.label62, '63':self.ui2.label63, '64':self.ui2.label64, '65':self.ui2.label65, '66':self.ui2.label66, '67':self.ui2.label67,
        '70':self.ui2.label70, '71':self.ui2.label71, '72':self.ui2.label72, '73':self.ui2.label73, '74':self.ui2.label74, '75':self.ui2.label75, '76':self.ui2.label76, '77':self.ui2.label77}


        #self.ui2.gameoverbutton.clicked.connect(self.openWinnerWindow)
###############################################################

        self.ui2.label00.clicked.connect(partial(self.showMoves,'00',self.ui2.label00))
        self.ui2.label01.clicked.connect(partial(self.showMoves,'01',self.ui2.label01))
        self.ui2.label02.clicked.connect(partial(self.showMoves,'02',self.ui2.label02))
        self.ui2.label03.clicked.connect(partial(self.showMoves,'03',self.ui2.label03))
        self.ui2.label04.clicked.connect(partial(self.showMoves,'04',self.ui2.label04))
        self.ui2.label05.clicked.connect(partial(self.showMoves,'05',self.ui2.label05))
        self.ui2.label06.clicked.connect(partial(self.showMoves,'06',self.ui2.label06))
        self.ui2.label07.clicked.connect(partial(self.showMoves,'07',self.ui2.label07))
        self.ui2.label10.clicked.connect(partial(self.showMoves,'10',self.ui2.label10))
        self.ui2.label11.clicked.connect(partial(self.showMoves,'11',self.ui2.label11))
        self.ui2.label12.clicked.connect(partial(self.showMoves,'12',self.ui2.label12))
        self.ui2.label13.clicked.connect(partial(self.showMoves,'13',self.ui2.label13))
        self.ui2.label14.clicked.connect(partial(self.showMoves,'14',self.ui2.label14))
        self.ui2.label15.clicked.connect(partial(self.showMoves,'15',self.ui2.label15))
        self.ui2.label16.clicked.connect(partial(self.showMoves,'16',self.ui2.label16))
        self.ui2.label17.clicked.connect(partial(self.showMoves,'17',self.ui2.label17))
        self.ui2.label20.clicked.connect(partial(self.showMoves,'20',self.ui2.label20))
        self.ui2.label21.clicked.connect(partial(self.showMoves,'21',self.ui2.label21))
        self.ui2.label22.clicked.connect(partial(self.showMoves,'22',self.ui2.label22))
        self.ui2.label23.clicked.connect(partial(self.showMoves,'23',self.ui2.label23))
        self.ui2.label24.clicked.connect(partial(self.showMoves,'24',self.ui2.label24))
        self.ui2.label25.clicked.connect(partial(self.showMoves,'25',self.ui2.label25))
        self.ui2.label26.clicked.connect(partial(self.showMoves,'26',self.ui2.label26))
        self.ui2.label27.clicked.connect(partial(self.showMoves,'27',self.ui2.label27))
        self.ui2.label30.clicked.connect(partial(self.showMoves,'30',self.ui2.label30))
        self.ui2.label31.clicked.connect(partial(self.showMoves,'31',self.ui2.label31))
        self.ui2.label32.clicked.connect(partial(self.showMoves,'32',self.ui2.label32))
        self.ui2.label33.clicked.connect(partial(self.showMoves,'33',self.ui2.label33))
        self.ui2.label34.clicked.connect(partial(self.showMoves,'34',self.ui2.label34))
        self.ui2.label35.clicked.connect(partial(self.showMoves,'35',self.ui2.label35))
        self.ui2.label36.clicked.connect(partial(self.showMoves,'36',self.ui2.label36))
        self.ui2.label37.clicked.connect(partial(self.showMoves,'37',self.ui2.label37))
        self.ui2.label40.clicked.connect(partial(self.showMoves,'40',self.ui2.label40))
        self.ui2.label41.clicked.connect(partial(self.showMoves,'41',self.ui2.label41))
        self.ui2.label42.clicked.connect(partial(self.showMoves,'42',self.ui2.label42))
        self.ui2.label43.clicked.connect(partial(self.showMoves,'43',self.ui2.label43))
        self.ui2.label44.clicked.connect(partial(self.showMoves,'44',self.ui2.label44))
        self.ui2.label45.clicked.connect(partial(self.showMoves,'45',self.ui2.label45))
        self.ui2.label46.clicked.connect(partial(self.showMoves,'46',self.ui2.label46))
        self.ui2.label47.clicked.connect(partial(self.showMoves,'47',self.ui2.label47))
        self.ui2.label50.clicked.connect(partial(self.showMoves,'50',self.ui2.label50))
        self.ui2.label51.clicked.connect(partial(self.showMoves,'51',self.ui2.label51))
        self.ui2.label52.clicked.connect(partial(self.showMoves,'52',self.ui2.label52))
        self.ui2.label53.clicked.connect(partial(self.showMoves,'53',self.ui2.label53))
        self.ui2.label54.clicked.connect(partial(self.showMoves,'54',self.ui2.label54))
        self.ui2.label55.clicked.connect(partial(self.showMoves,'55',self.ui2.label55))
        self.ui2.label56.clicked.connect(partial(self.showMoves,'56',self.ui2.label56))
        self.ui2.label57.clicked.connect(partial(self.showMoves,'57',self.ui2.label57))
        self.ui2.label60.clicked.connect(partial(self.showMoves,'60',self.ui2.label60))
        self.ui2.label61.clicked.connect(partial(self.showMoves,'61',self.ui2.label61))
        self.ui2.label62.clicked.connect(partial(self.showMoves,'62',self.ui2.label62))
        self.ui2.label63.clicked.connect(partial(self.showMoves,'63',self.ui2.label63))
        self.ui2.label64.clicked.connect(partial(self.showMoves,'64',self.ui2.label64))
        self.ui2.label65.clicked.connect(partial(self.showMoves,'65',self.ui2.label65))
        self.ui2.label66.clicked.connect(partial(self.showMoves,'66',self.ui2.label66))
        self.ui2.label67.clicked.connect(partial(self.showMoves,'67',self.ui2.label67))
        self.ui2.label70.clicked.connect(partial(self.showMoves,'70',self.ui2.label70))
        self.ui2.label71.clicked.connect(partial(self.showMoves,'71',self.ui2.label71))
        self.ui2.label72.clicked.connect(partial(self.showMoves,'72',self.ui2.label72))
        self.ui2.label73.clicked.connect(partial(self.showMoves,'73',self.ui2.label73))
        self.ui2.label74.clicked.connect(partial(self.showMoves,'74',self.ui2.label74))
        self.ui2.label75.clicked.connect(partial(self.showMoves,'75',self.ui2.label75))
        self.ui2.label76.clicked.connect(partial(self.showMoves,'76',self.ui2.label76))
        self.ui2.label77.clicked.connect(partial(self.showMoves,'77',self.ui2.label77))




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


    def showMoves(self, n, label):
        x=int(n[0])
        y=int(n[1])
        ls= canMove(x,y)
        if self.zold==False:
            if getname(x, y)!='':
                if ls != []:
                    self.zold=True
                    for i in ls:
                        which=self.poz[i]
                        which.setStyleSheet('border: 7px inset green;')
                    self.prevLab=label
                    self.prevLs=ls
                    self.prevName=getname(x,y)
                    self.prevN=n
        elif self.zold and n in self.prevLs:
            if self.prevN!='':
                i=int(self.prevN[0])
                j=int(self.prevN[1])
                label.setPixmap(QtGui.QPixmap(self.pic[self.prevName]))
                self.prevLab.clear()
                board[i][j]=''
                board[x][y]=self.prevName
                for i in self.prevLs:
                    which=self.poz[i]
                    #which.setStyleSheet('')

                self.zold=False




def canMove(x, y):
    name=getname(x,y)
    if name!='':
        if name[1]=='R':
            name=Rook(name)
            return name.canMove(x, y)
        elif name[1:]=='King':
            name=King(name)
            return name.canMove(x, y)
        elif name[1]=='B':
            name=Bishop(name)
            return name.canMove(x,y)
        elif name[1]=='Q':
            name=Queen(name)
            return name.canMove(x, y)
        elif name[1:]=='K':
            name=Knight(name)
            return name.canMove(x, y)


app = QtWidgets.QApplication(sys.argv)
cntrl = Setting()
sys.exit(app.exec_())
