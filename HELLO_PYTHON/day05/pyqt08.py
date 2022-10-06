import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt08.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)

    def drawStar(self,cnt):
        ret = "";
        for i in range(cnt) :
            ret += "*"  #별 누적   
        ret += "\n"
        return ret

    def myclick(self):
        first = int(self.le_first.text())
        second = int(self.le_last.text())
        
        txt = ""
        
        for i in range(first,second+1) :
            txt += self.drawStar(i)
        
        self.te.setText(txt)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
