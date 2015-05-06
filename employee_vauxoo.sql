-- Your sql code in this file
-- NOTE: Please, don't add sentence to create database in this script file.
--       You can create database locally to test it.
--       Consider add ';' at end sentence.

--creacion de la tabla departmentos
 create table employee_department(
 id serial,
 name varchar(20) not null,
 description varchar(20),
 primary key(id));
 

---creamos la tabla employee_hobby
create table employee_hobby(
id serial,
name varchar(20),
description varchar(20),
primary key(id));

primary key(id));


 --creacion de la tabla empleados
 create table employee(
 id serial,
 name varchar(20) not null,
 description varchar(20),
 --id_hobby smallint references employee_hobby(id) not null,
 id_department smallint references employee_department(id) not null,
 name_jefe varchar(10) unique not null,
 primary key(id));


create table otra(
    id1 serial,
    id2 serial
 );

 --insertar departmentos
 insert into employee_department(name) values ('compras');
 insert into employee_department(name) values ('ventas');
 insert into employee_department(name) values ('contabilidad');
 insert into employee_department(name) values ('produccion');
 insert into employee_department(name) values ('desarrollo');
 insert into employee_department(name) values ('sqa');

 
 --insertar los hobbys
insert into employee_hobby(name) values('jugar');
insert into employee_hobby(name) values('leer');
insert into employee_hobby(name) values('caminar');


--insertar empleados
 insert into employee(name,id_department,name_jefe) values('jose',1,'javier');
 insert into employee(name,id_department,name_jefe) values('jesus',2,'mendoza');
 insert into employee(name,id_department,name_jefe) values('juan',3,'alexis');
 insert into employee(name,id_department,name_jefe) values('janh',3,'pablo');
 


