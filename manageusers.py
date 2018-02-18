# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manageusers.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ManageUsers(object):
    def setupUi(self, ManageUsers):
        ManageUsers.setObjectName("ManageUsers")
        ManageUsers.resize(581, 391)
        ManageUsers.setGeometry(QtCore.QRect(230, 30, 581, 391))

        self.tableWidget = QtWidgets.QTableWidget(ManageUsers)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 541, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(134)
        self.add_user_button = QtWidgets.QPushButton(ManageUsers)
        self.add_user_button.setGeometry(QtCore.QRect(450, 320, 113, 32))
        self.add_user_button.setObjectName("add_user_button")

        self.retranslateUi(ManageUsers)
        QtCore.QMetaObject.connectSlotsByName(ManageUsers)

    def retranslateUi(self, ManageUsers):
        _translate = QtCore.QCoreApplication.translate
        ManageUsers.setWindowTitle(_translate("ManageUsers", "Manage Users"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ManageUsers", "Username"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ManageUsers", "Password"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ManageUsers", "Generate Password"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ManageUsers", "Delete User"))
        self.add_user_button.setText(_translate("ManageUsers", "Add User"))

