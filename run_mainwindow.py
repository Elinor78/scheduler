from PyQt5 import QtGui, QtWidgets
import sys
import os
import datetime

import mainwindow
import dailyschedule
import login
import forgotpassword
import schedulemeeting
import viewcalendar
import viewprofile
import viewnotifications
import logout
import managerooms
import addroom
import manageusers

class AddUser(QtWidgets.QFrame, addroom.Ui_AddRoom):
    def __init__(self, user, parent=None):
        super(AddUser, self).__init__(parent)
        self.setupUi(self)  

class ManageUsers(QtWidgets.QFrame, manageusers.Ui_ManageUsers):
    def __init__(self, user, parent=None):
        super(ManageUsers, self).__init__(parent)
        self.setupUi(self)  
        self.user = user
        self.add_user_button.clicked.connect(lambda: self.showAddUser(parent))


    def showAddUser(self, parent):
        parent.frame.hide()
        parent.frame = AddUser(self.user, parent)
        parent.frame.show()   

class AddRoom(QtWidgets.QFrame, addroom.Ui_AddRoom):
    def __init__(self, user, parent=None):
        super(AddRoom, self).__init__(parent)
        self.setupUi(self)     

class ManageRooms(QtWidgets.QFrame, managerooms.Ui_ManageRooms):
    def __init__(self, user, parent=None):
        super(ManageRooms, self).__init__(parent)
        self.setupUi(self)
        self.user = user
        self.add_room_button.clicked.connect(lambda: self.showAddRoom(parent))


    def showAddRoom(self, parent):
        parent.frame.hide()
        parent.frame = AddRoom(self.user, parent)
        parent.frame.show()


class Logout(QtWidgets.QDialog, logout.Ui_Logout):
    def __init__(self, user, parent=None):
        super(Logout, self).__init__(parent)
        self.setupUi(self)    

class ViewNotifications(QtWidgets.QFrame, viewnotifications.Ui_ViewNotifications):
    def __init__(self, user, parent=None):
        super(ViewNotifications, self).__init__(parent)
        self.setupUi(self) 

class ViewCalendar(QtWidgets.QFrame, viewcalendar.Ui_ViewCalendar):
    def __init__(self, user, parent=None):
        super(ViewCalendar, self).__init__(parent)
        self.setupUi(self)  

class ViewProfile(QtWidgets.QFrame, viewprofile.Ui_ViewProfile):   
    def __init__(self, user, parent=None):
        super(ViewProfile, self).__init__(parent)
        self.setupUi(self) 

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
        self.frame.hide()
        self.frame = DailySchedule(self)
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
    login = Login()
    if login.exec_() == QtWidgets.QDialog.Accepted:
        form = Scheduler(user=login.user)
        form.show()
        app.exec_()


if __name__ == '__main__':
    main()
