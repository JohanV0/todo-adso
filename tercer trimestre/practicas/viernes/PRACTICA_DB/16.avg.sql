/*La funcion AVG calcula el proemdio de una columna numerica*/
--calculamos la edad promedio de los usuarios
SELECT AVG(edad) AS edadPromedio FROM usuarios;

/*ahora ROUND redondea el resultado */
SELECT ROUND(AVG(edad)) AS edadPromedio FROM usuarios;

-- muestre el promedio con dos decimales

SELECT ROUND(AVG(edad),2) from usuarios

SELECT AVG(edad) as edadPromedio FROM usuarios WHERE edad < 30;

SELECT AVG(edad) AS edadPromediogmail FROM usuarios WHERE email LIKE '%gmail.com'