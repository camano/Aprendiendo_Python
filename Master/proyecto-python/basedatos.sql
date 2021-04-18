create database if not exists master_python;
use master_python;

create table usuarios(
id int(25) auto_increment not null,
nombre varchar(100),
apellidos varchar(255),
email varchar(255) not null,
password varchar(255)not null,
fecha date not null,
CONSTRAINT pk_usuarios primary key(id),
CONSTRAINT uq_email unique(email)
)ENGINE=InnoDb;

create table notas(
id int(25) auto_increment not null,
usuario_id int(25) not null,
titulo varchar(255)not null,
descripcion MEDIUMTEXT,
fecha date not null,
CONSTRAINT pk_nota primary key(id),
CONSTRAINT fk_nota_usuario foreign key(usuario_id) references usuarios(id)
)ENGINE=InnoDb;
