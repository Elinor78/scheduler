# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewnotifications.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewNotifications(object):
    def setupUi(self, ViewNotifications):
        ViewNotifications.setObjectName("ViewNotifications")
        ViewNotifications.resize(581, 391)
        ViewNotifications.setGeometry(QtCore.QRect(230, 30, 581, 391))

        self.tableWidget = QtWidgets.QTableWidget(ViewNotifications)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 561, 371))
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(139)

        self.retranslateUi(ViewNotifications)
        QtCore.QMetaObject.connectSlotsByName(ViewNotifications)

    def retranslateUi(self, ViewNotifications):
        _translate = QtCore.QCoreApplication.translate
        ViewNotifications.setWindowTitle(_translate("ViewNotifications", "Frame"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ViewNotifications", "Time"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ViewNotifications", "Meeting Owner"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ViewNotifications", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ViewNotifications", "Accept/Decline"))

