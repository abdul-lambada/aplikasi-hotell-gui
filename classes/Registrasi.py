import os, sys; sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
from config.db import DBConnection as mydb

class Registrasi:

    def __init__(self):
        self.__idregistrasi=None
        self.__kode_booking=None
        self.__noktp=None
        self.__nama=None
        self.__jk=None
        self.__no_telp=None
        self.__tgl_datang=None
        self.__tgl_keluar=None
        self.__nokamar=None
        self.__kode_kamar=None
        self.__harga=None
        self.__status_inap=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "Kode Booking:" + self.__kode_booking + "\n" + "Noktp:" + self.__noktp + "\n" + "nama" + self.__nama + "\n" + "Jk" + self.__jk + "\n" + "No_Telp:" + self.__no_telp + "\n" + "Tgl datang" + self.__tgl_datang + "\n" + "Tgl keluar:" + self.__tgl_keluar+ "\n" + "nokamar:" + self.__nokamar + "\n" + "kode_kamar" + self.__kode_kamar + "\n" + "harga" + self.__harga + "\n" + "Stts inap:" + self.__status_inap
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def idregistrasi(self):
        return self.__idregistrasi

    @property
    def kode_booking(self):
        return self.__kode_booking

    @kode_booking.setter
    def kode_booking(self, value):
        self.__kode_booking = value

    @property
    def noktp(self):
        return self.__noktp

    @noktp.setter
    def noktp(self, value):
        self.__noktp = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value

    @property
    def no_telp(self):
        return self.__no_telp

    @no_telp.setter
    def no_telp(self, value):
        self.__no_telp = value

    @property
    def tgl_datang(self):
        return self.__tgl_datang

    @tgl_datang.setter
    def tgl_datang(self, value):
        self.__tgl_datang = value

    @property
    def tgl_keluar(self):
        return self.__tgl_keluar

    @tgl_keluar.setter
    def tgl_keluar(self, value):
        self.__tgl_keluar = value
        
    @property
    def nokamar(self):
        return self.__nokamar

    @nokamar.setter
    def nokamar(self, value):
        self.__nokamar = value

    @property
    def kode_kamar(self):
        return self.__kode_kamar

    @kode_kamar.setter
    def kode_kamar(self, value):
        self.__kode_kamar = value

    @property
    def harga(self):
        return self.__harga
    
    @harga.setter
    def harga(self, value):
        self.__harga = value

    @property
    def status_inap(self):
        return self.__status_inap

    @status_inap.setter
    def status_inap(self, value):
        self.__status_inap = value


    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_booking, self.__noktp, self.__nama, self.__jk, self.__no_telp, self.__tgl_datang, self.__tgl_keluar, self.__nokamar, self.__kode_kamar, self.__harga, self.__status_inap)
        sql="INSERT INTO registrasi (kode_booking, noktp, nama, jk, no_telp, tgl_datang, tgl_keluar, nokamar, kode_kamar, harga, status_inap) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, idregistrasi):
        self.conn = mydb()
        val = (self.__kode_booking, self.__noktp, self.__nama, self.__jk, self.__no_telp, self.__tgl_datang, self.__tgl_keluar, self.__nokamar, self.__kode_kamar, self.__harga, self.__status_inap, idregistrasi)
        sql="UPDATE registrasi SET kode_booking = %s, noktp = %s, nama=%s, jk=%s, no_telp=%s, tgl_datang=%s, tgl_keluar=%s, nokamar=%s, kode_kamar=%s, harga=%s, status_inap=%s WHERE idregistrasi=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByKODE_BOOKING(self, kode_booking):
        self.conn = mydb()
        val = (self.__noktp, self.__nama, self.__jk, self.__no_telp, self.__tgl_datang, self.__tgl_keluar, self.__nokamar, self.__kode_kamar, self.__harga, self.__status_inap, kode_booking)
        sql="UPDATE registrasi SET noktp = %s, nama=%s, jk=%s, no_telp=%s, tgl_datang=%s, tgl_keluar=%s, nokamar=%s, kode_kamar=%s, harga=%s, status_inap=%s  WHERE kode_booking=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, idregistrasi):
        self.conn = mydb()
        sql="DELETE FROM registrasi WHERE idregistrasi='" + str(idregistrasi) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByKODEBOOKING(self, kode_booking):
        self.conn = mydb()
        sql="DELETE FROM registrasi WHERE kode_booking='" + str(kode_booking) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByIDREGISTRASI(self, idregistrasi):
        self.conn = mydb()
        sql="SELECT * FROM registrasi WHERE idregistrasi='" + str(idregistrasi) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_booking = self.result[2]
        self.__noktp = self.result[3]
        self.__nama = self.result[4]
        self.__jk = self.result[5]
        self.__no_telp = self.result[6]
        self.__tgl_datang = self.result[7]
        self.__tgl_keluar = self.result[8]
        self.__nokamar = self.result[9]
        self.__kode_kamar = self.result[10]
        self.__harga =self.result[11]
        self.__status_inap = self.result[12]
        self.conn.disconnect
        return self.result

    def getByKODE_BOOKING(self, kode_booking):
        a=str(kode_booking)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM registrasi WHERE kode_booking='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_booking = self.result[2]
            self.__noktp = self.result[3]
            self.__nama = self.result[4]
            self.__jk = self.result[5]
            self.__no_telp = self.result[6]
            self.__tgl_datang = self.result[7]
            self.__tgl_keluar = self.result[8]
            self.__nokamar = self.result[9]
            self.__kode_kamar = self.result[10]
            self.__harga =self.result[11]
            self.__status_inap = self.result[12]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_booking = ''
            self.__noktp = ''
            self.__nama = ''
            self.__jk = ''
            self.__no_telp = ''
            self.__tgl_datang = ''
            self.__tgl_keluar = ''
            self.__nokamar = ''
            self.__kode_kamar = ''
            self.__harga = ''
            self.__status_inap = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM registrasi"
        self.result = self.conn.findAll(sql)
        return self.result

reg = Registrasi()
a = mydb()
sql="SELECT * FROM registrasi"
cur = a.findAll(sql)
# Get all 
result = reg.getAllData()
print(result)