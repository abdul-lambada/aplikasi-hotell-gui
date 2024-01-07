import os, sys; sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
#import psycopg2 as mc
from PyQt5 import QtWidgets, uic
#from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Users import Users as login
from forms.MainWindow import MainWindow

qtcreator_file  = "./ui/login.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class LoginWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #EvenSetup
        self.btnSubmit.clicked.connect(self.app_login) # ketika klik submit
        
    def app_login(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        valid = usr.Validasi(username,password)
        #Role = usr.rolename.strip()
        if(valid[0]==True) : # Login Berhasil
            self.messagebox("Info","Login Berhasil")
            if(valid[1]=='admin'):
                self.messagebox("Info","Anda Login Sebagai Admin ")
                dashboard.showFullScreen()
            if(valid[1]=='operator'):
                self.messagebox("Info","Anda Login Sebagai Operator ")
                dashboard.showFullScreen()
            window.close()
        else: #login Gagal
            self.messagebox("Info","Maaf Login Gagal ")
    def messagebox(self,title,message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()
        
if __name__== "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow() #load Object Window login
    dashboard = MainWindow() # load Window Dashboard
    window.show() # Menampilkan Window
    usr = login()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow() # load Window Login
    dashboard = MainWindow() # load object window Login
    usr = login()