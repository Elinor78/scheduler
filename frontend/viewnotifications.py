# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewnotifications.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from backend.utils import MeetingData, EmployeeData, EmployeeMeetingData
from frontend.utils import _translate_slot_backward_key, _translate_slot_backward

meeting_data = MeetingData()
employee_data = EmployeeData()
emp_meet_data = EmployeeMeetingData()

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
        self.tableWidget.verticalHeader().hide()
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
        item.setText(_translate("ViewNotifications", "Meeting"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ViewNotifications", "Meeting Owner"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ViewNotifications", "Schedule"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ViewNotifications", "Accept/Decline"))

class ViewNotifications(QtWidgets.QFrame, Ui_ViewNotifications):
    def __init__(self, user, parent=None):
        super(ViewNotifications, self).__init__(parent)
        self.setupUi(self) 
        self.user = user
        self.employee_meetings = []
        self.populate_meetings()

    def populate_meetings(self):
        meetings = meeting_data.get_meetings_by_user(self.user)
        #meetings += meeting_data.get_owned_meetings(self.user.id)
        print (meetings)
        print ([m.id for m in meetings])
        print("In populate_meetings")
        print(meetings)
        num_meetings = len(meetings)
        self.tableWidget.setRowCount(num_meetings)
        zipped = zip(
            [m for m in meetings],
            [[self.translate_timeslot(ts) for ts in m.timeslots] for m in meetings]
            )
        zipped = sorted(zipped,key=lambda m:m[1])

        rowcount = 0

        for meeting, times in zipped:

            date = meeting.date 
            title = meeting.title 
            owner = meeting.owner
            print (meeting.title)
            
            if owner == self.user.id:
                print ("in owner")
                #num_meetings -= 1
                #self.tableWidget.setRowCount(num_meetings)
                self.employee_meetings.append(meeting)
                item = QtWidgets.QTableWidgetItem(title)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(rowcount, 0, item)

                owner = employee_data.get_employee(owner)
                name = "{} ({} {})".format(
                    owner.username,
                    owner.first_name,
                    owner.last_name
                    )
                item = QtWidgets.QTableWidgetItem(name)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(rowcount, 1, item)

                t =  self.show_time(sorted(times))
                d = date.strftime('%m/%d/%y')
                dt = "{}, {}".format(d,t)
                item = QtWidgets.QTableWidgetItem(dt)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(rowcount, 2, item)
                # add cancel button

                self.cancel_btn = QtWidgets.QPushButton("Cancel")
                self.cancel_btn.clicked.connect(self.cancel_meeting)
                self.tableWidget.setCellWidget(rowcount, 3, self.cancel_btn) 

                rowcount += 1 

            else:
                em = emp_meet_data.get_employee_meeting(meeting.id, self.user.id)              
                if em.pending == False:
                    num_meetings -= 1
                    self.tableWidget.setRowCount(num_meetings)
               
                else:
                    self.employee_meetings.append(em)
                    item = QtWidgets.QTableWidgetItem(title)
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(rowcount, 0, item)

                    owner = employee_data.get_employee(owner)
                    name = "{} ({} {})".format(
                        owner.username,
                        owner.first_name,
                        owner.last_name
                        )
                    item = QtWidgets.QTableWidgetItem(name)
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(rowcount, 1, item)

                    t =  self.show_time(sorted(times))
                    d = date.strftime('%m/%d/%y')
                    dt = "{}, {}".format(d,t)
                    item = QtWidgets.QTableWidgetItem(dt)
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(rowcount, 2, item)

                    self.accept_btn = QtWidgets.QPushButton("Accept/Decline")
                    self.accept_btn.clicked.connect(self.accept_decline)
                    self.tableWidget.setCellWidget(rowcount, 3, self.accept_btn)

                    rowcount += 1
        print (self.employee_meetings)

    def translate_timeslot(self, ts):
        if isinstance(ts.begin_time, str):
            time = _translate_slot_backward_key(ts.begin_time)
        else:
            time = _translate_slot_backward(ts.begin_time.value)
        return time

    def accept_decline(self):
        print("accept_decline")
        button = self.sender()
        index = self.tableWidget.indexAt(button.pos())
        self.accept_meeting = AcceptMeeting(self.employee_meetings[index.row()], self)
        self.accept_meeting.show()

    def cancel_meeting(self):
        print("accept_decline")
        button = self.sender()
        index = self.tableWidget.indexAt(button.pos())
        self.accept_meeting = CancelMeeting(self.employee_meetings[index.row()], self)
        self.accept_meeting.show()

    def show_time(self, times):
        print(times)
        print(times[0])
        print(times[-1])
        start = self._translate_slot_forward(times[0])
        end = self._translate_slot_forward(times[-1] + 1)
        return "{} - {}".format(start, end)

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
            15: "4:30 pm",
            16: "5:00 pm"
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

class CancelMeeting(QtWidgets.QDialog):
    def __init__(self, meeting, parent=None):
        super(CancelMeeting, self).__init__(parent)
        self.meeting = meeting
        self.setObjectName("Cancel Metting")
        self.resize(357, 196)
        self.setSizeGripEnabled(False)
        self.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(20, 150, 321, 32))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        # self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setText("Accept")
        # self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).setText("Decline")
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(70, 50, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("Cancel Meeting?")   


        self.buttonBox.accepted.connect(self.cancel)
        self.buttonBox.rejected.connect(self.keep)

    def cancel(self):
        print("cancel")
        print(self.meeting)
        tmp = self.meeting.id
        meeting_data.delete_meeting(self.meeting)
        self.parent().populate_meetings()
        self.close()


    def keep(self):
        print("keep")
        self.close()

class AcceptMeeting(QtWidgets.QDialog):
    def __init__(self, employee_meeting, parent=None):
        super(AcceptMeeting, self).__init__(parent)
        self.employee_meeting = employee_meeting
        self.setObjectName("Accept Metting")
        self.resize(357, 196)
        self.setSizeGripEnabled(False)
        self.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(20, 150, 321, 32))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setText("Accept")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).setText("Decline")
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(70, 50, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("Accept or Decline?")   


        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.decline)


    def accept(self):
        print("accept")
        print (self.employee_meeting.pending)
        m = self.employee_meeting.meeting_id 
        e = self.employee_meeting.employee_id
        emp_meet_data.accept_meeting(self.employee_meeting)
        em = emp_meet_data.get_employee_meeting(m, e)
        print(em.accepted)
        print(em.pending)
        self.parent().populate_meetings()
        self.close()

    def decline(self):
        print("decline")
        print (self.employee_meeting.pending)

        m = self.employee_meeting.meeting_id 
        e = self.employee_meeting.employee_id
        emp_meet_data.decline_meeting(self.employee_meeting)
        #em = emp_meet_data.get_employee_meeting(m, e)
        #print(em.accepted)
        #print(em.pending)
        self.parent().populate_meetings()
        self.close()









