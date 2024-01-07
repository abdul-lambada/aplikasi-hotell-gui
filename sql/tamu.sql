-- ----------------------------
-- Table structure for tamu
-- ---------------------------
DROP TABLE IF EXISTS "public"."tamu";
CREATE TABLE "public"."tamu" (
  "idtamu" serial primary key NOT NULL,
  "kode_booking" varchar(20) UNIQUE NOT NULL,
  "noktp" varchar(20) UNIQUE NOT NULL,
  "nama" varchar(100) NOT NULL,
  "jk" char(1) NOT NULL,
  "no_telp" varchar(50) NOT NULL,
  "tgl_datang" DATE,
  "tgl_keluar" DATE, 
  "nokamar" VARCHAR(20) NOT NULL,
  "kode_kamar" varchar(40) NOT NULL,
  "harga" varchar(50) NOT NULL,
  "status_inap" CHAR(1) NOT NULL,
  CONSTRAINT registrasi
  FOREIGN KEY (kode_booking)
  REFERENCES registrasi (kode_booking)
  ON UPDATE CASCADE ON DELETE RESTRICT
);