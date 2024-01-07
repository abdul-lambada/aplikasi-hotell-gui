import os, sys; sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
import sys
from PyQt5 import QtWidgets, uic
import psycopg2 as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Tamu import Tamu
from classes.Registrasi import Registrasi

qtcreator_file  = "ui/tamu.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class TamuWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.txtKodeBooking.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox NOKTP
        self.btnClear.clicked.connect(self.clear_entry)

    def select_data(self):
        try:
            tmu = Tamu()

            # Get all 
            result = tmu.getAllData()

            self.gridTamu.setHorizontalHeaderLabels(['ID TAMU', 'Kode Booking', 'NOKTP', 'Nama', 'Jenis Kelamin', 'No_Telp', 'tgl_datang', 'tgl_keluar', 'nokamar', 'status_inap', 'tipe_kamar', 'harga'])
            self.gridTamu.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridTamu.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridTamu.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")
 
    def search_data(self):
        try:           
            kode_booking=self.txtKodeBooking.text()           
            tmu = Tamu()
           
            # search process
            result = tmu.getByKODE_BOOKING(kode_booking)
            a = tmu.affected
            if(a>0):
                self.TampilData(result)
            else:
                self.messagebox("INFO", "Data Sudah Check-out")
                self.txtNama.setFocus()
                
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def TampilData(self,result):
        self.txtKodeBooking.text(result[2])
        self.txtNOKTP.setText(result[3])
        self.txtNama.setText(result[4])
        if(result[5]=="L"):
            self.optLaki.setChecked(True)
            self.optPerempuan.setChecked(False)
        else:
            self.optLaki.setChecked(False)
            self.optPerempuan.setChecked(True)

        self.txtNo_telp.setText(result[6])
        self.txtTgl_datang.setDate(result[7])
        self.txtTgl_keluar.setDate(result[8])
        self.txtNOKAMAR.setText(result[9])
        if(result[10]=="Y"):
            self.checkBoxYes.setChecked(True)
            self.checkBoxNo.setChecked(False)
        else:
            self.checkBoxYes.setChecked(False)
            self.checkBoxNo.setChecked(True)
        self.cboTipe_kamar.currentText(result[11])
        self.txtHarga.setText(result[12])

    def clear_entry(self, MainWindow):
        self.txtKodeBooking.text("")
        self.txtNOKTP.setText("")
        self.txtNama.setText("")
        self.optLaki.setChecked(False)
        self.optPerempuan.setChecked(False)
        self.txtNo_telp.setText("")
        self.txtTgl_datang.setDate("")
        self.txtTgl_keluar.setDate("")
        self.txtNOKAMAR.setText("")
        self.checkBoxYes.setChecked(False)
        self.checkBoxNo.setChecked(False)
        self.cboTipe_kamar.currentText("")
        self.txtharga.setText("")
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TamuWindow()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = TamuWindow()
    #window.show()
    #window.select_data()