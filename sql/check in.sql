-- ----------------------------
-- Table structure for registrasi
-- ----------------------------
DROP TABLE IF EXISTS "public"."registrasi";
CREATE TABLE "public"."registrasi" (
  "idregistrasi" serial primary key NOT NULL,
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
  "status_inap" CHAR(1) NOT NULL
);