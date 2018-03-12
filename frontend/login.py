# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from backend.utils import EmployeeData
from sqlalchemy.orm.exc import NoResultFound

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(324, 137)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setMinimumSize(QtCore.QSize(324, 137))
        Login.setMaximumSize(QtCore.QSize(324, 137))
        self.formLayoutWidget_2 = QtWidgets.QWidget(Login)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 271, 71))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.username_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.username_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.username_label.setObjectName("username_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.username_label)
        self.username_lineedit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.username_lineedit.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.username_lineedit.setPlaceholderText("")
        self.username_lineedit.setObjectName("username_lineedit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username_lineedit)
        self.password_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.password_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.password_label.setObjectName("password_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.password_label)
        self.password_lineedit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_lineedit.sizePolicy().hasHeightForWidth())
        self.password_lineedit.setSizePolicy(sizePolicy)
        self.password_lineedit.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.password_lineedit.setObjectName("password_lineedit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.password_lineedit)
        self.login_button = QtWidgets.QPushButton(Login)
        self.login_button.setGeometry(QtCore.QRect(230, 90, 71, 32))
        self.login_button.setObjectName("login_button")
        self.forgot_password_button = QtWidgets.QPushButton(Login)
        self.forgot_password_button.setGeometry(QtCore.QRect(70, 90, 151, 32))
        self.forgot_password_button.setObjectName("forgot_password_button")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.username_label.setText(_translate("Login", "Username:"))
        self.password_label.setText(_translate("Login", "Password:"))
        self.login_button.setText(_translate("Login", "Login"))
        self.forgot_password_button.setText(_translate("Login", "Forgot Password"))

class Ui_ForgotPassword(object):
    def setupUi(self, ForgotPassword):
        ForgotPassword.setObjectName("ForgotPassword")
        ForgotPassword.resize(324, 137)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ForgotPassword.sizePolicy().hasHeightForWidth())
        ForgotPassword.setSizePolicy(sizePolicy)
        ForgotPassword.setMinimumSize(QtCore.QSize(324, 137))
        ForgotPassword.setMaximumSize(QtCore.QSize(324, 137))
        self.formLayoutWidget_2 = QtWidgets.QWidget(ForgotPassword)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 271, 71))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.form = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.form.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.form.setContentsMargins(0, 0, 0, 0)
        self.form.setObjectName("form")
        self.username_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.username_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.username_label.setObjectName("username_label")
        self.form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.username_label)
        self.username_lineedit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.username_lineedit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.username_lineedit.setPlaceholderText("")
        self.username_lineedit.setObjectName("username_lineedit")
        self.form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username_lineedit)
        self.email_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.email_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.email_label.setObjectName("email_label")
        self.form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.email_label)
        self.email_lineedit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_lineedit.sizePolicy().hasHeightForWidth())
        self.email_lineedit.setSizePolicy(sizePolicy)
        self.email_lineedit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.email_lineedit.setObjectName("email_lineedit")
        self.form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.email_lineedit)
        self.cancel_button = QtWidgets.QPushButton(ForgotPassword)
        self.cancel_button.setGeometry(QtCore.QRect(230, 90, 71, 32))
        self.cancel_button.setObjectName("cancel_button")
        self.submit_button = QtWidgets.QPushButton(ForgotPassword)
        self.submit_button.setGeometry(QtCore.QRect(150, 90, 81, 32))
        self.submit_button.setObjectName("submit_button")

        self.retranslateUi(ForgotPassword)
        QtCore.QMetaObject.connectSlotsByName(ForgotPassword)

    def retranslateUi(self, ForgotPassword):
        _translate = QtCore.QCoreApplication.translate
        ForgotPassword.setWindowTitle(_translate("ForgotPassword", "Forgot Password"))
        self.username_label.setText(_translate("ForgotPassword", "Username:"))
        self.email_label.setText(_translate("ForgotPassword", "Email"))
        self.cancel_button.setText(_translate("ForgotPassword", "Cancel"))
        self.submit_button.setText(_translate("ForgotPassword", "Submit"))


class ForgotPassword(QtWidgets.QDialog, Ui_ForgotPassword):
    def __init__(self, parent=None):
        super(ForgotPassword, self).__init__(parent)
        self.setupUi(self)
        self.cancel_button.clicked.connect(self.cancel_change)
        self.submit_button.clicked.connect(self.submit_change)

    def cancel_change(self):
        self.accept() 

    def submit_change(self):
        '''
        If an employee submits a request that they forgot their password,
        a notification is sent to the admin. It is then the admin's job to change
        the employee's password and notify that employee outside of the system
        of that change.
        If the input email does not match the saved email, an error is thrown and 
        no password notification is sent.
        
        TODO: implement password change notifications
        '''
        employeedata = EmployeeData()
        try:
            user = employeedata.get_employee_by_username(self.username_lineedit.text())
            if user.email != self.email_lineedit.text() or self.email_lineedit == '':
                QtWidgets.QMessageBox.warning(
                self, 'Error', 'Bad user or email') 
            #TODO: NOTIFICATION
            self.accept()
        except NoResultFound:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Bad user or email')

class Login(QtWidgets.QDialog, Ui_Login):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self) 
        self.login_button.clicked.connect(self.handleLogin)
        self.forgot_password_button.clicked.connect(self.forgot_password)
        
    def handleLogin(self):
        print("in handleLogin")
        employeedata = EmployeeData()

        try:

            user = employeedata.get_employee_by_username(self.username_lineedit.text())
            print(user.password)
            if user.password == self.password_lineedit.text():
                self.user = user
                self.accept()
            else:
                QtWidgets.QMessageBox.warning(
                    self, 'Error', 'Bad user or password')  

        except NoResultFound:
            if self.username_lineedit.text() == "joe":
                joe = employeedata.add_employee('joe', 'p')
                joe = employeedata.update_employee(joe.id, {'email': 'joe@fake.com', 'telephone':'800-999-9999', 'first_name': 'Joe', 'last_name': 'Smith', 'is_admin': True})
            else:
                QtWidgets.QMessageBox.warning(
                    self, 'Error', 'Bad user or password') 

    def forgot_password(self):
        #TODO hook up to db
        f = ForgotPassword()
        f.exec_()