/*La funcion SUM suma los valores numericos

SUM() ignora los valores NULL
*/

--sumar las edades registradas

SELECT SUM(edad) as SumaEdades FROM usuarios;

--sumar todas las edades delos usuarios mayores de edad 

SELECT SUM(edad) FROM usuarios WHERE edad >= 18

SELECT SUM(edad) FROM usuarios WHERE email LIKE '%gmail.com'

--smar las edades de los usuarios menores de 18 años 
SELECT SUM(edad) FROM usuarios WHERE edad <= 18
