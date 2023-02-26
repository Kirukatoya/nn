# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prokqleeO.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(False)
        MainWindow.resize(1025, 641)
        MainWindow.setStyleSheet(u"*{\n"
"   border: none;\n"
"   background-color: transparent;\n"
"   background: none;\n"
"   padding: 0;\n"
"   margin: 0;\n"
"   color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: rgb(77, 80, 85);\n"
"}\n"
"#LeftMenuContainer {\n"
"	\n"
"	background-color: rgb(80, 70, 85);\n"
"}\n"
"#LeftMenuContainer QPushButton{\n"
"text-align:left;\n"
"padding: 15px 15px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"}\n"
"#frame_3{\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuContainer = QWidget(self.centralwidget)
        self.LeftMenuContainer.setObjectName(u"LeftMenuContainer")
        self.LeftMenuContainer.setEnabled(False)
        self.LeftMenuContainer.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.LeftMenuContainer)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.LeftMenuContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.MenuBtn = QPushButton(self.frame)
        self.MenuBtn.setObjectName(u"MenuBtn")
        self.MenuBtn.setEnabled(False)
        self.MenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.MenuBtn)

        self.HomeBtn = QPushButton(self.frame)
        self.HomeBtn.setObjectName(u"HomeBtn")
        self.HomeBtn.setEnabled(False)
        self.HomeBtn.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.HomeBtn.setIconSize(QSize(24, 24))
        self.HomeBtn.setCheckable(False)
        self.HomeBtn.setAutoRepeat(False)
        self.HomeBtn.setAutoExclusive(False)
        self.HomeBtn.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.HomeBtn)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.LeftMenuContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.NewTaskBtn = QPushButton(self.frame_2)
        self.NewTaskBtn.setObjectName(u"NewTaskBtn")
        self.NewTaskBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.NewTaskBtn)

        self.SaveBtn = QPushButton(self.frame_2)
        self.SaveBtn.setObjectName(u"SaveBtn")
        self.SaveBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.SaveBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.HelpBtn = QPushButton(self.frame_2)
        self.HelpBtn.setObjectName(u"HelpBtn")
        self.HelpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.HelpBtn)

        self.InformationBtn = QPushButton(self.frame_2)
        self.InformationBtn.setObjectName(u"InformationBtn")
        self.InformationBtn.setEnabled(False)
        self.InformationBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.InformationBtn)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout_2.addWidget(self.LeftMenuContainer, 0, Qt.AlignLeft)

        self.mainBodyCotntainer = QWidget(self.centralwidget)
        self.mainBodyCotntainer.setObjectName(u"mainBodyCotntainer")
        self.horizontalLayout = QHBoxLayout(self.mainBodyCotntainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CenterMenuSubContainer = QWidget(self.mainBodyCotntainer)
        self.CenterMenuSubContainer.setObjectName(u"CenterMenuSubContainer")
        self.CenterMenuSubContainer.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.CenterMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.CenterMenuSubContainer.setSizePolicy(sizePolicy1)
        self.CenterMenuSubContainer.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.CenterMenuSubContainer)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.CenterMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:11, stop:0 rgba(51, 64, 22, 255), stop:0.121053 rgba(102, 79, 16, 255), stop:0.225 rgba(122, 102, 30, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(157, 145, 68, 255), stop:0.415 rgba(172, 164, 79, 255), stop:0.52 rgba(166, 150, 60, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(152, 140, 59, 255), stop:0.815789 rgba(166, 148, 58, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"\n"
"border-radius: 10px;")

        self.verticalLayout_5.addWidget(self.label_3)


        self.verticalLayout_4.addWidget(self.frame_4, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_3 = QFrame(self.CenterMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(80, 70, 85);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.verticalLayout_7 = QVBoxLayout(self.Home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.Home)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Franklin Gothic Medium")
        self.label.setFont(font)

        self.verticalLayout_7.addWidget(self.label)

        self.stackedWidget.addWidget(self.Home)
        self.Help = QWidget()
        self.Help.setObjectName(u"Help")
        self.verticalLayout_8 = QVBoxLayout(self.Help)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.Help)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_8.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.Help)
        self.Info = QWidget()
        self.Info.setObjectName(u"Info")
        self.verticalLayout_9 = QVBoxLayout(self.Info)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.Info)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_9.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.Info)
        self.NewTask = QWidget()
        self.NewTask.setObjectName(u"NewTask")
        self.formLayout = QFormLayout(self.NewTask)
        self.formLayout.setObjectName(u"formLayout")
        self.frame_5 = QFrame(self.NewTask)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_11.addWidget(self.label_6)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.frame_5)

        self.frame_6 = QFrame(self.NewTask)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.verticalLayout_10.addWidget(self.label_16)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.gridLayout_2.addWidget(self.label_14, 3, 0, 1, 1)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)

        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.gridLayout_2.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_15_Vi1 = QLabel(self.frame_6)
        self.label_15_Vi1.setObjectName(u"label_15_Vi1")
        self.label_15_Vi1.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_15_Vi1, 0, 1, 1, 1)

        self.label_16_Vi2 = QLabel(self.frame_6)
        self.label_16_Vi2.setObjectName(u"label_16_Vi2")
        self.label_16_Vi2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_16_Vi2, 1, 1, 1, 1)

        self.label_17_Vi3 = QLabel(self.frame_6)
        self.label_17_Vi3.setObjectName(u"label_17_Vi3")
        self.label_17_Vi3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_17_Vi3, 2, 1, 1, 1)

        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_15, 3, 1, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_2)


        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.frame_6)

        self.stackedWidget.addWidget(self.NewTask)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.CenterMenuSubContainer)


        self.horizontalLayout_2.addWidget(self.mainBodyCotntainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SmartBubble", None))
#if QT_CONFIG(tooltip)
        self.MenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.MenuBtn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
#if QT_CONFIG(tooltip)
        self.HomeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.HomeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.NewTaskBtn.setToolTip(QCoreApplication.translate("MainWindow", u"New task", None))
#endif // QT_CONFIG(tooltip)
        self.NewTaskBtn.setText(QCoreApplication.translate("MainWindow", u"New task", None))
#if QT_CONFIG(tooltip)
        self.SaveBtn.setToolTip(QCoreApplication.translate("MainWindow", u"save the recommendation file", None))
#endif // QT_CONFIG(tooltip)
        self.SaveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(tooltip)
        self.HelpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"leave a request", None))
#endif // QT_CONFIG(tooltip)
        self.HelpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
#if QT_CONFIG(tooltip)
        self.InformationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Information", None))
#endif // QT_CONFIG(tooltip)
        self.InformationBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">SmartBubble</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Welcome to SmartBubble </span></p><p align=\"center\"><span style=\" font-size:9pt;\">Click &quot;New Job&quot; in the menu on the left to get started.</span></p><p align=\"center\"><span style=\" font-size:9pt;\">If this is your first time working in this program, select &quot;Information&quot; to familiarize yourself with the basic functions.</span></p><p align=\"center\"><span style=\" font-size:9pt;\">If you're having trouble or would like to suggest ideas for improving SmartBubble, use the &quot;Help&quot; menu item.</span></p><p align=\"center\"><span style=\" font-size:9pt;\">Good luck!</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Contact information for user feedback and support:</p><p align=\"center\"><br/></p><p align=\"center\">If you have any questions about using SmartBubble, please contact our support team by emailing <span style=\" font-weight:600;\">support_smartbubble@mail.com</span>. </p><p align=\"center\">We will make every effort to respond to your request within 24 hours.</p><p align=\"center\">Feedback and suggestions for improving SmartBubble:</p><p align=\"center\">We always welcome feedback and suggestions from our users to help us improve the SmartBubble service.</p><p align=\"center\"> If you have any ideas or suggestions for improving our service, please email us at <span style=\" font-weight:600;\">feedback_smartbubble@mail.com</span>. </p><p align=\"center\">We will certainly consider your suggestion and respond to your message within a few days. Thank you for your participation in improving SmartBubble!</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0441\u0435\u0440\u0432\u0438\u0441\u0430 SmartBubble</p><p align=\"center\">\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f \u043f\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044e</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Please enter the details of your car wash</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Average number of car wash customers per hour", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Average service time per customer (in minutes)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Average number of service channels", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"queue length limitation", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Calculated indicators and recommendations</p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"queue length limitation", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Average service time per customer (in minutes)", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Average number of service channels", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Average number of car wash customers per hour", None))
        self.label_15_Vi1.setText("")
        self.label_16_Vi2.setText("")
        self.label_17_Vi3.setText("")
        self.label_15.setText("")
    # retranslateUi

