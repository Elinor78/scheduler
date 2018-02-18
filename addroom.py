# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addroom.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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

