import os, sys; sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
import sys
import psycopg2 as mc
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.keluar import Keluar
from classes.Registrasi import Registrasi
from classes.Tamu import Tamu

qtcreator_file  = "ui/keluar.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class WindowKeluar(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.txtKodeBooking.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox NIM
        self.btnClear.clicked.connect(self.clear_entry)

    def select_data(self):
        try:
            kel = Keluar()

            # Get all 
            result = kel.getAllData()

            self.gridKeluar.setHorizontalHeaderLabels(['Id keluar', 'Kode Booking', 'No ktp', 'nama', 'jk', 'no_telp', 'Tgl datang', 'Tgl keluar', 'No kamar', 'Stts inap', 'Tipe_kamar', 'harga'])
            self.gridKeluar.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridKeluar.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridKeluar.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            kode_booking=self.txtKodeBooking.text()           
            kel = Keluar()

            # search process
            result = kel.getByKODE_BOOKING(kode_booking)
            a = kel.affected
            if(a>0):
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
                self.cboTipeKamar.currentText(result[11])
                self.txtHarga.setText(result[12])
                self.btnSimpan.setText("Update")
                self.edit_mode=True
                self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
                self.btnHapus.setStyleSheet("background-color : red")
            else:
                self.messagebox("INFO", "Data Sudah Check-out")
                self.txtNOKTP.setFocus()
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self, MainWindow):
        self.txtKodeBooking.setText("")
        self.txtNOKTP.setText("")
        self.txtNama.setText("")
        self.optLaki.setChecked(False)
        self.optPerempuan.setChecked(False)
        self.txtNo_telp.setText("")
        self.txtTgl_datang.date().toString("yyyy-MM-dd")
        self.txtTgl_keluar.date().toString("yyyy-MM-dd")
        self.txtNOKAMAR.setText("")
        self.checkBoxYes.setChecked(False)
        self.checkBoxNo.setChecked(False)
        self.cboTipeKamar.currentText("")
        self.txtHARGA.setText("")
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
    window = WindowKeluar()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = WindowKeluar()