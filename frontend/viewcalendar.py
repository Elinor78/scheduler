# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewcalendar.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewCalendar(object):
    def setupUi(self, ViewCalendar):
        ViewCalendar.setObjectName("ViewCalendar")
        ViewCalendar.resize(581, 391)
        ViewCalendar.setGeometry(QtCore.QRect(230, 30, 581, 391))

        self.calendarWidget = QtWidgets.QCalendarWidget(ViewCalendar)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 10, 541, 191))
        self.calendarWidget.setMaximumDate(QtCore.QDate(7918, 6, 30))
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.tableWidget = QtWidgets.QTableWidget(ViewCalendar)
        self.tableWidget.setGeometry(QtCore.QRect(20, 200, 541, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(179)

        self.retranslateUi(ViewCalendar)
        QtCore.QMetaObject.connectSlotsByName(ViewCalendar)

    def retranslateUi(self, ViewCalendar):
        _translate = QtCore.QCoreApplication.translate
        ViewCalendar.setWindowTitle(_translate("ViewCalendar", "Frame"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ViewCalendar", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ViewCalendar", "Meeting"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ViewCalendar", "Modify"))


class ViewCalendar(QtWidgets.QFrame, Ui_ViewCalendar):
    def __init__(self, user, parent=None):
        super(ViewCalendar, self).__init__(parent)
        self.setupUi(self) 