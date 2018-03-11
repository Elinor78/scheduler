# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'managerooms.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from backend.utils import RoomData

room_data = RoomData()

class Ui_ManageRooms(object):
    def setupUi(self, ManageRooms):
        ManageRooms.setObjectName("ManageRooms")
        ManageRooms.resize(581, 391)
        ManageRooms.setGeometry(QtCore.QRect(230, 30, 581, 391))
        
        self.tableWidget = QtWidgets.QTableWidget(ManageRooms)
        self.tableWidget.setGeometry(QtCore.QRect(15, 11, 551, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        
        self.tableWidget.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        self.add_room_button = QtWidgets.QPushButton(ManageRooms)
        self.add_room_button.setGeometry(QtCore.QRect(430, 340, 113, 32))
        self.add_room_button.setObjectName("add_room_button")

        self.retranslateUi(ManageRooms)
        QtCore.QMetaObject.connectSlotsByName(ManageRooms)

    def retranslateUi(self, ManageRooms):
        _translate = QtCore.QCoreApplication.translate
        ManageRooms.setWindowTitle(_translate("ManageRooms", "Manage Rooms"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ManageRooms", "Room Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ManageRooms", "Room Number"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ManageRooms", "Building"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ManageRooms", "Capacity"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ManageRooms", "Edit"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ManageRooms", "Delete"))
        self.add_room_button.setText(_translate("ManageRooms", "Add Room"))




class ManageRooms(QtWidgets.QFrame, Ui_ManageRooms):
    def __init__(self, user, parent=None):
        super(ManageRooms, self).__init__(parent)
        self.setupUi(self)
        self.user = user
        self.populate_room_list()
        self.add_room_button.clicked.connect(lambda: self.showAddRoom(parent))


    def showAddRoom(self, parent):
        self.add_room = AddRoom(self)
        self.add_room.show()

    def populate_room_list(self):
        self.rooms = room_data.get_all_rooms()
        
        for room in self.rooms:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(room.roomname))
            self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(room.number)))
            self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(room.building)))
            self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(room.capacity)))
            self.btn = QtWidgets.QPushButton("Edit")
            self.btn.clicked.connect(self.showEditRoom)
            self.tableWidget.setCellWidget(rowPosition, 4, self.btn)

            self.delete_btn = QtWidgets.QPushButton("Delete")
            self.delete_btn.clicked.connect(self.showDeleteRoom)
            self.tableWidget.setCellWidget(rowPosition, 5, self.delete_btn)

    def delete_room_list(self):
        for i in reversed(range(self.tableWidget.rowCount())):
            self.tableWidget.removeRow(i)



    def showEditRoom(self):
        print("showEditRoom")
        button = self.sender()
        index = self.tableWidget.indexAt(button.pos())
        print(index)
        print(index.row())
        print (index.column())
        #print(self.rooms[index.row()].id)

        self.edit_room = EditRoom(self.rooms[index.row()], self)
        self.edit_room.show()

    def showDeleteRoom(self):
        button = self.sender()
        index = self.tableWidget.indexAt(button.pos())
        print(index.row())
        print(index.column())

        self.delete_room = DeleteRoom(self.rooms[index.row()], self)
        self.delete_room.show()

class AddRoom(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AddRoom, self).__init__(parent)
        self.setObjectName("Add Room")
        self.resize(357, 196)
        self.setSizeGripEnabled(False)
        self.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(20, 150, 321, 32))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(70, 50, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 39, 300, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.room_name_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.room_name_label.setObjectName("room_name_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.room_name_label)

        self.room_name_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.room_name_input.setObjectName("room_name_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.room_name_input)

        self.room_number_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.room_number_label.setObjectName("room_number_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.room_number_label)
        self.room_number_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.room_number_input.setObjectName("room_number_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.room_number_input)
        self.building_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.building_label.setObjectName("building_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.building_label)
        self.building_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.building_input.setObjectName("building_input")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.building_input)
        self.capacity_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.capacity_label.setObjectName("capacity_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.capacity_label)
        self.capacity_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.capacity_input.setObjectName("capacity_input")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.capacity_input)

        self.room_name_label.setText("Room Name")
        self.room_number_label.setText("Room Number")
        self.building_label.setText("Building")
        self.capacity_label.setText("Capacity")

        self.buttonBox.accepted.connect(self.save_room)
        self.buttonBox.rejected.connect(self.cancel)        

    def cancel(self):
        print("cancel")
        self.close()

    def save_room(self):
        print("save room")
 

        name = self.room_name_input.text()
        number = self.validate_is_int(self.room_number_input.text(), "Number")
        building = self.validate_is_int(self.building_input.text(), "Building")
        capacity = self.validate_is_int(self.capacity_input.text(), "Capacity")

        if all([x is not None for x in [name, number, building, capacity]]):
            r = room_data.add_room(name, number, building, capacity)
            print(r)
            if r:
                self.parent().delete_room_list()
                self.parent().populate_room_list()
                self.close()
            else:
                QtWidgets.QMessageBox.warning(
                    self, 'Error', 'Integrity Error')                 

    def validate_is_int(self, input, field):
        try:
            value = int(input)
            return value
        except ValueError as e:
            print (type(e))
            QtWidgets.QMessageBox.warning(
                self, 'Error', '{} must be an integer'.format(field))  

class DeleteRoom(QtWidgets.QDialog):
    def __init__(self, room, parent=None):
        super(DeleteRoom, self).__init__(parent)  
        self.room = room 
 
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
        self.label.setGeometry(QtCore.QRect(110, 50, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.buttonBox.accepted.connect(self.delete_room)
        self.buttonBox.rejected.connect(self.cancel)
        self.label.setText("Delete this room?")

    def delete_room(self):
        print("delete_room")
        room_data.delete_room(self.room)
        self.parent().delete_room_list()
        self.parent().populate_room_list()
        self.close()

    def cancel(self):
        self.close()




class EditRoom(QtWidgets.QDialog):
    def __init__(self, room, parent=None):
        super(EditRoom, self).__init__(parent)
        self.room = room
        self.setObjectName("Edit Room")
        self.resize(357, 196)
        self.setSizeGripEnabled(False)
        self.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(20, 150, 321, 32))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(70, 50, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 39, 300, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.room_name_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.room_name_label.setObjectName("room_name_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.room_name_label)

        self.room_name_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.room_name_input.setObjectName("room_name_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.room_name_input)

        self.room_number_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.room_number_label.setObjectName("room_number_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.room_number_label)
        self.room_number_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.room_number_input.setObjectName("room_number_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.room_number_input)
        self.building_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.building_label.setObjectName("building_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.building_label)
        self.building_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.building_input.setObjectName("building_input")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.building_input)
        self.capacity_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.capacity_label.setObjectName("capacity_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.capacity_label)
        self.capacity_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.capacity_input.setObjectName("capacity_input")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.capacity_input)

        self.room_name_label.setText("Room Name")
        self.room_number_label.setText("Room Number")
        self.building_label.setText("Building")
        self.capacity_label.setText("Capacity")

        self.room_name_input.setText(self.room.roomname)
        self.room_number_input.setText(str(self.room.number))
        self.building_input.setText(str(self.room.building))
        self.capacity_input.setText(str(self.room.capacity))

        self.buttonBox.accepted.connect(self.save_room)
        self.buttonBox.rejected.connect(self.cancel)        

    def cancel(self):
        print("cancel")
        self.close()

    def save_room(self):
        print("save room")
        print(self.room)

        name = self.room_name_input.text()
        number = self.validate_is_int(self.room_number_input.text(), "Number")
        building = self.validate_is_int(self.building_input.text(), "Building")
        capacity = self.validate_is_int(self.capacity_input.text(), "Capacity")

        if all([x is not None for x in [name, number, building, capacity]]):
            self.room.roomname = name 
            self.room.number = number
            self.room.building = building
            self.room.capacity = capacity
            r = room_data.update_room_by_object(self.room)
            print(r)
            if r:
                self.parent().delete_room_list()
                self.parent().populate_room_list()
                self.close()
            else:
                QtWidgets.QMessageBox.warning(
                    self, 'Error', 'Integrity Error')                 

    def validate_is_int(self, input, field):
        try:
            value = int(input)
            return value
        except ValueError as e:
            print (type(e))
            QtWidgets.QMessageBox.warning(
                self, 'Error', '{} must be an integer'.format(field))    


