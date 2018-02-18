# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forgotpassword.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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

