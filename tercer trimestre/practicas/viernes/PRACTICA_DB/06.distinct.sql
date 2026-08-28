/*DISTINCT elimina los valores o combinaciones repetidas del resultado de una consulta*/


use miBase;

SELECT DISTINCT edad from usuarios; -- muestra la edad una sola vez

SELECT DISTINCT apellido from usuarios;

SELECT DISTINCT nombre,edad from usuarios;
