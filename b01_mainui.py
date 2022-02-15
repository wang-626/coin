# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'b01.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(870, 442)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"background-color:\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 0))
        self.frame.setStyleSheet(u"#frame{\n"
"background-color: rgb(148, 136, 141);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameT1 = QFrame(self.frame)
        self.frameT1.setObjectName(u"frameT1")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameT1.sizePolicy().hasHeightForWidth())
        self.frameT1.setSizePolicy(sizePolicy)
        self.frameT1.setMinimumSize(QSize(0, 37))
        self.frameT1.setMaximumSize(QSize(16777215, 60))
        self.frameT1.setFrameShape(QFrame.StyledPanel)
        self.frameT1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frameT1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frameT1_1 = QFrame(self.frameT1)
        self.frameT1_1.setObjectName(u"frameT1_1")
        self.frameT1_1.setMinimumSize(QSize(0, 22))
        self.frameT1_1.setMaximumSize(QSize(16777215, 30))
        self.frameT1_1.setFrameShape(QFrame.StyledPanel)
        self.frameT1_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frameT1_1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.Refresh = QPushButton(self.frameT1_1)
        self.Refresh.setObjectName(u"Refresh")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Refresh.sizePolicy().hasHeightForWidth())
        self.Refresh.setSizePolicy(sizePolicy1)
        self.Refresh.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(10)
        self.Refresh.setFont(font)

        self.horizontalLayout_3.addWidget(self.Refresh)

        self.Set = QPushButton(self.frameT1_1)
        self.Set.setObjectName(u"Set")
        sizePolicy1.setHeightForWidth(self.Set.sizePolicy().hasHeightForWidth())
        self.Set.setSizePolicy(sizePolicy1)
        self.Set.setMaximumSize(QSize(16777215, 20))
        self.Set.setFont(font)

        self.horizontalLayout_3.addWidget(self.Set)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frameT1_1)

        self.frameT1_2 = QFrame(self.frameT1)
        self.frameT1_2.setObjectName(u"frameT1_2")
        sizePolicy.setHeightForWidth(self.frameT1_2.sizePolicy().hasHeightForWidth())
        self.frameT1_2.setSizePolicy(sizePolicy)
        self.frameT1_2.setMinimumSize(QSize(0, 15))
        self.frameT1_2.setMaximumSize(QSize(16000000, 30))
        self.frameT1_2.setStyleSheet(u"#frame_2{\n"
"background-color: rgb(98, 255, 148);\n"
"}")
        self.frameT1_2.setFrameShape(QFrame.StyledPanel)
        self.frameT1_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frameT1_2)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.frameT1_2)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy1.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy1)
        self.checkBox.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_11.addWidget(self.checkBox)


        self.verticalLayout_3.addWidget(self.frameT1_2)


        self.verticalLayout.addWidget(self.frameT1)

        self.frameT2 = QFrame(self.frame)
        self.frameT2.setObjectName(u"frameT2")
        self.frameT2.setMaximumSize(QSize(16777215, 30))
        self.frameT2.setFrameShape(QFrame.StyledPanel)
        self.frameT2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frameT2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.labelT1 = QLabel(self.frameT2)
        self.labelT1.setObjectName(u"labelT1")
        self.labelT1.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.labelT1.setMargin(0)

        self.horizontalLayout_7.addWidget(self.labelT1)

        self.labelT2 = QLabel(self.frameT2)
        self.labelT2.setObjectName(u"labelT2")
        self.labelT2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout_7.addWidget(self.labelT2)

        self.labelT3 = QLabel(self.frameT2)
        self.labelT3.setObjectName(u"labelT3")
        self.labelT3.setFrameShape(QFrame.NoFrame)
        self.labelT3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout_7.addWidget(self.labelT3)

        self.labelT4 = QLabel(self.frameT2)
        self.labelT4.setObjectName(u"labelT4")
        self.labelT4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout_7.addWidget(self.labelT4)


        self.verticalLayout.addWidget(self.frameT2)

        self.frameA = QFrame(self.frame)
        self.frameA.setObjectName(u"frameA")
        self.frameA.setMinimumSize(QSize(0, 15))
        self.frameA.setStyleSheet(u"#frameA:hover{\n"
"background-color: rgb(243, 235, 235);\n"
"}")
        self.frameA.setFrameShape(QFrame.StyledPanel)
        self.frameA.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frameA)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.labelA1 = QLabel(self.frameA)
        self.labelA1.setObjectName(u"labelA1")
        self.labelA1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelA1)

        self.labelA2 = QLabel(self.frameA)
        self.labelA2.setObjectName(u"labelA2")
        self.labelA2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelA2)

        self.labelA3 = QLabel(self.frameA)
        self.labelA3.setObjectName(u"labelA3")
        self.labelA3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelA3)

        self.labelA4 = QLabel(self.frameA)
        self.labelA4.setObjectName(u"labelA4")
        self.labelA4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelA4)


        self.verticalLayout.addWidget(self.frameA)

        self.frameB = QFrame(self.frame)
        self.frameB.setObjectName(u"frameB")
        self.frameB.setMinimumSize(QSize(0, 15))
        self.frameB.setStyleSheet(u"#frameB:hover{\n"
"background-color: rgb(243, 235, 235);\n"
"}")
        self.frameB.setFrameShape(QFrame.StyledPanel)
        self.frameB.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frameB)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.labelB1 = QLabel(self.frameB)
        self.labelB1.setObjectName(u"labelB1")
        self.labelB1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelB1)

        self.labelB2 = QLabel(self.frameB)
        self.labelB2.setObjectName(u"labelB2")
        self.labelB2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelB2)

        self.labelB3 = QLabel(self.frameB)
        self.labelB3.setObjectName(u"labelB3")
        self.labelB3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelB3)

        self.labelB4 = QLabel(self.frameB)
        self.labelB4.setObjectName(u"labelB4")
        self.labelB4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelB4)


        self.verticalLayout.addWidget(self.frameB)

        self.frameC = QFrame(self.frame)
        self.frameC.setObjectName(u"frameC")
        self.frameC.setMinimumSize(QSize(0, 15))
        self.frameC.setStyleSheet(u"#frameC:hover{\n"
"background-color: rgb(243, 235, 235);\n"
"}")
        self.frameC.setFrameShape(QFrame.StyledPanel)
        self.frameC.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frameC)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.labelC1 = QLabel(self.frameC)
        self.labelC1.setObjectName(u"labelC1")
        self.labelC1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelC1)

        self.labelC2 = QLabel(self.frameC)
        self.labelC2.setObjectName(u"labelC2")
        self.labelC2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelC2)

        self.labelC3 = QLabel(self.frameC)
        self.labelC3.setObjectName(u"labelC3")
        self.labelC3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelC3)

        self.labelC4 = QLabel(self.frameC)
        self.labelC4.setObjectName(u"labelC4")
        self.labelC4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelC4)


        self.verticalLayout.addWidget(self.frameC)

        self.frameD = QFrame(self.frame)
        self.frameD.setObjectName(u"frameD")
        self.frameD.setMinimumSize(QSize(0, 15))
        self.frameD.setStyleSheet(u"#frameD:hover{\n"
"background-color: rgb(243, 235, 235);\n"
"}")
        self.frameD.setFrameShape(QFrame.StyledPanel)
        self.frameD.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frameD)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.labelD1 = QLabel(self.frameD)
        self.labelD1.setObjectName(u"labelD1")
        self.labelD1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.labelD1)

        self.labelD2 = QLabel(self.frameD)
        self.labelD2.setObjectName(u"labelD2")
        self.labelD2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.labelD2)

        self.labelD3 = QLabel(self.frameD)
        self.labelD3.setObjectName(u"labelD3")
        self.labelD3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.labelD3)

        self.labelD4 = QLabel(self.frameD)
        self.labelD4.setObjectName(u"labelD4")
        self.labelD4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.labelD4)


        self.verticalLayout.addWidget(self.frameD)

        self.frameE = QFrame(self.frame)
        self.frameE.setObjectName(u"frameE")
        self.frameE.setMinimumSize(QSize(0, 15))
        self.frameE.setStyleSheet(u"#frameE:hover{\n"
"background-color: rgb(243, 235, 235);\n"
"}")
        self.frameE.setFrameShape(QFrame.StyledPanel)
        self.frameE.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frameE)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.labelE1 = QLabel(self.frameE)
        self.labelE1.setObjectName(u"labelE1")
        self.labelE1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.labelE1)

        self.labelE2 = QLabel(self.frameE)
        self.labelE2.setObjectName(u"labelE2")
        self.labelE2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.labelE2)

        self.labelE3 = QLabel(self.frameE)
        self.labelE3.setObjectName(u"labelE3")
        self.labelE3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.labelE3)

        self.labelE4 = QLabel(self.frameE)
        self.labelE4.setObjectName(u"labelE4")
        self.labelE4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.labelE4)


        self.verticalLayout.addWidget(self.frameE)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"yee0.1", None))
        self.Refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.Set.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"AutoRefresh", None))
        self.labelT1.setText(QCoreApplication.translate("MainWindow", u"Coin", None))
        self.labelT2.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.labelT3.setText(QCoreApplication.translate("MainWindow", u"24High", None))
        self.labelT4.setText(QCoreApplication.translate("MainWindow", u"24Low", None))
        self.labelA1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelA2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelA3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelA4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelB1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelB2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelB3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelB4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelC1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelC2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelC3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelC4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelD1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelD2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelD3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelD4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelE1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelE2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelE3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelE4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

