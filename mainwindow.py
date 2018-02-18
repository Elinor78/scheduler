# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 473)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(827, 473))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 191, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.schedule_meeting_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.schedule_meeting_button.setObjectName("schedule_meeting_button")
        self.verticalLayout.addWidget(self.schedule_meeting_button)
        self.view_calendar_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.view_calendar_button.setObjectName("view_calendar_button")
        self.verticalLayout.addWidget(self.view_calendar_button)
        self.view_profile_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.view_profile_button.setObjectName("view_profile_button")
        self.verticalLayout.addWidget(self.view_profile_button)
        self.view_notifications_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.view_notifications_button.setObjectName("view_notifications_button")
        self.verticalLayout.addWidget(self.view_notifications_button)
        self.view_daily_schedule_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.view_daily_schedule_button.setObjectName("view_daily_schedule_button")
        self.verticalLayout.addWidget(self.view_daily_schedule_button)
        self.logout_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.logout_button.setObjectName("logout_button")
        self.verticalLayout.addWidget(self.logout_button)
        self.manage_rooms_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.manage_rooms_button.setEnabled(False)
        self.manage_rooms_button.setObjectName("manage_rooms_button")
        self.verticalLayout.addWidget(self.manage_rooms_button)
        self.manage_users_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.manage_users_button.setEnabled(False)
        self.manage_users_button.setObjectName("manage_users_button")
        self.verticalLayout.addWidget(self.manage_users_button)
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(230, 30, 581, 391))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.view_calendar_button, self.schedule_meeting_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scheduler"))
        self.schedule_meeting_button.setText(_translate("MainWindow", "Schedule Meeting"))
        self.view_calendar_button.setText(_translate("MainWindow", "View Calendar"))
        self.view_profile_button.setText(_translate("MainWindow", "View Profile"))
        self.view_notifications_button.setText(_translate("MainWindow", "View Notifications"))
        self.view_daily_schedule_button.setText(_translate("MainWindow", "View Daily Schedule"))
        self.logout_button.setText(_translate("MainWindow", "Logout"))
        self.manage_rooms_button.setText(_translate("MainWindow", "Manage Rooms"))
        self.manage_users_button.setText(_translate("MainWindow", "Manage Users"))

