from PyQt5 import QtWidgets, QtCore
import sys
import datetime
from backend.utils import EmployeeData, RoomData, MeetingData
from frontend.utils import _translate_slot_backward, _translate_slot_backward_key

employee_data = EmployeeData()
room_data = RoomData()
meeting_data = MeetingData()

class ScheduleTableWidget(QtWidgets.QTableWidget):
    def __init__(self, user, parent=None):
        super(ScheduleTableWidget, self).__init__(parent)
        self.setGeometry(1,66,256,192)
        self.verticalHeader().hide()
        self.date = datetime.date.today()
        self.user = user
        self.setColumnCount(17)
        self.setRowCount(1)
        self.available_checkboxes = []
        self.participants = []
        for i in range(1, 17):
            cell_widget = ScheduleCheckBoxWidget()
            self.setCellWidget(0, i, cell_widget)
            self.available_checkboxes.append(cell_widget)
        self.owner_availability()
        self.chosen_room = None

    def reset_table(self):
        self.available_checkboxes = []
        for i in range(1, 17):
            cell_widget = ScheduleCheckBoxWidget()
            self.setCellWidget(0, i, cell_widget)
            self.available_checkboxes.append(cell_widget)

        rowPosition = self.rowCount()
        for i in reversed(range(1, rowPosition)):
            self.removeRow(i)

        # owner availability by date
        self.owner_availability()
        # room availability by date (if room chosen)
        self._update_room()
        # all participant availability by date
        for participant in self.participants:
            self.update_participant(participant)




    def owner_availability(self):
        owner_availability = self._get_employee_meetings(self.user)

        rowPosition = self.rowCount()
        self.insertRow(rowPosition)

        item = QtWidgets.QTableWidgetItem(self.user.username)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.setItem(rowPosition, 0, item)

        for i, is_available in enumerate(owner_availability):
            if is_available:
                cell_widget = self.available_checkboxes[i]
                cell_widget.chk_bx.setEnabled(True)

                checked = QtCore.Qt.Checked if is_available else QtCore.Qt.Unchecked
                owner_cell_widget = ScheduleCheckBoxWidget(checked=checked)
                self.setCellWidget(rowPosition, i+1, owner_cell_widget)
            else:
                cell_widget = self.available_checkboxes[i]
                cell_widget.chk_bx.hide()


    def update_participant(self, participant):
        participant_availability = self._get_employee_meetings(participant)
        rowPosition = self.rowCount()
        self.insertRow(rowPosition)

        item = QtWidgets.QTableWidgetItem(participant.username)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.setItem(rowPosition, 0, item)

        for i, is_available in enumerate(participant_availability):
            cell_widget = self.available_checkboxes[i]
            enabled = cell_widget.chk_bx.isEnabled()
            if enabled and is_available:
                cell_widget.chk_bx.setEnabled(enabled and is_available)
                print(cell_widget.chk_bx.isEnabled())

                checked = QtCore.Qt.Checked if is_available else QtCore.Qt.Unchecked
                participant_cell_widget = ScheduleCheckBoxWidget(checked=checked)
                self.setCellWidget(rowPosition, i+1, participant_cell_widget)
            else:
                cell_widget.chk_bx.hide()        

    def add_participant(self, username):
        print("in add_participant")
        print(username)
        print(self.user.username)
        if username != self.user.username:
            if self._check_username(username):
                participant = employee_data.get_employee_by_username(username)
                if participant not in self.participants:#can't use this in update
                    self.participants.append(participant)
                    participant_availability = self._get_employee_meetings(participant)
                    rowPosition = self.rowCount()
                    self.insertRow(rowPosition)

                    item = QtWidgets.QTableWidgetItem(username)
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.setItem(rowPosition, 0, item)

                    for i, is_available in enumerate(participant_availability):

                        cell_widget = self.available_checkboxes[i]
                        enabled = cell_widget.chk_bx.isEnabled()
                        if enabled and is_available:
                            cell_widget.chk_bx.setEnabled(enabled and is_available)
                            print(cell_widget.chk_bx.isEnabled())

                            checked = QtCore.Qt.Checked if is_available else QtCore.Qt.Unchecked
                            participant_cell_widget = ScheduleCheckBoxWidget(checked=checked)
                            self.setCellWidget(rowPosition, i+1, participant_cell_widget)
                        else:
                            cell_widget.chk_bx.hide()
                else:
                    QtWidgets.QMessageBox.warning(
                            self, 'Error', 'Employee already in meeting.')  
            else:
                QtWidgets.QMessageBox.warning(
                            self, 'Error', 'Invalid employee username')
        else:
            QtWidgets.QMessageBox.warning(
                        self, 'Error', 'Cannot add owner to meeting')           

    def _check_username(self, username):
        return employee_data.check_username(username)           

    def check_availability(self):
        pass 

    def add_room(self, room):
        if self.date:
            if not self.chosen_room:
                #TODO: get data
                #TODO: save to room attribute
                #TODO: check that room is only one
                print("in widget add room")
                room_availability = self._get_room_meetings(room)
                rowPosition = self.rowCount()
                self.insertRow(rowPosition)
                item = QtWidgets.QTableWidgetItem(room.roomname)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.setItem(rowPosition, 0, item)
                for i, is_available in enumerate(room_availability):
                    cell_widget = self.available_checkboxes[i]
                    enabled = cell_widget.chk_bx.isEnabled()
                    if enabled and is_available:
                        cell_widget.chk_bx.setEnabled(enabled and is_available)
                        print(cell_widget.chk_bx.isEnabled())

                        checked = QtCore.Qt.Checked if is_available else QtCore.Qt.Unchecked
                        participant_cell_widget = ScheduleCheckBoxWidget(checked=checked)
                        self.setCellWidget(rowPosition, i+1, participant_cell_widget)
                    else:
                        cell_widget.chk_bx.hide()
                self.chosen_room = room

            else:
                QtWidgets.QMessageBox.warning(
                        self, 'Error', 'Cannot add more than one room')                
        else:
            QtWidgets.QMessageBox.warning(
                    self, 'Error', 'Must choose a date to add a room') 

    def _get_room_meetings(self, room):
        times = []
        meetings = room_data.get_room_meetings_by_date(room, self.date)
        print(meetings)
        for meeting in meetings:
            for ts in meeting.timeslots:
                if isinstance(ts.begin_time, str):
                    times.append(_translate_slot_backward_key(ts.begin_time))
                else:
                    times.append(_translate_slot_backward(ts.begin_time.value))
        print(times)
        _times = [True]*16
        for i in times:
            _times[i] = False
        print(_times)
        return _times

    def _get_employee_meetings(self, employee):
        times = []
        meetings = meeting_data.get_meetings_by_date_and_user(self.date, employee) 
        print(meetings)
        for meeting in meetings:
            for ts in meeting.timeslots:
                print(ts)
                print(type(ts))
                print(ts.begin_time)
                print(type(ts.begin_time))
                if isinstance(ts.begin_time, str):
                    times.append(_translate_slot_backward_key(ts.begin_time))
                else:
                    times.append(_translate_slot_backward(ts.begin_time.value))
        print(times)
        _times = [True]*16
        for i in times:
            _times[i] = False
        print(_times)
        return _times

    def _update_room(self):
        if self.chosen_room:
            #TODO find chosen room on list and remove
            print("in widget _update room")
            room_availability = self._get_room_meetings(self.chosen_room)


            rowPosition = self.rowCount()
            print("rowPosition")
            print(rowPosition)
            self.insertRow(rowPosition)
            item = QtWidgets.QTableWidgetItem(self.chosen_room.roomname)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.setItem(rowPosition, 0, item)
            for i, is_available in enumerate(room_availability):#going to have to redo the entire thing

                cell_widget = self.available_checkboxes[i]
                enabled = cell_widget.chk_bx.isEnabled()
                if enabled and is_available:
                    cell_widget.chk_bx.setEnabled(enabled and is_available)
                    print(cell_widget.chk_bx.isEnabled())

                    checked = QtCore.Qt.Checked if is_available else QtCore.Qt.Unchecked
                    participant_cell_widget = ScheduleCheckBoxWidget(checked=checked)
                    self.setCellWidget(rowPosition, i+1, participant_cell_widget)
                else:
                    cell_widget.chk_bx.hide()


class ScheduleCheckBoxWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, checked=QtCore.Qt.Unchecked, enabled=False):
        super(ScheduleCheckBoxWidget, self).__init__(parent)
        self.chk_bx = QtWidgets.QCheckBox()
        self.chk_bx.setObjectName("chk_bx")
        self.chk_bx.setCheckState(checked)
        self.chk_bx.setEnabled(enabled)
        lay_out = QtWidgets.QHBoxLayout(self)
        lay_out.addWidget(self.chk_bx)
        lay_out.setAlignment(QtCore.Qt.AlignCenter)
        lay_out.setContentsMargins(0,0,0,0)
        self.setLayout(lay_out)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #form = ScheduleTableWidget(user="fake")

    #form.show()
    #form.add_participant()
    search = EmployeeSearchWidget()
    search.show()
    app.exec_()

