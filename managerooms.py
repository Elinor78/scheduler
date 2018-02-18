# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'managerooms.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ManageRooms(object):
    def setupUi(self, ManageRooms):
        ManageRooms.setObjectName("ManageRooms")
        ManageRooms.resize(581, 391)
        ManageRooms.setGeometry(QtCore.QRect(230, 30, 581, 391))
        self.tableWidget = QtWidgets.QTableWidget(ManageRooms)
        self.tableWidget.setGeometry(QtCore.QRect(15, 11, 551, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(109)
        self.add_room_button = QtWidgets.QPushButton(ManageRooms)
        self.add_room_button.setGeometry(QtCore.QRect(430, 340, 113, 32))
        self.add_room_button.setObjectName("add_room_button")

        self.retranslateUi(ManageRooms)
        QtCore.QMetaObject.connectSlotsByName(ManageRooms)

    def retranslateUi(self, ManageRooms):
        _translate = QtCore.QCoreApplication.translate
        ManageRooms.setWindowTitle(_translate("ManageRooms", "Manage Rooms"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ManageRooms", "Room Number"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ManageRooms", "Building"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ManageRooms", "Capacity"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ManageRooms", "Edit"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ManageRooms", "Delete"))
        self.add_room_button.setText(_translate("ManageRooms", "Add Room"))

