--crear una base de datos llamada empresa
CREATE DATABASE empresa;

--esta sentencia solo crea una base de datos si todavia no existe COMMENT
CREATE DATABASE IF NOT EXISTS empresa
CHARACTER SET utf8mb4
COLLATE utf8mb4_spanish_ci;

--mostramos una base de datos del servidor

SHOW DATABASES;

--cambiamos la base de datos de mi base a la base de datos empresa

USE empresa;

--muestra la base de datos que esta utilizando
SELECT DATABASE() AS base_datos_actual;
