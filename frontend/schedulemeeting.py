# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'schedulemeeting.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from custom_widgets import ScheduleTableWidget

class Ui_schedulemeeting(object):
    def setupUi(self, schedulemeeting):
        schedulemeeting.setObjectName("schedulemeeting")
        schedulemeeting.resize(581, 391)
        schedulemeeting.setGeometry(QtCore.QRect(230, 30, 581, 391))

        self.formLayoutWidget = QtWidgets.QWidget(schedulemeeting)
        self.formLayoutWidget.setGeometry(QtCore.QRect(5, 10, 571, 301))
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
        self.timeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.timeLabel.setObjectName("timeLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.timeLabel)
        self.timeComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.timeComboBox.setObjectName("timeComboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.timeComboBox)
        self.durationLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.durationLabel.setObjectName("durationLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.durationLabel)
        self.durationComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.durationComboBox.setObjectName("durationComboBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.durationComboBox)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.textEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.tableWidget = ScheduleTableWidget(self.formLayoutWidget)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(17)
        self.tableWidget.setRowCount(2)
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
        self.pushButton = QtWidgets.QPushButton(schedulemeeting)
        self.pushButton.setGeometry(QtCore.QRect(480, 330, 81, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(schedulemeeting)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 330, 131, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(schedulemeeting)
        QtCore.QMetaObject.connectSlotsByName(schedulemeeting)

    def retranslateUi(self, schedulemeeting):
        _translate = QtCore.QCoreApplication.translate
        schedulemeeting.setWindowTitle(_translate("schedulemeeting", "Schedule Meeting"))
        self.titleLabel.setText(_translate("schedulemeeting", "Title"))
        self.dateLabel.setText(_translate("schedulemeeting", "Date"))
        self.dateDateEdit.setDisplayFormat(_translate("schedulemeeting", "MMMM dd, yyyy"))
        self.timeLabel.setText(_translate("schedulemeeting", "Time"))
        self.durationLabel.setText(_translate("schedulemeeting", "Duration"))
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
        self.pushButton.setText(_translate("schedulemeeting", "Save"))
        self.pushButton_2.setText(_translate("schedulemeeting", "Add Participant"))


class ScheduleMeeting(QtWidgets.QFrame, Ui_schedulemeeting):
    def __init__(self, user, parent=None):
        super(ScheduleMeeting, self).__init__(parent)
        self.setupUi(self) 
        

    def add_participant(self):
        pass
        #TODO search box for finding participant
            #if click on one and OK, then call self.tableWidget.add_participant 
            # with user info
            # if click cancel, pass, basically


    def save_meeting(self):
        pass
        #TODO - whole bunch





        