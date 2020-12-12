'THE LIBRERIES THAT WERE USED TO CREATE THE UI FILES'
from PySide2.QtGui import *

'THE LIBRERY THAT WAS USED TO CONVERT THE LINKS'
import youtube_dl

'THE LIBRERIES THAT WERE USED TO CHANGE THE LOCATION OF THE FILES'
import os
import shutil
import os.path

'THE LIBRERIES THAT WERE USED TO CREATE THE UI FILES'
from PySide2.QtCore import (QCoreApplication, QMetaObject,QRect, QSize,Qt)
from PySide2.QtGui import (QFont, QIcon,QPixmap)
from PySide2.QtWidgets import (QWidget)
from PySide2.QtWidgets import *
from pyside2uic.properties import QtWidgets
import sys






'CREATE A GLOBAL VARIABLES FOR THE USER INTERFACE'
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True
GLOBAL = 0

'CREATE A ACCOUNTS.TXT FILE FOR LOGINS'
list = []
file1 = open("Accounts.txt", "w")
s = "admin,password"
file1.write(s)
file1.close()



'CREATES THE ACCOUNTS IN THE Accounts.txt file'
class Account:
    def __init__(self, userID, password):
        self.userID = userID
        self.password = password


'UI CLASSES'



'ALL THESE FILES ARE CREATED USING Qt User Interface Compiler version 5.15.1'

'THESE FILES ARE CONVERTED FROM A .UI FILE TYPE TO .PY FILE TYPE USING PYSIDE-UIC.EXE'



'UI FILE FOR THE MAIN CONVERTER WINDOW'
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(775, 458)
        MainWindow.setMinimumSize(QSize(760, 300))
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0.0738636 rgba(0, 37, 43, 255), stop:1 rgba(47, 66, 88, 255));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 25))
        self.frame_7.setStyleSheet(u"background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Frame11 = QFrame(self.frame_7)
        self.Frame11.setObjectName(u"Frame11")
        self.Frame11.setMaximumSize(QSize(25, 16777215))
        self.Frame11.setFrameShape(QFrame.StyledPanel)
        self.Frame11.setFrameShadow(QFrame.Raised)
        self.Frame11.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.Frame11)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.Frame11)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        self.Btn_Toggle.setMinimumSize(QSize(25, 25))
        self.Btn_Toggle.setMaximumSize(QSize(25, 25))
        self.Btn_Toggle.setFlat(True)

        self.horizontalLayout_3.addWidget(self.Btn_Toggle)


        self.horizontalLayout_2.addWidget(self.Frame11)

        self.MoveWindow = QFrame(self.frame_7)
        self.MoveWindow.setObjectName(u"MoveWindow")
        self.MoveWindow.setMinimumSize(QSize(610, 0))
        self.MoveWindow.setFrameShape(QFrame.StyledPanel)
        self.MoveWindow.setFrameShadow(QFrame.Raised)
        self.MoveWindow.setLineWidth(0)

        self.horizontalLayout_2.addWidget(self.MoveWindow)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(25, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_9.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Minimize = QPushButton(self.frame_9)
        self.Minimize.setObjectName(u"Minimize")
        self.Minimize.setMinimumSize(QSize(25, 25))
        self.Minimize.setMaximumSize(QSize(25, 25))
        self.Minimize.setFlat(True)

        self.verticalLayout_5.addWidget(self.Minimize)


        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(25, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Exit = QPushButton(self.frame_10)
        self.Exit.setObjectName(u"Exit")
        self.Exit.setMinimumSize(QSize(25, 25))
        self.Exit.setMaximumSize(QSize(25, 25))
        self.Exit.setFlat(True)

        self.verticalLayout_6.addWidget(self.Exit)


        self.horizontalLayout_2.addWidget(self.frame_10)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(220, 0, 220, 0)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_3.setMidLineWidth(0)
        self.label_3.setPixmap(QPixmap(u":/newPrefix/newPrefix/Images/logonobreadIcon.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 200))
        self.frame_3.setStyleSheet(u"background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.label)

        self.Links_2 = QLineEdit(self.frame_6)
        self.Links_2.setObjectName(u"Links_2")
        self.Links_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.Links_2)

        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.lineEdit_2)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(9, 9, 9, 30)
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolButton = QToolButton(self.frame_8)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(0, 20))
        self.toolButton.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.toolButton)

        self.MP4 = QRadioButton(self.frame_8)
        self.MP4.setObjectName(u"MP4")
        self.MP4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.MP4)

        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout_8.addWidget(self.frame_8)

        self.Submit = QPushButton(self.frame_5)
        self.Submit.setObjectName(u"Submit")
        self.Submit.setMinimumSize(QSize(0, 20))
        self.Submit.setMaximumSize(QSize(16777215, 20))
        self.Submit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Submit.setFlat(True)

        self.verticalLayout_8.addWidget(self.Submit)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText("")
        self.Minimize.setText("")
        self.Exit.setText("")
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Youtube Link", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Save Location", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.MP4.setText(QCoreApplication.translate("MainWindow", u"MP4", None))
        self.label_4.setText("")
        self.Submit.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
    # retranslateUi

'UI FILE FOR TELL THE USER THE CREATION OF THE ACCOUNT WAS SUCCESSFUL'
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(329, 169)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-10, -10, 341, 181))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.textBrowser)

        self.awesome_button = QPushButton(self.verticalLayoutWidget)
        self.awesome_button.setObjectName(u"awesome_button")

        self.verticalLayout.addWidget(self.awesome_button)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; tex"
                        "t-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">You have successfully registered!</span></p></body></html>", None))
        self.awesome_button.setText(QCoreApplication.translate("Dialog", u"Awesome!", None))
    # retranslateUi

'UI FILE FOR THE LOGIN PAGE'
class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(480, 620)
        Login.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 360, 100, 15))
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(185, 185, 185);")
        self.UserID_Input = QLineEdit(Login)
        self.UserID_Input.setObjectName(u"UserID_Input")
        self.UserID_Input.setGeometry(QRect(140, 250, 261, 30))
        self.UserID_Input.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Password_Input = QLineEdit(Login)
        self.Password_Input.setObjectName(u"Password_Input")
        self.Password_Input.setGeometry(QRect(140, 310, 261, 30))
        self.Password_Input.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(Login)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(250, 360, 85, 20))
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 118, 118);")
        self.UserID_Label = QLabel(Login)
        self.UserID_Label.setObjectName(u"UserID_Label")
        self.UserID_Label.setGeometry(QRect(50, 250, 71, 30))
        font1 = QFont()
        font1.setPointSize(15)
        self.UserID_Label.setFont(font1)
        self.UserID_Label.setStyleSheet(u"color: rgb(255, 32, 132);border:0;")
        self.pushButton = QPushButton(Login)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 460, 100, 30))
        font2 = QFont()
        font2.setPointSize(16)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"color: rgb(255, 242, 243);\n"
"background-color: rgb(148, 148, 148);")
        self.Password_Label = QLabel(Login)
        self.Password_Label.setObjectName(u"Password_Label")
        self.Password_Label.setGeometry(QRect(50, 310, 85, 30))
        self.Password_Label.setFont(font1)
        self.Password_Label.setStyleSheet(u"color: rgb(255, 32, 132);")
        self.Message_Label = QLabel(Login)
        self.Message_Label.setObjectName(u"Message_Label")
        self.Message_Label.setGeometry(QRect(52, 530, 375, 40))
        font3 = QFont()
        font3.setPointSize(10)
        self.Message_Label.setFont(font3)
        self.Message_Label.setStyleSheet(u"background-color: rgb(90, 90, 90);\n"
"color: rgb(255, 50, 50);")
        self.Message_Label.setAlignment(Qt.AlignCenter)
        self.Picture_Label = QLabel(Login)
        self.Picture_Label.setObjectName(u"Picture_Label")
        self.Picture_Label.setGeometry(QRect(-10, 40, 250, 200))
        self.Login_Label = QLabel(Login)
        self.Login_Label.setObjectName(u"Login_Label")
        self.Login_Label.setGeometry(QRect(185, 120, 191, 61))
        font4 = QFont()
        font4.setPointSize(40)
        self.Login_Label.setFont(font4)
        self.Login_Label.setStyleSheet(u"color: rgb(110, 156, 255);\n"
"color: rgb(255, 8, 94);\n"
"")
        self.Login_Label.setAlignment(Qt.AlignCenter)
        self.Picture_Label.raise_()
        self.label.raise_()
        self.UserID_Input.raise_()
        self.Password_Input.raise_()
        self.pushButton_2.raise_()
        self.UserID_Label.raise_()
        self.pushButton.raise_()
        self.Password_Label.raise_()
        self.Message_Label.raise_()
        self.Login_Label.raise_()

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.label.setText(QCoreApplication.translate("Login", u"No Account?", None))
        self.pushButton_2.setText(QCoreApplication.translate("Login", u"Create Account", None))
        self.UserID_Label.setText(QCoreApplication.translate("Login", u"User ID", None))
        self.pushButton.setText(QCoreApplication.translate("Login", u"Login", None))
        self.Password_Label.setText(QCoreApplication.translate("Login", u"Password", None))
        self.Message_Label.setText("")
        self.Picture_Label.setText("")
        self.Login_Label.setText(QCoreApplication.translate("Login", u"YTRam", None))
    # retranslateUi

'UI FILE FOR THE CREATING AN ACCOUNT PAGE'
class Ui_Register(object):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName(u"Login")
        Register.resize(480, 620)
        Register.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.Create_Button = QPushButton(Register)
        self.Create_Button.setObjectName(u"Create_Button")
        self.Create_Button.setGeometry(QRect(300, 430, 100, 30))
        font = QFont()
        font.setPointSize(16)
        self.Create_Button.setFont(font)
        self.Create_Button.setStyleSheet(u"color: rgb(255, 242, 243);\n"
"background-color: rgb(148, 148, 148);")
        self.UserID_Input = QLineEdit(Register)
        self.UserID_Input.setObjectName(u"UserID_Input")
        self.UserID_Input.setGeometry(QRect(140, 250, 261, 30))
        self.UserID_Input.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Password_Label = QLabel(Register)
        self.Password_Label.setObjectName(u"Password_Label")
        self.Password_Label.setGeometry(QRect(50, 310, 85, 30))
        font1 = QFont()
        font1.setPointSize(15)
        self.Password_Label.setFont(font1)
        self.Password_Label.setStyleSheet(u"color: rgb(255, 32, 132);")
        self.Login_Label = QLabel(Register)
        self.Login_Label.setObjectName(u"Login_Label")
        self.Login_Label.setGeometry(QRect(140, 110, 200, 70))
        font2 = QFont()
        font2.setPointSize(40)
        self.Login_Label.setFont(font2)
        self.Login_Label.setStyleSheet(u"color: rgb(110, 156, 255);\n"
"color: rgb(255, 8, 94);\n"
"")
        self.Login_Label.setAlignment(Qt.AlignCenter)
        self.Password_Input = QLineEdit(Register)
        self.Password_Input.setObjectName(u"Password_Input")
        self.Password_Input.setGeometry(QRect(140, 310, 261, 30))
        self.Password_Input.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Password_Label_2 = QLabel(Register)
        self.Password_Label_2.setObjectName(u"Password_Label_2")
        self.Password_Label_2.setGeometry(QRect(50, 370, 85, 30))
        font3 = QFont()
        font3.setPointSize(13)
        self.Password_Label_2.setFont(font3)
        self.Password_Label_2.setStyleSheet(u"color: rgb(255, 32, 132);")
        self.Password_Input_2 = QLineEdit(Register)
        self.Password_Input_2.setObjectName(u"Password_Input_2")
        self.Password_Input_2.setGeometry(QRect(140, 370, 261, 30))
        self.Password_Input_2.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.UserID_Label = QLabel(Register)
        self.UserID_Label.setObjectName(u"UserID_Label")
        self.UserID_Label.setGeometry(QRect(50, 250, 71, 30))
        self.UserID_Label.setFont(font1)
        self.UserID_Label.setStyleSheet(u"color: rgb(255, 32, 132);")
        self.Cancel_Button = QPushButton(Register)
        self.Cancel_Button.setObjectName(u"Cancel_Button")
        self.Cancel_Button.setGeometry(QRect(100, 430, 100, 30))
        self.Cancel_Button.setFont(font)
        self.Cancel_Button.setStyleSheet(u"color: rgb(255, 242, 243);\n"
"background-color: rgb(148, 148, 148);")
        self.Message_Label = QLabel(Register)
        self.Message_Label.setObjectName(u"Message_Label")
        self.Message_Label.setGeometry(QRect(52, 530, 375, 40))
        font4 = QFont()
        font4.setPointSize(10)
        self.Message_Label.setFont(font4)
        self.Message_Label.setStyleSheet(u"background-color: rgb(90, 90, 90);\n"
"color: rgb(255, 50, 50);")
        self.Message_Label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"Form", None))
        self.Create_Button.setText(QCoreApplication.translate("Register", u"Create", None))
        self.Password_Label.setText(QCoreApplication.translate("Register", u"Password", None))
        self.Login_Label.setText(QCoreApplication.translate("Register", u"Register", None))
        self.Password_Label_2.setText(QCoreApplication.translate("Register", u"Confirm PW", None))
        self.UserID_Label.setText(QCoreApplication.translate("Register", u"User ID", None))
        self.Cancel_Button.setText(QCoreApplication.translate("Register", u"Cancel", None))
        self.Message_Label.setText("")
    # retranslateUi




'UI Function Classes'

'THE YT_Convert_MP3 USES A SET OF PARAMERTERS TO SPECIFY A AUDIO ONLY DOWNLOAD'
class YT_Convert_MP3():
    def converter(links_Main,destinationpath):
        file1 = open("Links1.txt", 'r')
        x = (file1.readlines())
        params = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],

        }
        for y in x:
            print(y)
            if y != '\n':
                youtube = youtube_dl.YoutubeDL(params)
                youtube.download([str(y)])

        sourcepath = os.getcwd()
        sourcefiles = os.listdir(sourcepath)
        for file in sourcefiles:
            if file.endswith('.mp3'):
                shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
            elif file.endswith(('.mp4')):
                shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath, file))
            elif file.endswith('.webm'):
                shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath, file))
            elif file.endswith(('.mkv')):
                shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath, file))
        file1.close()

'THE YT_Convert_MP4() USES ONE PARAMERTER TO DOWNLOAD A ALL IN ONE MP4 FILE'
class YT_Convert_MP4():
    def converter(links_Main,destinationpath):
        import ffmpeg
        import ffprobe
        file1 = open("Links1.txt", 'r')
        x = (file1.readlines())
        for y in x:
            print(y)
            if y != '\n':

                youtube = youtube_dl.YoutubeDL()
                youtube.extract_info((y))
        sourcepath = os.getcwd()
        sourcefiles = os.listdir(sourcepath)
        for file in sourcefiles:
            if file.endswith('.mkv'):
                shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
            elif file.endswith(('.mp4')):
                shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath, file))
            elif file.endswith('.webm'):
                shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath, file))
            elif file.endswith(('.mkv')):
                shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath, file))
        file1.close()


'MainWindow Classes'

'LOGIN CLASS THAT INTIALIZES THE LOGIN PAGE USING THE Ui_Login CLASS'
class Login(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        #pixmap = QGraphicsPixmapItem('logo.png')
        #self.Picture_Label.setPixmap(pixmap)
        self.ui.pushButton.clicked.connect(self.loginfunction)
        self.ui.Password_Input.setEchoMode(QLineEdit.Password) #Hides password
        self.ui.pushButton_2.clicked.connect(self.gotocreate)
        pixmap = QPixmap('logo.png')
        self.ui.Picture_Label.setPixmap(pixmap)
        self.ui.Picture_Label.setScaledContents(True)
        #self.setWindowTitle('YTRAM')
        self.show()
        #Initialize list of accounts
        with open('Accounts.txt', 'r') as f:
            for line in f:
                #print(line)
                if line == "\n" : continue
                temp_string = line.split(',')
                temp = Account(temp_string[0], temp_string[1])
                list.append(temp)

        for items in list:
            print('items:', items.userID)


    def gotocreate(self):
        # Switch Screen
        createacc = CreateAcc()
        self.hide()
        self.addWidget(createacc)
        self.setCurrentIndex(self.currentIndex()+1)
    def gotomain(self):
        #Switch screen
        createmainwindow = MainWindow()
        self.hide()
        self.addWidget(createmainwindow)
        self.setCurrentIndex(self.currentIndex()+1)
        self.setFixedWidth(800)
        self.setFixedHeight(600)

    def loginfunction(self):
        userID = self.ui.UserID_Input.text()
        password = self.ui.Password_Input.text()
        userID = userID.strip('\n')
        password = password.strip('\n')
        checker = 0

        with open('Accounts.txt', 'r') as f:
            for line in f:
                if line == "\n" : continue
                temp_string = line.split(',')
                temp_string[0] = temp_string[0].strip('\n')
                temp_string[1] = temp_string[1].strip('\n')

                if (userID == temp_string[0]):
                    print(userID, 'detected')
                    if (temp_string[1] == password):
                        print(temp_string[0], 'has successfully logged in')
                        checker = 1

                        self.gotomain()



                        #login function here
                        break;
                    else :
                        print('Incorrect Password')
                        self.ui.Message_Label.setText('Incorrect User ID or Password')

        if (not checker) :
            print("Incorrect User ID or Password")
            self.ui.Message_Label.setText('Incorrect User ID or Password')

'DIALOG CLASS THAT INITALIZES THE DIALOG PAGE USING THE Ui_Dialog CLASS'
class Dialog(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.awesome_button.clicked.connect(self.closefunction)
        self.show()


    def closefunction(self):
        # Switch Screen
        login = Login()
        self.hide()
        self.ui.addWidget(login)
        self.ui.setCurrentIndex(self.currentIndex() + 1)
        self.ui.setFixedWidth(480)
        self.ui.setFixedHeight(620)

'CREATEACC CLASS THAT INITALIZES THE CREATE ACCOUNT PAGE USING THE Ui_Register CLASS'
class CreateAcc(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Register()
        self.ui.setupUi(self)
        self.ui.Create_Button.clicked.connect(self.createaccfunction)
        self.ui.Cancel_Button.clicked.connect(self.cancelfunction)
        self.ui.Password_Input.setEchoMode(QLineEdit.Password)  # Hides password
        self.ui.Password_Input_2.setEchoMode(QLineEdit.Password)  # Hides password
        self.show()

    def createaccfunction(self):

        if ((len(self.ui.UserID_Input.text()) < 4
                or len(self.ui.UserID_Input.text()) > 12)
                or (len(self.ui.Password_Input.text()) < 4)
                or len(self.ui.Password_Input.text()) > 12):
            print("UserID or Password too short")
            self.ui.Message_Label.setText("User ID and Password must be between 4 and 12 characters!")

        if (sum(c.isalpha() for c in self.ui.UserID_Input.text()) < 4):
            print("UserID must contain at least 4 characters")
            self.ui.Message_Label.setText('User ID must contain at least 4 alphabetical characters')

        if self.ui.Password_Input.text() != self.ui.Password_Input_2.text():
            print("Password input does not match confirm password")
            self.ui.Message_Label.setText('Password input does not match confirm password entry')

        if (' ' in self.ui.UserID_Input.text()): userID_space = 1
        else: userID_space = 0
        if (' ' in self.ui.Password_Input.text()): password_space = 1
        else: password_space = 0

        if (userID_space or password_space) :
            print("UserID and PW cannot contain spaces")
            self.ui.Message_Label.setText("UserID and Password cannot contain spaces")

        with open('Accounts.txt', 'r') as f:
            for line in f:
                if line == "\n" : continue
                temp_string = line.split(',')
                user_checker = temp_string[0]
                if (user_checker == self.ui.UserID_Input.text()):
                    print("UserID:", self.ui.UserID_Input.text(), "already exists.")
                    temp_string = 'User ID: ' + self.ui.UserID_Input.text() + ' already exists.'
                    self.ui.Message_Label.setText(temp_string)
                    break



        if (self.ui.Password_Input.text() == self.ui.Password_Input_2.text()) \
        and (len(self.ui.UserID_Input.text()) >= 4
        and len(self.ui.Password_Input.text()) >= 4)\
        and (sum(c.isalpha() for c in self.ui.UserID_Input.text()) >= 4)\
        and (user_checker != self.ui.UserID_Input.text())\
        and (len(self.ui.UserID_Input.text()) <= 12)\
        and (len(self.ui.Password_Input.text()) <= 12)\
        and (not(userID_space) and not(password_space)):

            userID = self.ui.UserID_Input.text()

            password=self.ui.Password_Input.text()
            temp = userID + ',' + password
            #print('temp: ',temp)
            print("Created Account:", userID, password)

            with open('Accounts.txt', 'a') as wf:
                wf.write('\n')
                wf.write(temp)

            dialog = Dialog()
            self.ui.addWidget(dialog)
            self.hide()
            self.setCurrentIndex(self.currentIndex() + 1)

            #Switch Screen
            login=Login()
            self.ui.addWidget(login)
            self.hide()
            self.setCurrentIndex(self.currentIndex()+1)

    def cancelfunction(self):
        self.hide()
        print("Cancel Detected")
        login=Login()
        self.addWidget(login)

        self.setCurrentIndex(self.currentIndex()+1)

'MAINWINDOW CLASS THAT INITIALIZES THE YOUTUBE CONVERTER PAGE USING THE Ui_MainWindow CLASS'
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        MainWindow_Open = True
        self.ui.Btn_Toggle.setIcon(QIcon('menu.png'))
        'ALLOWS THE YOUTUBE CONVERTER TO BE CLOSED'
        def close_window_Ram(bool):
                MainWindow = bool

        'REMOVES THE DEFAULT TITLEBAR'
        def remove_titlebar(status):
                global GLOBAL_TITLE_BAR
                GLOBAL_TITLE_BAR = status
        'ALLOWS THE USER TO MOVE THE WINDOW'
        def moveWindow(event):  # !!!
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)

                self.dragPos = event.globalPos()
                event.accept()
        self.ui.MoveWindow.mouseMoveEvent = moveWindow
        # self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 70, True))

        'THE NEXT FEW LINKS OF CODE MAKE THE UI MORE ASTHTIC AND ALSO INTERACTS WITH Ui_MainWindow CLASS'
        remove_titlebar(True)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.Exit.clicked.connect(close_window_Ram(False))
        self.ui.Exit.setIcon(QIcon('cancel.png'))
        self.ui.Exit.clicked.connect(lambda: sys.exit(app.exec_()))
        self.ui.Minimize.clicked.connect(lambda: QMainWindow.hide())
        self.ui.Minimize.setIcon(QIcon('minus.png'))
        print(self.ui.MP4.isChecked())
        self.ui.Submit.clicked.connect(self.Links_Textbox)
        pixmap = QPixmap('logonobreadIcon.png')
        self.ui.label_3.setPixmap(pixmap)
        self.ui.label_3.setScaledContents(True)
        self.show()

    'COMMUNICATES WITH THE moveWindow DEF TO HELP IT MOVE'
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    'COMMUNITCATES WITH YT_Convert_MP3 AND YT_Convert_MP4 TO CONVERT THE FILES'
    def Links_Textbox(self):

        if(self.ui.MP4.isChecked() == True):
            'COMMUNITICATES WITH YT_Convert_MP4 BY CHECKING IF THE CHECK BOX IS CLICKED'
            import os
            Links = self.ui.Links_2.text()
            file1 = open("Links1.txt", 'w+')
            file1.writelines(Links)
            file1.close()
            SourcePath = self.ui.lineEdit_2.text()
            'USES THE TRY AND EXCEPT METHOD TO DETECT IF THE YOUTUBE LINK OR THE FILE LOCATIONS ARE VAILD'
            try:
                try:
                    YT_Convert_MP4.converter(Links, SourcePath)
                    self.ui.label_4.setText('Vaild')
                except FileNotFoundError:
                    self.ui.label_4.setText('Invalid File Directory')
            except youtube_dl.utils.DownloadError:
                self.ui.label_4.setText('Invalid Youtube Link')

            sourcepath = os.getcwd()
            sourcefiles = os.listdir(sourcepath)
            'CHANGES THE LOCATIONS OF THE SORUCEFILES TO THE LOCATION SPECIFIED BY THE USER'
            for file in sourcefiles:
                if file.endswith('.mkv'):
                    shutil.move(os.path.join(sourcepath, file), os.path.join(SourcePath, file))
                    self.ui.label_4.setText('Vaild')
                elif file.endswith(('.mp4')):
                    shutil.move(os.path.join(sourcepath, file), os.path.join(SourcePath, file))
                    self.ui.label_4.setText('Vaild')
                elif file.endswith('.webm'):
                    shutil.move(os.path.join(sourcepath, file), os.path.join(SourcePath, file))
                    self.ui.label_4.setText('Vaild')
                elif file.endswith(('.mkv')):
                    shutil.move(os.path.join(sourcepath, file), os.path.join(SourcePath, file))
                    self.ui.label_4.setText('Vaild')
                elif file.endswith(('.m4a')):
                    shutil.move(os.path.join(sourcepath, file), os.path.join(SourcePath, file))
                    self.ui.label_4.setText('Vaild')

            os.remove("Links1.txt")
        else:
            'COMMUNITICATES WITH YT_Convert_MP3 BY CHECKING IF THE CHECK BOX IS CLICKED'
            import os
            Links = self.ui.Links_2.text()
            file1 = open("Links1.txt", 'w+')
            file1.writelines(Links)
            file1.close()
            SourcePath = self.ui.lineEdit_2.text()
            'USES THE TRY AND EXCEPT METHOD TO DETECT IF THE YOUTUBE LINK OR THE FILE LOCATIONS ARE VAILD'
            try:
                try:
                    YT_Convert_MP3.converter(Links, SourcePath)
                    self.ui.label_4.setText('Vaild')
                except FileNotFoundError:
                    self.ui.label_4.setText('Invalid File Directory')
            except youtube_dl.utils.DownloadError:
                self.ui.label_4.setText('Invalid Youtube Link')

            sourcepath = os.getcwd()
            sourcefiles = os.listdir(sourcepath)
            'CHANGES THE LOCATIONS OF THE SORUCEFILES TO THE LOCATION SPECIFIED BY THE USER'
            for file in sourcefiles:
                if file.endswith('.mkv'):
                    shutil.move(os.path.join(sourcepath, file), os.path.join(SourcePath, file))
                    self.ui.label_4.setText('Vaild')
                elif file.endswith(('.mp4')):
                    shutil.move(os.path.join(sourcepath, file), os.path.join(SourcePath, file))
                    self.ui.label_4.setText('Vaild')
                elif file.endswith('.webm'):
                    shutil.move(os.path.join(sourcepath, file), os.path.join(SourcePath, file))
                    self.ui.label_4.setText('Vaild')
                elif file.endswith(('.mkv')):
                    shutil.move(os.path.join(sourcepath, file), os.path.join(SourcePath, file))
                    self.ui.label_4.setText('Vaild')
                elif file.endswith(('.m4a')):
                    shutil.move(os.path.join(sourcepath, file), os.path.join(SourcePath, file))
                    self.ui.label_4.setText('Vaild')



            os.remove("Links1.txt")



    global MainWindow_Open1
    MainWindow_Open1 = True
    def close_window_Ram(bool):
        MainWindow = bool


'USED TO INIIALIZE THE ENTIRE CODE ABOVE'
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    sys.exit(app.exec_())