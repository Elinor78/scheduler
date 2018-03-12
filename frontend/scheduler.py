from PyQt5 import QtWidgets
import sys
import os

from frontend.mainwindow import Ui_MainWindow
from frontend.dailyschedule import DailySchedule
from frontend.login import Login
from frontend.schedulemeeting import ScheduleMeeting
from frontend.viewcalendar import ViewCalendar
from frontend.viewprofile import ViewProfile
from frontend.viewnotifications import ViewNotifications
from frontend.logout import Logout
from frontend.managerooms import ManageRooms
from frontend.manageusers import ManageUsers

from backend.models import init_db


class Scheduler(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, user, parent=None):
        super(Scheduler, self).__init__(parent)
        self.setupUi(self)
        self.user = user
        if self.is_admin() or self.user.username == "joe":
            self.manage_rooms_button.setEnabled(True)
            self.manage_users_button.setEnabled(True)
        self.schedule_meeting_button.clicked.connect(self.showScheduleMeeting)
        self.view_calendar_button.clicked.connect(self.showViewCalendar)
        self.view_profile_button.clicked.connect(self.showProfile)
        self.view_notifications_button.clicked.connect(self.showNotifications)
        self.logout_button.clicked.connect(self.showLogout)
        self.view_daily_schedule_button.clicked.connect(self.showDailySchedule)
        self.manage_rooms_button.clicked.connect(self.showManageRooms)
        self.manage_users_button.clicked.connect(self.showManageUsers)
        

        self.buttons = [self.schedule_meeting_button, self.view_calendar_button,
            self.view_profile_button, self.view_notifications_button, self.logout_button,
            self.view_daily_schedule_button, self.manage_rooms_button, self.manage_users_button
            ]

        self.showNotifications()

    def _set_button(self, button):
        button.setStyleSheet("background-color: lightsalmon")
        for b in self.buttons:
            if b != button:
                b.setStyleSheet("")

    def is_admin(self):
        return self.user.is_admin

    def showDailySchedule(self):
        self.frame.hide()
        self._set_button(self.view_daily_schedule_button)
        self.frame = DailySchedule(self.user, self)
        self.frame.show()

    def showScheduleMeeting(self):
        self.frame.hide()
        self._set_button(self.schedule_meeting_button)
        self.frame = ScheduleMeeting(self.user, self)
        self.frame.show()        

    def showViewCalendar(self):
        self.frame.hide()
        self._set_button(self.view_calendar_button)
        self.frame = ViewCalendar(self.user, self)
        self.frame.show()
        

    def showProfile(self):
        self.frame.hide()
        self._set_button(self.view_profile_button)
        self.frame = ViewProfile(self.user, self)
        self.frame.show()

    def showNotifications(self):
        self.frame.hide()
        self._set_button(self.view_notifications_button)
        self.frame = ViewNotifications(self.user, self)
        self.frame.show()

    def showLogout(self):
        print("showLogout")
        self.frame.hide()
        self._set_button(self.logout_button)
        self.frame = Logout(self.user, self)
        self.frame.show()

    def showManageRooms(self):
        self.frame.hide()
        self._set_button(self.manage_rooms_button)
        self.frame = ManageRooms(self.user, self)
        self.frame.show()

    def showManageUsers(self):
        self.frame.hide()
        self._set_button(self.manage_users_button)
        self.frame = ManageUsers(self.user, self)
        self.frame.show()