create database Cadastro_comentarios;

USE Cadastro_comentarios;


create table  tb_comentarios(
 data_hora datetime not null ,
 nome  varchar(50) not null ,
comentario TEXT not null ,
codigo_coment int primary key auto_increment
 ); 
