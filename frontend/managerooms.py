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

class Ui_AddRoom(object):
    def setupUi(self, AddRoom):
        AddRoom.setObjectName("AddRoom")
        AddRoom.resize(581, 391)
        AddRoom.setGeometry(QtCore.QRect(230, 30, 581, 391))
        self.buttonBox = QtWidgets.QDialogButtonBox(AddRoom)
        self.buttonBox.setGeometry(QtCore.QRect(340, 160, 164, 31))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(AddRoom)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 39, 531, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.room_number_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.room_number_label.setObjectName("room_number_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.room_number_label)
        self.room_number_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.room_number_input.setObjectName("room_number_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.room_number_input)
        self.building_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.building_label.setObjectName("building_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.building_label)
        self.building_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.building_input.setObjectName("building_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.building_input)
        self.capacity_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.capacity_label.setObjectName("capacity_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.capacity_label)
        self.capacity_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.capacity_input.setObjectName("capacity_input")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.capacity_input)

        self.retranslateUi(AddRoom)
        QtCore.QMetaObject.connectSlotsByName(AddRoom)

    def retranslateUi(self, AddRoom):
        _translate = QtCore.QCoreApplication.translate
        AddRoom.setWindowTitle(_translate("AddRoom", "Frame"))
        self.room_number_label.setText(_translate("AddRoom", "Room Number"))
        self.building_label.setText(_translate("AddRoom", "Building"))
        self.capacity_label.setText(_translate("AddRoom", "Capacity"))

class AddRoom(QtWidgets.QFrame, Ui_AddRoom):
    def __init__(self, user, parent=None):
        super(AddRoom, self).__init__(parent)
        self.setupUi(self)     

class ManageRooms(QtWidgets.QFrame, Ui_ManageRooms):
    def __init__(self, user, parent=None):
        super(ManageRooms, self).__init__(parent)
        self.setupUi(self)
        self.user = user
        self.add_room_button.clicked.connect(lambda: self.showAddRoom(parent))


    def showAddRoom(self, parent):
        parent.frame.hide()
        parent.frame = AddRoom(self.user, parent)
        parent.frame.show()
