-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS users;
CREATE TABLE users(
  "iduser" serial primary key,
  "username" varchar(100) unique not null,
  "password" varchar(100) not null,
  "rolename" varchar(100) not null
);

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO users(username,password,rolename)values('admin',MD5('123'),'admin');
INSERT INTO users(username,password,rolename)values('operator',MD5('123'),'operator');