import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt03.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
    
    def myclick(self):
        a = self.le1.text()
        aa = int(a)
        b = self.le2.text()
        bb = int(b)
        self.le3.setText(str(aa+bb)); #숫자를 다시 문자열로

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
