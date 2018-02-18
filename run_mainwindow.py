from PyQt5 import QtGui, QtWidgets
import sys
import os
import datetime

import mainwindow
import dailyschedule
import login
import forgotpassword
import schedulemeeting

class ScheduleMeeting(QtWidgets.QFrame, schedulemeeting.Ui_schedulemeeting):
    def __init__(self, user, parent=None):
        super(ScheduleMeeting, self).__init__(parent)
        self.setupUi(self) 
        

    def add_participant(self):
        pass
        #TODO search box for finding participant
            #if click on one and OK, then call self.tableWidget.add_participant 
            # with user info
            # if click cancel, pass, basically


    def save_meeting(self):
        pass
        #TODO - whole bunch





class DailySchedule(QtWidgets.QFrame, dailyschedule.Ui_DailySchedule):
    def __init__(self, parent=None):
        super(DailySchedule, self).__init__(parent)
        self.setupUi(self)
        self.set_date()

    def set_date(self):
        today = datetime.date.today()
        self.label.setText(today.strftime('%B %d %Y'))
        width = self.label.fontMetrics().boundingRect(self.label.text()).width()
        height = self.label.fontMetrics().boundingRect(self.label.text()).height()
        self.label.resize(width, height)        


class ForgotPassword(QtWidgets.QDialog, forgotpassword.Ui_ForgotPassword):
    def __init__(self, parent=None):
        super(ForgotPassword, self).__init__(parent)
        self.setupUi(self)
        self.cancel_button.clicked.connect(self.cancel_change)
        self.submit_button.clicked.connect(self.submit_change)

    def cancel_change(self):
        self.accept() 

    def submit_change(self):
        #TODO: hook up to db
        #STUB
        if self.username_lineedit.text() and self.email_lineedit.text():
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Bad user or email') 


class Login(QtWidgets.QDialog, login.Ui_Login):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self) 
        self.login_button.clicked.connect(self.handleLogin)
        self.forgot_password_button.clicked.connect(self.forgot_password)
        
    def handleLogin(self):
        #TODO: hook up to user DB
        if (self.username_lineedit.text() == 'foo' and
            self.password_lineedit.text() == 'bar'):
            self.user = self.username_lineedit.text()
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Bad user or password') 

    def forgot_password(self):
        #TODO hook up to db
        f = ForgotPassword()
        f.exec_()

class Scheduler(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
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
        return True

    def showDailySchedule(self):
        self.frame = DailySchedule(self)
        self.frame.show()

    def showScheduleMeeting(self):
        self.frame = ScheduleMeeting(self.user, self)
        self.frame.show()        

    def showViewCalendar(self):
        print("view calendar")
        

    def showProfile(self):
        print("showProfile")

    def showNotifications(self):
        print("showNotifications")

    def showLogout(self):
        print("showLogout")

    def showManageRooms(self):
        print("showManageRooms")

    def showManageUsers(self):
        print("showManageUsers")

def main():
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    if login.exec_() == QtWidgets.QDialog.Accepted:
        form = Scheduler(user=login.user)
        form.show()
        app.exec_()


if __name__ == '__main__':
    main()
