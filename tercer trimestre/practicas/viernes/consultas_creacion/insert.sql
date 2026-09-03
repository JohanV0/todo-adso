--creamos la base de datos de la empresa

CREATE DATABASE IF NOT EXISTS empresa;

USE empresa;

--insertamos un registro
CREATE TABLE usuarios(
    usuario_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100),
    edad INT,
    correo VARCHAR(100),
    fecha_registro DATE);

INSERT INTO usuarios (nombre, apellido, edad, correo, fecha_registro) VALUES 
    ('Ana','Perez', 25 ,'ana@gmail.com', '2026-07-31'),
    ('Johan','Vergara', 19 ,'johan@gmail.com', '2007-09-05');

SELECT * FROM usuarios;

DROP TABLE IF EXISTS usuarios;
