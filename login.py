# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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

