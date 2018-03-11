from backend.models import init_db
from backend.utils import EmployeeData, RoomData, MeetingData, TimeSlotData, EmployeeMeetingData
import os
import datetime

dirname = os.path.dirname
os.remove(os.path.abspath(os.path.join(dirname(dirname(__file__)), "sqlalchemy_example.db")))

engine = init_db('sqlite:///sqlalchemy_example.db')	


employee_data = EmployeeData()

joe = employee_data.add_employee('joe', 'p')
joe = employee_data.update_employee(joe.id, {'email': 'joe@fake.com', 'telephone':'800-999-9999', 'first_name': 'Joe', 'last_name': 'Smith', 'is_admin': True})
