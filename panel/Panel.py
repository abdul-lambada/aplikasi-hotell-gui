import os, sys; sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from forms.frmTamu import TamuWindow
from forms.frmRegistrasi import WindowRegistrasi
from forms.frmKeluar import WindowKeluar
dock = QtWidgets.QDockWidget()
def child_panels(self):   
    tamu_panel(self)
    registrasi_panel(self)
    keluar_panel(self)

def tamu_panel(self):     
    tamu_widget = TamuWindow()
    tamu_widget.select_data()
    self.centralwidget = tamu_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)
        

def registrasi_panel(self):
    registrasi_widget = WindowRegistrasi()
    registrasi_widget.select_data()
    self.centralwidget = registrasi_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def keluar_panel(self):
    keluar_widget = WindowKeluar()
    keluar_widget.select_data()
    self.centralwidget = keluar_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def tamu_on(self):
    tamu_widget = TamuWindow()
    tamu_widget.select_data()
    self.centralwidget = tamu_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

def registrasi_on(self):
    registrasi_widget = WindowRegistrasi()
    registrasi_widget.select_data()
    self.centralwidget = registrasi_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

def keluar_on(self):
    keluar_widget = WindowKeluar()
    keluar_widget.select_data()
    self.centralwidget = keluar_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()




        
     