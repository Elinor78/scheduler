# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adduser.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddUser(object):
    def setupUi(self, AddUser):
        AddUser.setObjectName("AddUser")
        AddUser.resize(581, 391)
        AddUser.setGeometry(QtCore.QRect(230, 30, 581, 391))
        self.formLayoutWidget = QtWidgets.QWidget(AddUser)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 40, 501, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.username_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.username_label.setObjectName("username_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.username_label)
        self.username_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.username_input.setObjectName("username_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username_input)
        self.password_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.password_label.setObjectName("password_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.password_label)
        self.generate_password_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.generate_password_button.setObjectName("generate_password_button")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.generate_password_button)
        self.generated_password_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.generated_password_label.setObjectName("generated_password_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.generated_password_label)
        self.generated_password_input = QtWidgets.QLabel(self.formLayoutWidget)
        self.generated_password_input.setText("")
        self.generated_password_input.setObjectName("generated_password_input")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.generated_password_input)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddUser)
        self.buttonBox.setGeometry(QtCore.QRect(370, 160, 164, 32))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(AddUser)
        QtCore.QMetaObject.connectSlotsByName(AddUser)

    def retranslateUi(self, AddUser):
        _translate = QtCore.QCoreApplication.translate
        AddUser.setWindowTitle(_translate("AddUser", "Add User"))
        self.username_label.setText(_translate("AddUser", "Username"))
        self.password_label.setText(_translate("AddUser", "Password"))
        self.generate_password_button.setText(_translate("AddUser", "Generate Password"))
        self.generated_password_label.setText(_translate("AddUser", "Generated Password"))

