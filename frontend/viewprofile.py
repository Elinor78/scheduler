# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewprofile.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewProfile(object):
    def setupUi(self, ViewProfile):
        ViewProfile.setObjectName("ViewProfile")
        ViewProfile.resize(581, 391)
        ViewProfile.setGeometry(QtCore.QRect(230, 30, 581, 391))

        self.formLayoutWidget = QtWidgets.QWidget(ViewProfile)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 40, 471, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.employee_formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.employee_formLayout.setContentsMargins(0, 0, 0, 0)
        self.employee_formLayout.setObjectName("employee_formLayout")
        self.first_name_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.first_name_label.setObjectName("first_name_label")
        self.employee_formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.first_name_label)
        self.first_name_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.first_name_input.setObjectName("first_name_input")
        self.employee_formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.first_name_input)
        self.last_name_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.last_name_label.setObjectName("last_name_label")
        self.employee_formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.last_name_label)
        self.last_name_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.last_name_input.setObjectName("last_name_input")
        self.employee_formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.last_name_input)
        self.email_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.email_label.setObjectName("email_label")
        self.employee_formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.email_label)
        self.email_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.email_input.setObjectName("email_input")
        self.employee_formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.email_input)
        self.telephone_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.telephone_label.setObjectName("telephone_label")
        self.employee_formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.telephone_label)
        self.telephone_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.telephone_input.setObjectName("telephone_input")
        self.employee_formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.telephone_input)
        self.employee_id_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.employee_id_label.setObjectName("employee_id_label")
        self.employee_formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.employee_id_label)
        self.employee_id_input = QtWidgets.QLabel(self.formLayoutWidget)
        self.employee_id_input.setText("")
        self.employee_id_input.setObjectName("employee_id_input")
        self.employee_formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.employee_id_input)
        self.usernam_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.usernam_label.setObjectName("usernam_label")
        self.employee_formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.usernam_label)
        self.usename_input = QtWidgets.QLabel(self.formLayoutWidget)
        self.usename_input.setText("")
        self.usename_input.setObjectName("usename_input")
        self.employee_formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.usename_input)
        self.change_password_button = QtWidgets.QPushButton(ViewProfile)
        self.change_password_button.setGeometry(QtCore.QRect(260, 230, 131, 32))
        self.change_password_button.setObjectName("change_password_button")
        self.save_button = QtWidgets.QPushButton(ViewProfile)
        self.save_button.setGeometry(QtCore.QRect(400, 230, 113, 32))
        self.save_button.setObjectName("save_button")

        self.retranslateUi(ViewProfile)
        QtCore.QMetaObject.connectSlotsByName(ViewProfile)

    def retranslateUi(self, ViewProfile):
        _translate = QtCore.QCoreApplication.translate
        ViewProfile.setWindowTitle(_translate("ViewProfile", "Frame"))
        self.first_name_label.setText(_translate("ViewProfile", "First Name"))
        self.last_name_label.setText(_translate("ViewProfile", "Last Name"))
        self.email_label.setText(_translate("ViewProfile", "Email"))
        self.telephone_label.setText(_translate("ViewProfile", "Telephone"))
        self.employee_id_label.setText(_translate("ViewProfile", "Employee ID"))
        self.usernam_label.setText(_translate("ViewProfile", "Username"))
        self.change_password_button.setText(_translate("ViewProfile", "Change Password"))
        self.save_button.setText(_translate("ViewProfile", "Save"))

class ViewProfile(QtWidgets.QFrame, Ui_ViewProfile):   
    def __init__(self, user, parent=None):
        super(ViewProfile, self).__init__(parent)
        self.setupUi(self) 