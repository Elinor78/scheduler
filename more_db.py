from backend.models import init_db
from backend.utils import EmployeeData, RoomData, MeetingData, TimeSlotData, EmployeeMeetingData
import os
import datetime

dirname = os.path.dirname
try:
	os.remove(os.path.abspath(os.path.join(dirname(dirname(__file__)), "scheduler.db")))
except:
	pass
engine = init_db('sqlite:///scheduler.db')	


employee_data = EmployeeData()

joe = employee_data.add_employee('joe', 'p')
joe = employee_data.update_employee(joe.id, {'email': 'joe@fake.com', 'telephone':'800-999-9999', 'first_name': 'Joe', 'last_name': 'Smith', 'is_admin': True})

jack = employee_data.add_employee('jack', 'p')
jack = employee_data.update_employee(jack.id, {'email': 'jack@fake.com', 'telephone':'800-999-9999', 'first_name': 'Jack', 'last_name': 'Jones', })

jill = employee_data.add_employee('jill', 'p')
jill = employee_data.update_employee(jill.id, {'email': 'jill@fake.com', 'telephone':'800-999-9999', 'first_name': 'Jill', 'last_name': 'Lin', })

room_data = RoomData()

room1 = room_data.add_room("Room 1", 1, 2, 100)
room2 = room_data.add_room("Room 2", 2, 2, 40)
room3 = room_data.add_room("Room 3", 3, 2, 35)
room4 = room_data.add_room("Room 4", 1, 10, 100)
room5 = room_data.add_room("Room 5", 2, 10, 50)


