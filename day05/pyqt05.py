import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt05.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        mine = self.leMine.text()
        com = self.leComRand()
        
    def leComRand(self):
    
        com = ""
        rnd = randint(0,2)
        if(rnd == 0):
            com = "짝"
        else:
            com = "홀"
        return com 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
