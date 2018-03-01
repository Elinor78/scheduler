from backend.models import Base, session, init_db, Employee, EmployeeMeeting, Meeting, Room
import os
from sqlalchemy import exc


def handle_exception():
	init_db('sqlite:///sqlalchemy_example.db')

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

	def delete_employee_obj(self, employee):
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

	def update_employee_by_obj(self, employee):
		try:
			employee_id = employee.id 
			session.commit()
			return self.get_employee(employee_id)
		except Exception as e:
			session.rollback()
			handle_exception()
			return False		


class MeetingData:
	def add_employees_to_meeting(self):
		pass



class RoomData:
	def add_room(self, roomname, number, building, capacity=None):
		try:
			if capacity:
				room = Room(roomname=roomname, number=number, building=building, capacity=capacity)
			else:
				room = Room(roomname=roomname, number=number, building=building)
			session.add(room)
			session.commit()
			room = session.query(Room).filter(Room.number == number).filter(Room.building == building).one()
			return room
		except Exception as e:
			session.rollback()
			handle_exception()
			return False

	def get_all_rooms(self):
		return session.query(Room).all()

	def get_room_by_name(self, roomname):
		room = session.query(Room).filter(Room.roomname == roomname).first()
		return room

	def get_room_by_id(self, room_id):
		room = session.query(Room).filter(Room.id == room_id).one()
		return room

	 	
	def update_room_by_object(self, room_obj):
		try:
			room_id = room_obj.id 
			session.commit()
			return self.get_room_by_id(room_id)
		except Exception as e:
			session.rollback()
			handle_exception()
			return False

	def delete_room(self, room):
		session.delete(room)
		session.commit()

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


