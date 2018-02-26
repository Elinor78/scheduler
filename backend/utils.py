from backend.models import Base, session, init_db, Employee, EmployeeMeeting, Meeting, Room
import os


class EmployeeData:
	def add_employee(self, username, password):
		employee = Employee(username=username, password=password)
		session.add(employee)
		session.commit()
		return self.get_employee_by_username(username)

	def delete_employee(self, employee_id):
		employee = session.query(Employee).filter(Employee.id == employee_id).one()
		print (employee)
		session.delete(employee)
		session.commit()

	def get_employee(self, employee_id):
		employee = session.query(Employee).filter(Employee.id == employee_id).one()
		return employee

	def get_employee_by_username(self, username):
		employee = session.query(Employee).filter(Employee.username == username).one()
		return employee

	def get_employee_meetings(self, employee_id):
		a = session.query(Employee).join(EmployeeMeeting, Employee.meetings).join(Meeting, EmployeeMeeting.meeting).filter(Employee.id == employee_id)
		return a.all()

	def get_all_employees(self):
		return session.query(Employee).all()

	def get_some_employees(self, employee_ids):
		return session.query(Employee).filter(Employee.id in employee_ids).all()

	def add_employee_to_meeting(self, meeting_id, employee_id):
		employee_meeting = EmployeeMeeting(meeting_id=meeting_id, employee_id=employee_id)
		session.add(employee_meeting)
		session.commit()

	def update_employee(self, employee_id, kwargs):
		employee = self.get_employee(employee_id)
		for kwarg, value in kwargs.items():
			setattr(employee, kwarg, value)
		session.commit()
		return self.get_employee(employee_id)


class MeetingData:
	def add_meeting(self):
		pass

class RoomData:
	def add_room(self, number, building, capacity=None):
		if capacity:
			room = Room(number=number, building=building, capacity=capacity)
		else:
			room = Room(number=number, building=building)
		session.add(room)
		session.commit()
		return room

	 	

if __name__ == '__main__':
	engine = init_db('sqlite:///sqlalchemy_example.db')	
	e = EmployeeData()
	e.add_employee('joe', 'password')
	emp = e.get_employee_by_username('joe')
	m = e.get_employee_meetings(emp.id)
	print(m)

	r = RoomData()
	room = r.add_room(10, 100)
	print (room.id)



	# deleting the db so it migrates on changes
	#dirname = os.path.dirname
	#os.remove(os.path.abspath(os.path.join(dirname(dirname(__file__)), "sqlalchemy_example.db")))

