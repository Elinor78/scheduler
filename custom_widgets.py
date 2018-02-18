from PyQt5 import QtWidgets, QtCore
import sys

class ScheduleTableWidget(QtWidgets.QTableWidget):
	def __init__(self, user, parent=None):
		super(ScheduleTableWidget, self).__init__(parent)
		self.setColumnCount(17)
		self.setRowCount(2)
		self.available_checkboxes = []
		self.availability = [False]*16
		self.participants = [user]
		for i in range(1, 17):
			cell_widget = ScheduleCheckBoxWidget()
			self.setCellWidget(0, i, cell_widget)
			self.available_checkboxes.append(cell_widget)
		self.owner_availability()


	def owner_availability(self):
		fake_owner_data = [True, False]*8

		for i, is_available in enumerate(fake_owner_data):
			if is_available:
				cell_widget = self.available_checkboxes[i]
				cell_widget.chk_bx.setEnabled(True)

				checked = QtCore.Qt.Checked if is_available else QtCore.Qt.Unchecked
				owner_cell_widget = ScheduleCheckBoxWidget(checked=checked)
				self.setCellWidget(1, i+1, owner_cell_widget)



	def add_participant(self):
		fake_participant_data = [False, False, True, False]*4
		rowPosition = self.rowCount()
		self.insertRow(rowPosition)
		for i, is_available in enumerate(fake_participant_data):
			cell_widget = self.available_checkboxes[i]
			enabled = cell_widget.chk_bx.isEnabled()
			cell_widget.chk_bx.setEnabled(enabled and is_available)
			print(cell_widget.chk_bx.isEnabled())

			checked = QtCore.Qt.Checked if is_available else QtCore.Qt.Unchecked
			participant_cell_widget = ScheduleCheckBoxWidget(checked=checked)
			self.setCellWidget(rowPosition, i+1, participant_cell_widget)


	def check_availability(self):
		pass 




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
	form = ScheduleTableWidget(user="fake")

	form.show()
	form.add_participant()
	app.exec_()

