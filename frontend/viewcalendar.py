# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewcalendar.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from backend.utils import MeetingData
import datetime
from frontend.utils import _translate_slot_backward_key, _translate_slot_backward, _translate_slot_forward


meeting_data = MeetingData()

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
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(16)
        self.tableWidget.setVerticalHeaderLabels([""]*16)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        self.tableWidget.horizontalHeader().setDefaultSectionSize(270)

        self.retranslateUi(ViewCalendar)
        QtCore.QMetaObject.connectSlotsByName(ViewCalendar)

    def retranslateUi(self, ViewCalendar):
        _translate = QtCore.QCoreApplication.translate
        ViewCalendar.setWindowTitle(_translate("ViewCalendar", "Frame"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ViewCalendar", "Time"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ViewCalendar", "Meeting"))



class ViewCalendar(QtWidgets.QFrame, Ui_ViewCalendar):
    def __init__(self, user, parent=None):
        super(ViewCalendar, self).__init__(parent)
        self.setupUi(self) 
        self.user = user
        self.showDate(date = self.calendarWidget.selectedDate())
        self.calendarWidget.clicked[QtCore.QDate].connect(self.showDate)

    def showDate(self, date):
        self.delete_meeting_list()
        date = date.toPyDate()
        meetings = meeting_data.get_meetings_by_date_and_user(date, self.user)

        self.tableWidget.setRowCount(len(meetings))
        zipped = zip(
            [m.title for m in meetings],
            [[self.translate_timeslot(ts) for ts in m.timeslots] for m in meetings]
            )
        zipped = sorted(zipped,key=lambda m:m[1])
        rowcount = 0
        for title, times in zipped:
            print(rowcount)
            item = QtWidgets.QTableWidgetItem(title)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(rowcount, 1, item)

            item = QtWidgets.QTableWidgetItem(self.show_time(sorted(times)))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(rowcount, 0, item)

            rowcount += 1

    def translate_timeslot(self, ts):
        if isinstance(ts.begin_time, str):
            time = _translate_slot_backward_key(ts.begin_time)
        else:
            time = _translate_slot_backward(ts.begin_time.value)
        return time

    def show_time(self, times):
        start = _translate_slot_forward(times[0])
        end = _translate_slot_forward(times[-1] + 1)
        return "{} - {}".format(start, end)

    def delete_meeting_list(self):
        for i in reversed(range(self.tableWidget.rowCount())):
            self.tableWidget.removeRow(i)









