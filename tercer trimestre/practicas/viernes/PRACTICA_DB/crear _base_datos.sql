--creamos la base de datos y utilizamos los parametros para que reconozca los caracteres especiales--
mysql> CREATE DATABASE IF NOT EXISTS hello_mysql
    -> CHARACTER SET utf8mb4
    -> COLLATE utf8mb4_spanish_ci;

--ahora camos a utilizar la base de datos recien creada que fue hello_mysql--
use hello_mysql

create table user(
    id_user VARCHAR(30) not null primary key,
    nombre VARCHAR(30) not null,
    apellido VARCHAR(40) null,
    edad TINYINT(3)null,
    fecha DATE null);
--mostramos la tabla que creamos, en este caso la tabla user--
describe user;
describe table user;
--el comando es para saber que datos tiene la tabla en este casi esta vacia--


--limpiar la tabla por si tiene datos previos--
DELETE  FROM user;

INSERT INTO user(id_user,nombre,apellido,edad,fecha) values 
('1','johan','vergara',18,'2007-09-05'),
('2','anne','hernandez',17,'2009-02-03'),
('3','nicolas','vazquez',18,'2007-07-05');

SELECT * FROM user;

--verificamos cuantos usuarios hay en la tabla en este caso deveria devolver 3--
SELECT COUNT(*) AS total_usuarios FROM user;
    