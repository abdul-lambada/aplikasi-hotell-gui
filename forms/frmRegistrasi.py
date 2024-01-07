import os, sys; sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
import sys
import psycopg2 as mc
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Registrasi import Registrasi

qtcreator_file  = "ui/registrasi.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class WindowRegistrasi(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.btnSimpan.clicked.connect(self.save_data) # Jika tombol simpan diklik
        self.txtKodeBooking.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox NIM
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

    def select_data(self):
        try:
            reg = Registrasi()

            # Get all 
            result = reg.getAllData()

            self.gridRegistrasi.setHorizontalHeaderLabels(['Id Registrasi', 'Kode Booking', 'No ktp', 'nama', 'jk', 'no_telp', 'Tgl datang', 'Tgl keluar', 'No kamar', 'Kode kamar', 'harga', 'Stts inap'])
            self.gridRegistrasi.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridRegistrasi.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridRegistrasi.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            kode_booking=self.txtKodeBooking.text()           
            reg = Registrasi()

            # search process
            result = reg.getByKODE_BOOKING(kode_booking)
            a = reg.affected
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
                self.cboKODEKAMAR.currentText(result[11])
                self.txtHarga.setText(result[12])

                if(result[10]=="Y"):
                    self.checkBoxYes.setChecked(True)
                    self.checkBoxNo.setChecked(False)
                else:
                    self.checkBoxYes.setChecked(False)
                    self.checkBoxNo.setChecked(True)

                self.btnSimpan.setText("Update")
                self.edit_mode=True
                self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
                self.btnHapus.setStyleSheet("background-color : red")
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtNOKTP.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("color:black;background-color : grey")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self, MainWindow):
        try:
            reg = Registrasi()
            kode_booking=self.txtKodeBooking.text()
            noktp=self.txtNOKTP.text()
            nama=self.txtNama.text()
            if self.optLaki.isChecked():
                jk="L"

            if self.optPerempuan.isChecked():
                jk="P"

            no_telp=self.txtNo_telp.text()
            tgl_datang= self.txtTgl_datang.date().toString("yyyy-MM-dd")
            tgl_keluar= self.txtTgl_keluar.date().toString("yyyy-MM-dd")
            nokamar= self.txtNOKAMAR.text()
            self.cboKODEKAMAR.currentText()
            self.txtHARGA.text()

            if self.checkBoxYes.isChecked():
                status_inap="Y"
            if self.checkBoxNo.isChecked():
                status_inap="N"


            if(self.edit_mode==False):   
                reg.kode_booking = kode_booking
                reg.noktp = noktp
                reg.nama = nama
                reg.jk = jk
                reg.no_telp = no_telp
                reg.tgl_datang = tgl_datang
                reg.tgl_keluar = tgl_keluar
                reg.nokamar = nokamar
                reg.kode_kamar = kode_kamar
                reg.harga = harga
                reg.status_inap = status_inap

                a = reg.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Registrasi Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Registrasi Gagal Tersimpan")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                reg.kode_booking = kode_booking
                reg.noktp = noktp
                reg.nama = nama
                reg.jk = jk
                reg.no_telp = no_telp
                reg.tgl_datang = tgl_datang
                reg.tgl_keluar = tgl_keluar
                reg.nokamar = nokamar
                reg.kode_kamar = kode_kamar
                reg.harga = harga
                reg.status_inap = status_inap

                a = reg.updateByKODE_BOOKING(kode_booking)
                if(a>0):
                    self.messagebox("SUKSES", "Data Registrasi Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Registrasi Gagal Diperbarui")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def delete_data(self, MainWindow):
        try:
            reg = Registrasi()
            kode_booking=self.txtKodeBooking.text()
                       
            if(self.edit_mode==True):
                a = reg.deleteByKODEBOOKING(kode_booking)
                if(a>0):
                    self.messagebox("SUKSES", "Data Peminjaman Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Peminjaman Gagal Dihapus")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

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
        self.cboKODEKAMAR.currentText("")
        self.txtHARGA.setText("")
        
        self.checkBoxYes.setChecked(False)
        self.checkBoxNo.setChecked(False)

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
    window = WindowRegistrasi()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = WindowRegistrasi()