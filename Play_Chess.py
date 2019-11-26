import sys
from PyQt5 import QtWidgets
from settingwindow import Ui_MainWindow


class Setting:

    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.ui.player_add_button.clicked.connect(self.addPlayer)
        self.MainWindow.show()
        self.h=0


    def addPlayer(self):
        self.h+=1
        if self.h==2:
            k=1
        if self.h==1:
            name=self.ui.namebox.toPlainText()
            self.ui.player1.setText(name)
        if self.h==2:
            name=self.ui.namebox.toPlainText()
            self.ui.player2.setText(name)
        print("clicked")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# app = QtWidgets.QApplication(sys.argv)
# cntrl = Setting()
# sys.exit(app.exec_())
