from PyQt5 import QtGui, QtWidgets
import sys
from frontend.login import Login
from frontend.scheduler import Scheduler
from backend.models import init_db

def main():
    app = QtWidgets.QApplication(sys.argv)
    engine = init_db('sqlite:///scheduler.db') 
    login = Login()
    if login.exec_() == QtWidgets.QDialog.Accepted:
        form = Scheduler(user=login.user)
        form.show()
        sys.exit(app.exec_()) 


if __name__ == '__main__':
    main()
