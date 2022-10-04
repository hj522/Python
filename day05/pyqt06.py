import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt06.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        dan = int(self.le.text())
        self.te.setText("{}*{}={}".format(dan,1,dan*1)
                        +"\n"+"{}*{}={}".format(dan,2,str(dan*2))
                        +"\n"+"{}*{}={}".format(dan,3,str(dan*3))
                        +"\n"+"{}*{}={}".format(dan,4,str(dan*4))
                        +"\n"+"{}*{}={}".format(dan,5,str(dan*5))
                        +"\n"+"{}*{}={}".format(dan,6,str(dan*6))
                        +"\n"+"{}*{}={}".format(dan,7,str(dan*7))
                        +"\n"+"{}*{}={}".format(dan,8,str(dan*8))
                        +"\n"+"{}*{}={}".format(dan,9,str(dan*9))
                        )
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
