# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewprofile.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import re

from backend.utils import EmployeeData
employee_data = EmployeeData()


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
        self.user = user
        self.setupUi(self) 
        self.save_button.clicked.connect(self.save)
        self.change_password_button.clicked.connect(self.change_password)
        
        self.employee_id_input.setText(str(self.user.id))
        self.usename_input.setText(self.user.username)
        self.first_name_input.setText(self.user.first_name)
        self.last_name_input.setText(self.user.last_name)
        self.email_input.setText(self.user.email)
        self.telephone_input.setText(self.user.telephone)

    def save(self):
        self._check_email()
        self._check_telephone()
        self.user = employee_data.update_employee(
            self.user.id,
            {
                'first_name': self.first_name_input.text(),
                'last_name': self.last_name_input.text(),
                'email': self.email_input.text(),
                'telephone': self.telephone_input.text()
            }
            )

    def change_password(self):
        self.password = ChangePassword(self.user, self)
        self.password.show()


    def _check_email(self):
        pattern = re.compile('[^@]+@[^@]+\.[^@]+')
        if pattern.match(self.email_input.text()) is None and self.email_input.text() != "":
            QtWidgets.QMessageBox.warning(
                    self, 'Error', 'Email must be in format: [str]@[str].[str]')    


    def _check_telephone(self):
        pattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
        if pattern.match(self.telephone_input.text()) is None and self.telephone_input.text() != "":
            QtWidgets.QMessageBox.warning(
                    self, 'Error', 'Telephone must be in format: XXX-XXX-XXXX')    

class Ui_ChangePassword(object):
    def setupUi(self, ChangePassword):
        ChangePassword.setObjectName("ChangePassword")
        ChangePassword.resize(350, 250)


        self.formLayoutWidget = QtWidgets.QWidget(ChangePassword)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 80, 311, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.password_lineedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.password_lineedit.setObjectName("password_lineedit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.password_lineedit)
        self.password_lineedit2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.password_lineedit2.setObjectName("password_lineedit2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.password_lineedit2)

        self.change_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.change_button.setObjectName("Add_button")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.change_button)
        self.label = QtWidgets.QLabel(ChangePassword)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 31))
        self.label.setObjectName("label")

        self.retranslateUi(ChangePassword)
        QtCore.QMetaObject.connectSlotsByName(ChangePassword)

    def retranslateUi(self, ChangePassword):
        _translate = QtCore.QCoreApplication.translate
        ChangePassword.setWindowTitle(_translate("ChangePassword", ""))
        self.change_button.setText(_translate("ChangePassword", "Change"))
        self.label.setText(_translate("ChangePassword", "Enter new password (twice)"))

class ChangePassword(QtWidgets.QDialog, Ui_ChangePassword):
    def __init__(self, user, parent=None):
        super(ChangePassword, self).__init__(parent) 
        self.user = user 
        self.setupUi(self)
        self.change_button.clicked.connect(self.change)


    def change(self):
        self.changed_password1 = self.password_lineedit.text()
        self.changed_password2 = self.password_lineedit2.text()
        if self.changed_password1 == "" or self.changed_password2 == "":
            QtWidgets.QMessageBox.warning(
                    self, 'Error', 'Passwords cannot be blank')    

        elif not self.changed_password1 == self.changed_password2:
            QtWidgets.QMessageBox.warning(
                    self, 'Error', 'Passwords not equal')    
        else:
            self.user = employee_data.update_employee(
                self.user.id,
                {
                    'password': self.changed_password1,
                }
                ) 
            QtWidgets.QMessageBox.warning(self, 'Warning', 'Password changed')  
            self.close()    

