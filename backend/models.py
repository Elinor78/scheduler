import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, String, Integer, Boolean, Date, Table, Enum, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker, column_property
from sqlalchemy import create_engine
from sqlalchemy.ext.hybrid import hybrid_property



Base = declarative_base()
session = scoped_session(sessionmaker())

class EmployeeMeeting(Base):
    __tablename__ = 'employeemeeting'
    employee_id = Column(Integer, ForeignKey('employee.id'), primary_key=True)
    meeting_id = Column(Integer, ForeignKey('meeting.id'), primary_key=True)
    pending = Column(Boolean, default=True)
    accepted = Column(Boolean, default=False)
    employee = relationship("Employee", back_populates="meetings")
    meeting = relationship("Meeting", back_populates="employees")


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=True, default="")
    last_name = Column(String(100), nullable=True, default="")
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(100), nullable=True)
    telephone = Column(String(100), nullable=True)
    is_admin = Column(Boolean, default=False)
    meetings = relationship("EmployeeMeeting", back_populates='employee')

association_table = Table('timeblock', Base.metadata,
    Column('meeting_id', Integer, ForeignKey('meeting.id')),
    Column('timeslot_id', Integer, ForeignKey('timeslot.id'))
)

class Meeting(Base):
    __tablename__ = 'meeting'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    room = Column(Integer, ForeignKey("room.id"))
    owner = Column(Integer, ForeignKey("employee.id"))
    date = Column(Date, nullable=False)
    employees = relationship("EmployeeMeeting", back_populates='meeting')
    timeslots = relationship("TimeSlot",
        secondary=association_table,
        back_populates="meetings"
        )

class Room(Base):
    __tablename__ = "room"
    id = Column(Integer, primary_key=True)
    roomname = Column(String, unique=True, nullable=False)
    number = Column(Integer, nullable=False)
    building = Column(Integer, nullable=False)
    capacity = Column(Integer, nullable=True)


    __table_args__ = (UniqueConstraint('number', 'building', name='room_uc'),)

class TimeSlotEnum(enum.Enum):
    one = "9:00 am"
    two = "9:30 am"
    three = "10:00 am"
    four = "10:30 am"
    five = "11:00 am"
    six = "11:30 am"
    seven = "12:00 pm"
    eight = "12:30 pm"
    nine = "1:00 pm"
    ten = "1:30 pm"
    eleven = "2:00 pm"
    twelve = "2:30 pm"
    thirteen = "3:00 pm"
    fourteen = "3:30 pm"
    fifteen = "4:00 pm"
    sixteen = "4:30 pm"

class TimeSlot(Base):
    __tablename__ = 'timeslot'
    
    id = Column(Integer, primary_key=True)

    begin_time = Column(Enum(TimeSlotEnum))
    meetings = relationship('Meeting', 
        secondary=association_table, back_populates="timeslots")


def init_db(dbname):
    engine = create_engine(dbname, echo=False)
    session.configure(bind=engine, autoflush=False, expire_on_commit=False)
    Base.metadata.create_all(engine)
    return engine

