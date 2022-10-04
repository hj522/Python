import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt10.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.setCom()
    
    def setCom(self):
        ran = [1,2,3,4,5,6,7,8,9]
        for i in range(100) :
            rnd = int(random()*9)
            a = ran[0]
            b = ran[rnd]
            ran[0] = b
            ran[rnd] = a
        
        self.com = str(ran[0])+str(ran[1])+str(ran[2])
        print("self.com",self.com)
    
    def getStrike(self,com,mine):
        cnt = 0
        c1 = com[0:1]
        c2 = com[1:2]
        c3 = com[2:3]
        m1 = mine[0:1]
        m2 = mine[1:2]
        m3 = mine[2:3]
        
        if c1 == m1 : cnt+=1
        if c2 == m2 : cnt+=1
        if c3 == m3 : cnt+=1
        
        return cnt

    def getBall(self,com,mine):
        cnt = 0
        c1 = com[0:1]
        c2 = com[1:2]
        c3 = com[2:3]
        m1 = mine[0:1]
        m2 = mine[1:2]
        m3 = mine[2:3]
        
        if c1 == m2 or c1 == m3 : cnt+=1
        if c2 == m1 or c2 == m3 : cnt+=1
        if c3 == m1 or c3 == m2 : cnt+=1
        
        return cnt

    def myclick(self):
        str_old = self.te.toPlainText()
        mine = self.le.text()
        s = self.getStrike(self.com, mine)
        b = self.getBall(self.com, mine)
        
        str_new = mine+" "+str(s)+"S"+str(b)+"B"+"\n"
        
        self.te.setText(str_old+str_new)
        self.le.setText("")
        
        if s == 3:
            QMessageBox.information(self, "야구게임", mine+"를 맞혔습니다!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
