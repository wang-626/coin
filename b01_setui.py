# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)

from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)

from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_setWindow(object):
    def setupUi(self, setWindow):
        if not setWindow.objectName():
            setWindow.setObjectName(u"setWindow")
        setWindow.resize(234, 190)
        setWindow.setMinimumSize(QSize(234, 190))
        setWindow.setMaximumSize(QSize(234, 190))
        self.centralwidget = QWidget(setWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit_1 = QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName(u"lineEdit")
        self.lineEdit_1.setGeometry(QRect(10, 20, 111, 21))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 50, 113, 20))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 80, 113, 20))
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(10, 110, 113, 20))
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(10, 140, 113, 20))
        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(150, 160, 75, 23))
        setWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(setWindow)

        QMetaObject.connectSlotsByName(setWindow)
    # setupUi

    def retranslateUi(self, setWindow):
        setWindow.setWindowTitle(QCoreApplication.translate("setWindow", u"set", None))
        self.saveButton.setText(QCoreApplication.translate("setWindow", u"SAVE", None))
    # retranslateUi

