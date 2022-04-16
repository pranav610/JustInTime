# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'SplashScreen.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        palette = QPalette()
        brush = QBrush(QColor(236, 236, 236, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(236, 236, 236, 128))
        brush1.setStyle(Qt.SolidPattern)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
# endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
# endif
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        brush3 = QBrush(QColor(0, 0, 0, 128))
        brush3.setStyle(Qt.SolidPattern)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
# endif
        SplashScreen.setPalette(palette)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
                                           "	background-color: rgb(216,102,102);\n"
                                           "	color: rgb(0, 0, 0);\n"
                                           "	border-radius: 20px;\n"
                                           "}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 90, 661, 61))
        font = QFont()
        font.setFamily(u"Bahnschrift SemiBold SemiConden")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(243,239 , 108)")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 150, 661, 31))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift Light Condensed")
        font1.setPointSize(14)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(243,239 , 108)")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 270, 561, 23))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush4 = QBrush(QColor(255, 255, 255, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush4)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
# endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush4)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
# endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        brush5 = QBrush(QColor(44, 49, 60, 128))
        brush5.setStyle(Qt.SolidPattern)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
# endif
        self.progressBar.setPalette(palette1)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.progressBar.setFont(font2)
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
                                       "	background-color: rgb(255, 255, 255);\n"
                                       "	border-style: none;\n"
                                       "	border-radius: 10px;\n"
                                       "	text-align: center;\n"
                                       "}\n"
                                       "QProgressBar::chunk{\n"
                                       "	border-radius: 10px;\n"
                                       "	background-color: qlineargradient(spread:pad, x1:0, y1:0.563, x2:0.995025, y2:0.585, stop:0 rgba(154, 134, 101, 255), stop:1 rgba(250, 213, 113, 255))\n"
                                       "}")
        self.progressBar.setValue(50)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 310, 661, 31))
        font3 = QFont()
        font3.setFamily(u"MingLiU-ExtB")
        font3.setPointSize(12)
        self.label_loading.setFont(font3)
        self.label_loading.setStyleSheet(u"color: rgb(230, 230, 81)")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(-10, 350, 621, 21))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        self.label_credits.setFont(font4)
        self.label_credits.setStyleSheet(u"color: rgb(230, 230, 81);")
        self.label_credits.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate(
            "SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate(
            "SplashScreen", u"<html><head/><body><p align=\"center\">JustInTime</p></body></html>", None))
        self.label_description.setText(QCoreApplication.translate(
            "SplashScreen", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-style:italic;\">Motor Part Shop System</span></p></body></html>", None))
        self.label_loading.setText(QCoreApplication.translate(
            "SplashScreen", u"Loading Motor Part Shop System...", None))
        self.label_credits.setText(QCoreApplication.translate(
            "SplashScreen", u"<html><head/><body><p><span style=\" font-weight:600;\">Group 5: Complex Processors</span></p></body></html>", None))
    # retranslateUi
