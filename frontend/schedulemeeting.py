# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'schedulemeeting.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from custom_widgets import ScheduleTableWidget
import datetime
from backend.utils import EmployeeData, RoomData


class Ui_schedulemeeting(object):
    def setupUi(self, schedulemeeting):
        schedulemeeting.setObjectName("schedulemeeting")
        schedulemeeting.resize(581, 391)
        schedulemeeting.setGeometry(QtCore.QRect(230, 30, 581, 391))

        self.formLayoutWidget = QtWidgets.QWidget(schedulemeeting)
        self.formLayoutWidget.setGeometry(QtCore.QRect(5, 10, 571, 350))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.titleLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.titleLabel.setObjectName("titleLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.titleLabel)
        self.titleLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.titleLineEdit)
        self.dateLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.dateLabel.setObjectName("dateLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.dateLabel)
        self.dateDateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dateDateEdit.setMinimumDate(QtCore.QDate(2018, 3, 1))
        self.dateDateEdit.setCalendarPopup(True)
        self.dateDateEdit.setObjectName("dateDateEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dateDateEdit)
        #self.timeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        #self.timeLabel.setObjectName("timeLabel")
        #self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.timeLabel)
        #self.timeComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        #self.timeComboBox.setObjectName("timeComboBox")
        #self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.timeComboBox)
        #self.durationLabel = QtWidgets.QLabel(self.formLayoutWidget)
        #self.durationLabel.setObjectName("durationLabel")
        #self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.durationLabel)
        #self.durationComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        #self.durationComboBox.setObjectName("durationComboBox")
        #self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.durationComboBox)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.textEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.tableWidget = ScheduleTableWidget(self.user, self.formLayoutWidget)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(17)
        self.tableWidget.setRowCount(2)
        #schedulemeeting.setGeometry(QtCore.QRect(230, 30, 581, 391))
        #self.tableWidget.setGeometry(QtCore.QRect(340, 50, 100, 100))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 1, item)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.tableWidget)
        self.save_button = QtWidgets.QPushButton(schedulemeeting)
        self.save_button.setGeometry(QtCore.QRect(480, 330, 81, 32))
        self.save_button.setObjectName("save_button")
        self.add_participant_button = QtWidgets.QPushButton(schedulemeeting)
        self.add_participant_button.setGeometry(QtCore.QRect(350, 330, 131, 32))
        self.add_participant_button.setObjectName("add_participant_button")
        self.add_room_button = QtWidgets.QPushButton(schedulemeeting)
        self.add_room_button.setGeometry(QtCore.QRect(250, 330, 100, 32))
        self.add_room_button.setObjectName("add_room_button")

        self.retranslateUi(schedulemeeting)
        QtCore.QMetaObject.connectSlotsByName(schedulemeeting)

    def retranslateUi(self, schedulemeeting):
        _translate = QtCore.QCoreApplication.translate
        schedulemeeting.setWindowTitle(_translate("schedulemeeting", "Schedule Meeting"))
        self.titleLabel.setText(_translate("schedulemeeting", "Title"))
        self.dateLabel.setText(_translate("schedulemeeting", "Date"))
        self.dateDateEdit.setDisplayFormat(_translate("schedulemeeting", "MMMM dd, yyyy"))
        #self.timeLabel.setText(_translate("schedulemeeting", "Time"))
        #self.durationLabel.setText(_translate("schedulemeeting", "Duration"))
        self.label.setText(_translate("schedulemeeting", "Description"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("schedulemeeting", "Owner"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("schedulemeeting", "Participants"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("schedulemeeting", "9:00 am"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("schedulemeeting", "9:30 am"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("schedulemeeting", "10:00 am"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("schedulemeeting", "10:30 am"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("schedulemeeting", "11:00 am"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("schedulemeeting", "11:30 am"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("schedulemeeting", "12:00 pm"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("schedulemeeting", "12:30 pm"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("schedulemeeting", "1:00 pm"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("schedulemeeting", "1:30 pm"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("schedulemeeting", "2:00 pm"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("schedulemeeting", "2:30 pm"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("schedulemeeting", "3:00 pm"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("schedulemeeting", "3:30 pm"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("schedulemeeting", "4:00 pm"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("schedulemeeting", "4:30 pm"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.save_button.setText(_translate("schedulemeeting", "Save"))
        self.add_participant_button.setText(_translate("schedulemeeting", "Add Participant"))
        self.add_room_button.setText(_translate("schedulemeeting", "Add Room"))


class ScheduleMeeting(QtWidgets.QFrame, Ui_schedulemeeting):
    def __init__(self, user, parent=None):
        super(ScheduleMeeting, self).__init__(parent)
        self.user = user
        self.setupUi(self) 
        self.add_participant_button.clicked.connect(self._add_participant)
        self.add_room_button.clicked.connect(self._add_room)
        self.save_button.clicked.connect(self.save_meeting)
        self.to_add_participant = None

    def _add_room(self):
        self.room_search = SearchRoom(self)
        self.room_search.show()

    def add_room(self, roomname):
        self.tableWidget.add_room(roomname)

    def _add_participant(self):
        #TODO search box for finding participant
            #if click on one and OK, then call self.tableWidget.add_participant 
            # with user info
            # if click cancel, pass, basically

        #print("here")
        self.search = SearchParticipant(self)
        self.search.show()

        #print("here 2")
        #print(self.search.to_add_participant)

    def add_participant(self, username):
        #print ("here 3")

        #print(self.tableWidget)
        self.tableWidget.add_participant(username)

    def save_meeting(self):
        #TODO - whole bunch
        print("A")
        self._check_date()
        self._check_title()

        print(self.tableWidget.participants)
        print("B")

    def _check_date(self):
        print(type(self.dateDateEdit.text()))
        #print(datetime.date(self.dateDateEdit.text()))
        _date = datetime.datetime.strptime(self.dateDateEdit.text(), '%B %d, %Y').date()
        margin = datetime.timedelta(days=14)
        today = datetime.date.today()
        print (_date.weekday())
        #weekday is less than 5
        if _date.weekday() >= 5:#saturday and sunday
            QtWidgets.QMessageBox.warning(
                    self, 'Error', 'Cannot schedule meetings on weekends')
        if today < _date < today + margin:
            pass
        else:
            QtWidgets.QMessageBox.warning(
                    self, 'Error', 'Meetings must be scheduled within 14 days of today')    

    def _check_title(self):
        if self.titleLineEdit.text() == "":
            QtWidgets.QMessageBox.warning(
                self, 'Error', "Must include meeting title")
        print(self.titleLineEdit.text())    



class Ui_SearchParticipant(object):
    def setupUi(self, SearchParticipant):
        SearchParticipant.setObjectName("SearchParticipant")
        SearchParticipant.resize(350, 112)


        self.formLayoutWidget = QtWidgets.QWidget(SearchParticipant)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 60, 311, 41))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.search_lineedit = EmployeeSearchWidget(self.formLayoutWidget)
        self.search_lineedit.setObjectName("search_lineedit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.search_lineedit)
        self.Add_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.Add_button.setObjectName("Add_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Add_button)
        self.label = QtWidgets.QLabel(SearchParticipant)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 31))
        self.label.setObjectName("label")

        self.retranslateUi(SearchParticipant)
        QtCore.QMetaObject.connectSlotsByName(SearchParticipant)

    def retranslateUi(self, SearchParticipant):
        _translate = QtCore.QCoreApplication.translate
        SearchParticipant.setWindowTitle(_translate("SearchParticipant", "Form"))
        self.Add_button.setText(_translate("SearchParticipant", "Add"))
        self.label.setText(_translate("SearchParticipant", "Search for participant"))

class SearchParticipant(QtWidgets.QDialog, Ui_SearchParticipant):
    def __init__(self, parent=None):
        super(SearchParticipant, self).__init__(parent)  
        self.setupUi(self) 
        self.to_add_participant = None
        self.Add_button.clicked.connect(self.add)

    def add(self):
        self.to_add_participant = self.search_lineedit.text()
        print(self.to_add_participant)
        print(self.parent())
        self.parent().add_participant(self.to_add_participant)
        self.close()


class EmployeeSearchWidget(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(EmployeeSearchWidget, self).__init__(parent)
        #self.edit = QtWidgets.QLineEdit()
        completer = QtWidgets.QCompleter()
        self.setCompleter(completer)



        model = QtCore.QStringListModel()
        completer.setModel(model)
        model.setStringList(self.get_employees())

    def get_employees(self):
        employeedata = EmployeeData()
        return [e.username for e in employeedata.get_all_employees()]


class Ui_SearchRoom(object):
    def setupUi(self, SearchRoom):
        SearchRoom.setObjectName("SearchRoom")
        SearchRoom.resize(350, 112)


        self.formLayoutWidget = QtWidgets.QWidget(SearchRoom)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 60, 311, 41))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.search_lineedit = RoomSearchWidget(self.formLayoutWidget)
        self.search_lineedit.setObjectName("search_lineedit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.search_lineedit)
        self.Add_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.Add_button.setObjectName("Add_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Add_button)
        self.label = QtWidgets.QLabel(SearchRoom)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 31))
        self.label.setObjectName("label")

        self.retranslateUi(SearchRoom)
        QtCore.QMetaObject.connectSlotsByName(SearchRoom)

    def retranslateUi(self, SearchRoom):
        _translate = QtCore.QCoreApplication.translate
        SearchRoom.setWindowTitle(_translate("SearchRoom", "Form"))
        self.Add_button.setText(_translate("SearchRoom", "Add"))
        self.label.setText(_translate("SearchRoom", "Search for room"))

class SearchRoom(QtWidgets.QDialog, Ui_SearchRoom):
    def __init__(self, parent=None):
        super(SearchRoom, self).__init__(parent)  
        self.setupUi(self) 
        self.to_add_room = None
        self.Add_button.clicked.connect(self.add)

    def add(self):
        self.to_add_room = self.search_lineedit.text()
        self.parent().add_room(self.to_add_room)
        self.close()

class RoomSearchWidget(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(RoomSearchWidget, self).__init__(parent)
        completer = QtWidgets.QCompleter()
        self.setCompleter(completer)
        model = QtCore.QStringListModel()
        completer.setModel(model)
        model.setStringList(self.get_rooms())

    def get_rooms(self):
        roomdata = RoomData()
        return [e.roomname for e in roomdata.get_all_rooms()]


        
