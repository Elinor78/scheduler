from PyQt5 import QtGui, QtWidgets
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
        if self.is_admin():
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

    def is_admin(self):
        return self.user.is_admin

    def showDailySchedule(self):
        self.frame.hide()
        self.frame = DailySchedule(self.user, self)
        self.frame.show()

    def showScheduleMeeting(self):
        self.frame.hide()
        self.frame = ScheduleMeeting(self.user, self)
        self.frame.show()        

    def showViewCalendar(self):
        self.frame.hide()
        self.frame = ViewCalendar(self.user, self)
        self.frame.show()
        

    def showProfile(self):
        self.frame.hide()
        self.frame = ViewProfile(self.user, self)
        self.frame.show()

    def showNotifications(self):
        self.frame.hide()
        self.frame = ViewNotifications(self.user, self)
        self.frame.show()

    def showLogout(self):
        print("showLogout")
        self.frame.hide()
        self.frame = Logout(self.user, self)
        self.frame.show()

    def showManageRooms(self):
        self.frame.hide()
        self.frame = ManageRooms(self.user, self)
        self.frame.show()

    def showManageUsers(self):
        self.frame.hide()
        self.frame = ManageUsers(self.user, self)
        self.frame.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    engine = init_db('sqlite:///sqlalchemy_example.db') 
    login = Login()
    if login.exec_() == QtWidgets.QDialog.Accepted:
        form = Scheduler(user=login.user)
        form.show()
        app.exec_()


if __name__ == '__main__':
    main()
