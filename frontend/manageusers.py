# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manageusers.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from backend.utils import EmployeeData
import secrets
import string

employee_data = EmployeeData()

class Ui_ManageUsers(object):
    def setupUi(self, ManageUsers):
        ManageUsers.setObjectName("ManageUsers")
        ManageUsers.resize(581, 391)
        ManageUsers.setGeometry(QtCore.QRect(230, 30, 581, 391))

        self.tableWidget = QtWidgets.QTableWidget(ManageUsers)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 541, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(134)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        header = self.tableWidget.horizontalHeader()       
        

        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)


        self.add_user_button = QtWidgets.QPushButton(ManageUsers)
        self.add_user_button.setGeometry(QtCore.QRect(450, 320, 113, 32))
        self.add_user_button.setObjectName("add_user_button")

        self.retranslateUi(ManageUsers)
        QtCore.QMetaObject.connectSlotsByName(ManageUsers)

    def retranslateUi(self, ManageUsers):
        _translate = QtCore.QCoreApplication.translate
        ManageUsers.setWindowTitle(_translate("ManageUsers", "Manage Users"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ManageUsers", "Username"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ManageUsers", "Password"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ManageUsers", "Generate Password"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ManageUsers", "Delete User"))
        self.add_user_button.setText(_translate("ManageUsers", "Add User"))

# Form implementation generated from reading ui file 'adduser.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

class AddUser(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AddUser, self).__init__(parent)
        self.setObjectName("AddUser")
        self.resize(357, 196)
        self.setSizeGripEnabled(False)
        self.setModal(True)
        #self.setGeometry(QtCore.QRect(230, 30, 581, 391))
        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 30, 300, 101))
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
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(20, 150, 321, 32))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")

        self.username_label.setText("Username")
        self.password_label.setText("Password")
        self.generate_password_button.setText("Generate Password")
        self.generated_password_label.setText("Generated Password")

        self.buttonBox.accepted.connect(self.save_user)
        self.buttonBox.rejected.connect(self.cancel)
        self.generate_password_button.clicked.connect(self.generate_password)

    def save_user(self):
        print("save_user")
        username = self.username_input.text()
        password = self.generated_password_input.text()
        if username in (None, ""):
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Username is required')            
        if password in (None, ""):
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Password is required') 

        if username and password:
            if self._check_username(username):
                employee = employee_data.add_employee(username, password)           

                print(password)
                self.parent().delete_user_list()
                self.parent().populate_user_list()
                self.close()
            else:
                QtWidgets.QMessageBox.warning(
                    self, 'Error', 'Username already exists')                

    def _check_username(self, username):
        return employee_data.check_employee_exists(username)

    def cancel(self):
        print("cancel")
        self.close()

    def generate_password(self):
        print("generate_password")
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        print(password)
        self.generated_password_input.setText(password)
        '''
        self.employee.password = password
        employee = employee_data.update_employee_by_obj(self.employee)
        if employee:
            self.parent().delete_user_list()
            self.parent().populate_user_list()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Integrity Error')

        '''

class ManageUsers(QtWidgets.QFrame, Ui_ManageUsers):
    def __init__(self, user, parent=None):
        super(ManageUsers, self).__init__(parent)
        self.setupUi(self)  
        self.user = user
        self.populate_user_list()
        self.add_user_button.clicked.connect(lambda: self.showAddUser(parent))


    def showAddUser(self, parent):
        self.add_user = AddUser(self)
        self.add_user.show() 

    def populate_user_list(self):
        self.employees = employee_data.get_all_employees()

        for employee in self.employees:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(employee.username))
            self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(employee.password))
            self.btn = QtWidgets.QPushButton("Generate Password")
            self.btn.clicked.connect(self.showGeneratePassword)
            self.tableWidget.setCellWidget(rowPosition, 2, self.btn)

            print(employee)
            print(self.user)
            if employee != self.user:
                self.delete_btn = QtWidgets.QPushButton("Delete")
                self.delete_btn.clicked.connect(self.showDeleteUser)
                self.tableWidget.setCellWidget(rowPosition, 3, self.delete_btn)


    def delete_user_list(self):
        for i in reversed(range(self.tableWidget.rowCount())):
            self.tableWidget.removeRow(i)

    def showGeneratePassword(self):
        print("showGeneratePassword")
        button = self.sender()
        index = self.tableWidget.indexAt(button.pos())
        self.generate_password = GeneratePassword(self.employees[index.row()], self)
        self.generate_password.show()

    def showDeleteUser(self):
        print("showDeleteRoom")
        button = self.sender()
        index = self.tableWidget.indexAt(button.pos()) 
        self.delete_user = DeleteUser(self.employees[index.row()], self)
        self.delete_user.show()

class DeleteUser(QtWidgets.QDialog):
    def __init__(self, employee, parent=None):
        super(DeleteUser, self).__init__(parent)  
        self.employee = employee 
 


        self.setObjectName("Dialog")
        self.resize(375, 185)
        self.setSizeGripEnabled(False)
        self.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(10, 120, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Yes|QtWidgets.QDialogButtonBox.No)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(90, 50, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.buttonBox.accepted.connect(self.delete_user)
        self.buttonBox.rejected.connect(self.cancel)
        self.label.setText("Delete this employee?")

    def delete_user(self):
        print("delete_room")
        employee_data.delete_employee_obj(self.employee)
        self.parent().delete_user_list()
        self.parent().populate_user_list()
        self.close()

    def cancel(self):
        self.close()      

class GeneratePassword(QtWidgets.QDialog):
    def __init__(self, employee, parent=None):
        super(GeneratePassword, self).__init__(parent)
        self.employee = employee
        self.setObjectName("Dialog")
        self.resize(375, 185)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(10, 120, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(90, 50, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.buttonBox.accepted.connect(self.generate)
        self.buttonBox.rejected.connect(self.cancel)

        self.setWindowTitle("Dialog")
        self.label.setText("Generate new password?")

    def generate(self):
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        self.employee.password = password
        employee = employee_data.update_employee_by_obj(self.employee)
        if employee:
            self.parent().delete_user_list()
            self.parent().populate_user_list()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Integrity Error')            


    def cancel(self):
        print("cancel")
        self.close()


