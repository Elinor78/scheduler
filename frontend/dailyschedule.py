# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dailyschedule.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from backend.utils import MeetingData
from frontend.utils import _translate_slot_backward, _translate_slot_backward_key

meeting_data = MeetingData()

class Ui_DailySchedule(object):
    def setupUi(self, DailySchedule):
        DailySchedule.setObjectName("DailySchedule")
        DailySchedule.resize(581, 391)
        DailySchedule.setGeometry(QtCore.QRect(230, 30, 581, 391))
        self.label = QtWidgets.QLabel(DailySchedule)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 21))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(DailySchedule)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 561, 341))
        self.tableWidget.setRowCount(16)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(["Time", "Meetings"])
        self.tableWidget.setVerticalHeaderLabels([""]*16)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(12, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(13, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(14, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(15, 0, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(265)
        self.tableWidget.horizontalHeader().setHighlightSections(True)

        self.retranslateUi(DailySchedule)
        QtCore.QMetaObject.connectSlotsByName(DailySchedule)

    def retranslateUi(self, DailySchedule):
        _translate = QtCore.QCoreApplication.translate
        DailySchedule.setWindowTitle(_translate("DailySchedule", "Frame"))
        self.label.setText(_translate("DailySchedule", "Date"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("DailySchedule", "9:00 am"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("DailySchedule", "9:30 am"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("DailySchedule", "10:00 am"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("DailySchedule", "10:30 am"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("DailySchedule", "11:00 am"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("DailySchedule", "11:30 am"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("DailySchedule", "12:00 pm"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("DailySchedule", "12:30 pm"))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("DailySchedule", "1:00 pm"))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("DailySchedule", "1:30 pm"))
        item = self.tableWidget.item(10, 0)
        item.setText(_translate("DailySchedule", "2:00 pm"))
        item = self.tableWidget.item(11, 0)
        item.setText(_translate("DailySchedule", "2:30 pm"))
        item = self.tableWidget.item(12, 0)
        item.setText(_translate("DailySchedule", "3:00 pm"))
        item = self.tableWidget.item(13, 0)
        item.setText(_translate("DailySchedule", "3:30 pm"))
        item = self.tableWidget.item(14, 0)
        item.setText(_translate("DailySchedule", "4:00 pm"))
        item = self.tableWidget.item(15, 0)
        item.setText(_translate("DailySchedule", "4:30 pm"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)


class DailySchedule(QtWidgets.QFrame, Ui_DailySchedule):
    def __init__(self, user, parent=None):
        super(DailySchedule, self).__init__(parent)
        self.setupUi(self)
        self.user = user
        self.set_date()
        self.get_current_meetings()

    def set_date(self):
        today = datetime.date.today()
        self.label.setText(today.strftime('%B %d %Y'))
        width = self.label.fontMetrics().boundingRect(self.label.text()).width()
        height = self.label.fontMetrics().boundingRect(self.label.text()).height()
        self.label.resize(width, height)

    def get_current_meetings(self):
        today = datetime.date.today()
        meetings = meeting_data.get_meetings_by_date_and_user(date=today, employee=self.user)
        print(meetings)
        print([m.timeslots for m in meetings])
        '''
        zipped = zip(
            [m.title for m in meetings],
            [[self._translate_slot_backward(ts.begin_time.value) for ts in m.timeslots] for m in meetings]
            )
        for title, times in zipped:
            for time in times:
                item = QtWidgets.QTableWidgetItem(title)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(time, 1, item)
        '''
        for m in meetings:
            for ts in m.timeslots:
                if isinstance(ts.begin_time, str):
                    time = _translate_slot_backward_key(ts.begin_time)
                else:
                    time = _translate_slot_backward(ts.begin_time.value)
                item = QtWidgets.QTableWidgetItem(m.title)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(time, 1, item)                




    def _translate_slot_forward(self, i):
        tmp = {
            0: "9:00 am",
            1: "9:30 am",
            2: "10:00 am",
            3: "10:30 am",
            4: "11:00 am",
            5:"11:30 am",
            6: "12:00 pm",
            7: "12:30 pm",
            8:  "1:00 pm",
            9: "1:30 pm",
            10: "2:00 pm",
            11: "2:30 pm",
            12:  "3:00 pm",
            13:  "3:30 pm",
            14:  "4:00 pm",
            15: "4:30 pm"
        }
        return tmp[i]

    def _translate_slot_backward(self, i):
        tmp = {
            "9:00 am": 0,
            "9:30 am": 1,
            "10:00 am": 2,
            "10:30 am": 3,
            "11:00 am": 4,
            "11:30 am": 5,
            "12:00 pm": 6,
            "12:30 pm": 7,
            "1:00 pm": 8,
            "1:30 pm": 9,
            "2:00 pm": 10,
            "2:30 pm": 11,
            "3:00 pm": 12,
            "3:30 pm": 13,
            "4:00 pm": 14,
            "4:30 pm": 15
        }
        return tmp[i]






