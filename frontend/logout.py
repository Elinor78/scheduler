# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logout.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Logout(object):
    def setupUi(self, Logout):
        Logout.setObjectName("Logout")
        Logout.resize(357, 196)
        Logout.setSizeGripEnabled(False)
        Logout.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(Logout)
        self.buttonBox.setGeometry(QtCore.QRect(20, 130, 321, 32))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Logout)
        self.label.setGeometry(QtCore.QRect(70, 50, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Logout)
        QtCore.QMetaObject.connectSlotsByName(Logout)

    def retranslateUi(self, Logout):
        _translate = QtCore.QCoreApplication.translate
        Logout.setWindowTitle(_translate("Logout", "Dialog"))
        self.label.setText(_translate("Logout", "Are you sure you want to log out?"))

class Logout(QtWidgets.QDialog, Ui_Logout):
    def __init__(self, user, parent=None):
        super(Logout, self).__init__(parent)
        self.setupUi(self) 
        self.buttonBox.accepted.connect(self.logout)
        self.buttonBox.rejected.connect(self.remain)

    def logout(self):
        self.parent().close()

    def remain(self):
        self.close()
