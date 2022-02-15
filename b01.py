from configparser import ConfigParser
import sys
from tkinter import S, Widget
from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6.QtCore import QTimer
from b01_mainui import Ui_MainWindow
from b01_setui import Ui_setWindow
from setini import ini
from b import coin_price,coin_main
#pyside6-uic x.ui > x.py 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.i=ini()
        self.i.ini_set()
        self.ini_read()

        self.ui.Refresh.released.connect(self.refresh)
        self.ui.Set.released.connect(self.set)

        self.ui.checkBox.stateChanged.connect(self.auto) 

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh)

    def ini_read(self):
        i_data=self.i.ini_read()
        self.coin1=i_data['coin1']
        self.coin2=i_data['coin2']
        self.coin3=i_data['coin3']
        self.coin4=i_data['coin4']
        self.coin5=i_data['coin5']


    def refresh(self):
        self.ui.labelA1.setText(self.coin1)
        self.ui.labelB1.setText(self.coin2)
        self.ui.labelC1.setText(self.coin3)
        self.ui.labelD1.setText(self.coin4)
        self.ui.labelE1.setText(self.coin5)
        A,B,C,D,E=coin_price(self.coin1+'USDT',self.coin2+'USDT',self.coin3+'USDT',self.coin4+'USDT',self.coin5+'USDT')
        self.ui.labelA2.setText('%.2f'%float(A['c']))
        self.ui.labelB2.setText('%.2f'%float(B['c']))
        self.ui.labelC2.setText('%.2f'%float(C['c']))
        self.ui.labelD2.setText('%.2f'%float(D['c']))
        self.ui.labelE2.setText('%.2f'%float(E['c']))
        self.ui.labelA3.setText('%.2f'%float(A['h']))
        self.ui.labelB3.setText('%.2f'%float(B['h']))
        self.ui.labelC3.setText('%.2f'%float(C['h']))
        self.ui.labelD3.setText('%.2f'%float(D['h']))
        self.ui.labelE3.setText('%.2f'%float(E['h']))
        self.ui.labelA4.setText('%.2f'%float(A['l']))
        self.ui.labelB4.setText('%.2f'%float(B['l']))
        self.ui.labelC4.setText('%.2f'%float(C['l']))
        self.ui.labelD4.setText('%.2f'%float(D['l']))
        self.ui.labelE4.setText('%.2f'%float(E['l']))

    def set(self):
        self.setwindow=setWindow()
        self.setwindow.ui.lineEdit_1.setText(self.coin1)
        self.setwindow.ui.lineEdit_2.setText(self.coin2)
        self.setwindow.ui.lineEdit_3.setText(self.coin3)
        self.setwindow.ui.lineEdit_4.setText(self.coin4)
        self.setwindow.ui.lineEdit_5.setText(self.coin5)
        self.setwindow.ui.saveButton.clicked.connect(self.set_save) 
        self.setwindow.show() 

    def set_save(self):
        print('set_save')
        self.i.ini_change(self.setwindow.ui.lineEdit_1.text(),self.setwindow.ui.lineEdit_2.text(),self.setwindow.ui.lineEdit_3.text(),
                      self.setwindow.ui.lineEdit_4.text(),self.setwindow.ui.lineEdit_5.text())
        self.ini_read()
        self.refresh()
        self.setwindow.close() 
        

    def auto(self):
        checkbox = self.sender() #sender當某一個Object emit一個signal的時候，它就是一個sender,系統會記錄下當前是誰emit出這個signal的
        if checkbox.isChecked():
            print('auto on')
            return self.timer.start(5000)
        else:
            print('auto off')
            return self.timer.stop()





class setWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.ui = Ui_setWindow()
            self.ui.setupUi(self)


if __name__=='__main__':
    app=QApplication([])
    window=MainWindow()
    window.refresh()
    window.show()  
    sys.exit(app.exec_())