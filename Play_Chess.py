import sys
from PyQt5 import QtWidgets, QtGui
from settingwindow import Ui_MainWindow
from ChessWindow import Ui_Gameview
import time
from Base import *
from functools import partial
from PyQt5.QtWidgets import QWidget
#from ff import Widget
from PyQt5.QtGui import QColor
from selectwindow import Ui_Selection
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QMessageBox

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
                  'BR':'BR.png', 'BK':'BK.png' , 'BKing':'BKing.png', 'BB':'BB.png', 'BP':'BP1.png' , 'BQ':'BQ.png'}

        self.zold=False
        self.prevLab=None
        self.prevLs=[]
        self.prevN=''
        self.colors={}
        self.turn='W'
        self.outofPlay=[]
        self.selected='P'
        self.matt=''
        self.sakkmatt=''
        self.mattLs=[]
        self.inverse={'W':'B','B':'W'}

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
        ls= []
        ls0=canMove(x,y)
        k=King(self.inverse[self.turn]+'King')


        if getname(x,y)!='' and len(ls0)>0 and k.getPosition() in ls0:
            ls0.remove(k.getPosition())


        if self.matt!=self.turn:
            ls=ls0


        if self.matt==self.turn and ls0!=[] and getname(x,y)!='':
            if getname(x,y)[1:]=='King':
                ls=ls0
            else:
                for i in ls0:
                    if i in self.mattLs:
                        ls.append(i)




        if self.zold==False:
            if getname(x, y)!='' and getname(x,y)[0]==self.turn:
                if ls0 != []:
                    self.zold=True
                    for i in range(len(ls)):
                        which=self.poz[ls[i]]
                        self.colors[ls[i]]=which.palette().button().color()
                        #self.colors.append(which.palette().button().color())
                        which.setStyleSheet('background-color:'+which.palette().button().color().name()+';'+'border: 7px inset green;')

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

                if getname(x,y)!='' and getname(x, y)[1]!='P':
                    self.outofPlay.append(getname(x,y))

                board[i][j]=''
                board[x][y]=self.prevName
                print(searchall())
                print(self.searchChain(x,y))

                for i in range(len(self.prevLs)):
                    which=self.poz[self.prevLs[i]]
                    which.setStyleSheet('background-color:'+self.colors[self.prevLs[i]].name()+';')
                    #which.setStyleSheet('background-color:'+self.colors[i].name()+';')
                    #which.setStyleSheet('')

                if (x==0 or x==7) and self.prevName[1]=='P':
                    print(self.openSelection( x, y, label))

                self.zold=False
                self.turn=self.inverse[self.turn]
                # if self.turn=='W':
                #     self.turn='B'
                # elif self.turn=='B':
                #     self.turn='W'

        elif self.zold and n not in self.prevLs:
            self.zold=False
            for i in range(len(self.prevLs)):
                which=self.poz[self.prevLs[i]]
                which.setStyleSheet('background-color:'+self.colors[self.prevLs[i]].name()+';')

        # if self.matt==True:



    def openSelection(self, x, y, label):
        self.anotherWindow=QtWidgets.QMainWindow()
        self.ui3=Ui_Selection()
        self.ui3.setupUi(self.anotherWindow)
        # msg = QMessageBox()
        # msg.setWindowTitle("")
        # msg.setText("You can replace yor pawn with one of these pieces.")
        # msg.setIcon(QMessageBox.Information)
        # msg.setStandardButtons(QMessageBox.Ok)
        self.ui3.listWidget.currentItemChanged.connect(partial(self.replace,x,y,label))
        self.ui3.selectbutton.clicked.connect(self.anotherWindow.close)

        for i in self.outofPlay:
            item=QListWidgetItem()

            if i[0]!=self.turn:
                continue
            if i[1]=='Q':
                item.setText('Queen ♛')
            if i[1]=='R':
                item.setText('Rook ♜')
            if i[1]=='K':
                item.setText('Knight ♞')
            if i[1]=='B':
                item.setText('Bishop ♝')
            self.ui3.listWidget.addItem(item)
            self.ui3.listWidget.setCurrentItem(item)


        self.anotherWindow.show()


    def replace(self,x,y,label):
        curr= self.ui3.listWidget.currentItem()
        self.selected=self.inverse[self.turn]+curr.text()[0]
        label.setPixmap(QtGui.QPixmap(self.pic[self.selected]))
        board[x][y]=self.selected


    def searchChain(self, x,y):
        k=King(self.inverse[self.turn]+'King')
        n=k.getPosition()
        i=int(n[0])
        j=int(n[1])
        ls=canMove(x,y)
        self.mattLs=[]
        if n not in ls:
            self.matt=''
        elif n in ls:
            msg = QMessageBox()
            msg.setWindowTitle("")

            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)

            self.matt=self.inverse[self.turn]
            ls.remove(k.getPosition())
            if x == i:
                if y>j:
                    for i in range(j,y):
                        if str(x)+str(i) in ls:
                            self.mattLs.append(str(x)+str(i))
                elif j>y:
                    for i in range(y,j,-1):
                        if str(x)+str(i) in ls:
                            self.mattLs.append(str(x)+str(i))
            elif y==j:
                if x>i:
                    for i in range(x,i,-1):
                        if str(x)+str(i) in ls:
                            self.mattLs.append(str(x)+str(i))
                if i>x:
                    for i in range(x,i):
                        if str(x)+str(i) in ls:
                            self.mattLs.append(str(x)+str(i))
            elif x>i:
                if y>j:
                    h=x-1
                    for i in range(y-1,j,-1):
                        if str(h)+str(i) in ls:
                            self.mattLs.append(str(h)+str(i))
                        h-=1
                if j>y:
                    h=x-1
                    for i in range(y+1,j):
                        if str(h)+str(i) in ls:
                            self.mattLs.append(str(h)+str(i))
                        h-=1
            elif i>x:
                if y>j:
                    h=x+1
                    for i in range(y-1,j,-1):
                        if str(h)+str(i) in ls:
                            self.mattLs.append(str(h)+str(i))
                        h+=1
                if j>y:
                    h=x+1
                    for i in range(y+1,j):
                        if str(h)+str(i) in ls:
                            self.mattLs.append(str(h)+str(i))
                        h+=1

            if k.getPosition() in self.mattLs:
                self.mattLs.remove(k.getPosition())
            if str(x)+str(y) not in self.mattLs:
                self.mattLs.append(str(x)+str(y))

            print(searchall(), self.checkmate())
            print(self.mattLs)

            if self.sakkmatt!=True:
                msg.setText("Check!")

            else:
                if self.turn=='W':
                    msg.setText('Checkmate! '+self.ui.player1.text()+' wins!')
                else:
                    msg.setText('Checkmate! '+self.ui.player2.text()+' wins!')

            msg.exec()
            self.newWindow.close()
    def checkmate(self):
        k=0
        if self.matt=='B':
            for i in self.mattLs:
                for j in allB:
                    if i==j:
                        k+=1

        elif self.matt=='W':
            for i in self.mattLs:
                for j in allW:
                    if i==j:
                        k+=1
        if k==0:
            self.sakkmatt=True

        print(self.sakkmatt)

def canMove(x, y):
    name=getname(x,y)
    if name!='':
        if name[1]=='R':
            name=Rook(name)
            return name.canMove(x, y)
        elif name[1:]=='King':
            name=King(name)
            ls=[]

            if getname(x,y)[0]=='W':
                for i in name.canMove(x, y):
                    if i not in allB:
                        ls.append(i)

            elif getname(x,y)[0]=='B':
                for i in name.canMove(x, y):
                    if i not in allW:
                        ls.append(i)
            return ls
        elif name[1]=='B':
            name=Bishop(name)
            return name.canMove(x,y)
        elif name[1]=='Q':
            name=Queen(name)
            return name.canMove(x, y)
        elif name[1:]=='K':
            name=Knight(name)
            return name.canMove(x, y)
        elif name[1]=='P':
            name=Pawn(name)
            return name.canMove(x, y)


    # def mattAppend()



def searchall():
    allB=[]
    allW=[]
    for i in range(board_shape[0]):
        for j in range(board_shape[1]):
            if getname(i,j)!='' and getname(i, j)[0]=='W':
                for k in canMove(i, j):
                    if k not in allW:
                        allW.append(k)
            if getname(i,j)!='' and getname(i, j)[0]=='B':
                for k in canMove(i, j):
                    if k not in allB:
                        allB.append(k)





app = QtWidgets.QApplication(sys.argv)
cntrl = Setting()
sys.exit(app.exec_())
