import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt07.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.le_mine.returnPressed.connect(self.myclick) #엔터 치면 버튼 클릭 기능
        
    def myclick(self):
        mine = self.le_mine.text()
        com = ""
        result = ""

        rnd = random()
        
        if rnd > 0.66 :
            com = "가위"
        elif rnd > 0.33 :
            com = "바위"
        else :
            com = "보"
            
        if com == "가위" and mine == "가위" : result = "무승부"
        if com == "가위" and mine == "바위" : result = "승리"
        if com == "가위" and mine == "보" : result = "패배"

        if com == "바위" and mine == "가위" : result = "패배"
        if com == "바위" and mine == "바위" : result = "무승부"
        if com == "바위" and mine == "보" : result = "승리"

        if com == "보" and mine == "가위" : result = "승리"
        if com == "보" and mine == "바위" : result = "패배"
        if com == "보" and mine == "보" : result = "무승부"
                   
        self.le_com.setText(com)
        self.le_result.setText(result)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
