create database emeneses_py;

use emeneses_py;

create table user(
	id int primary key auto_increment,
	name varchar(100),
	lastname varchar(200),
    cedula varchar(10),
    email varchar(100)
);

use emeneses_py;
select * from user;