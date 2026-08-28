/* BETWEEN permite buscar valores dentri de un rango incluyendo los extremos 

ejemplo:
edad BETWEEN 20 AND 30 

esto significa que 

edad >= 20 AND  edad <= 30

--Vamos a buscar usuarios con edades entre 20 y 30 años
*/

SELECT * FROM usuarios
WHERE edad BETWEEN 20 AND 30;


-- Buscar usuarios registrados en las fechas 2020-01-01 y 2022-12-31
SELECT * FROM usuarios
WHERE fecha_nacimiento BETWEEN '2020-01-01' AND '2022-12-31';

--Buscar nombres dentro del rango alfabetico entre A y M
SELECT * FROM usuarios  
WHERE nombre BETWEEN 'A' AND 'M';

SELECT * FROM usuarios
WHERE edad NOT BETWEEN 18 AND 40;

--buscar usuarios entre 15 y 30 años ordenarlos de menor a mayor de edad
SELECT * FROM usuarios
WHERE edad BETWEEN 15 AND 30
ORDER BY edad ASC;

-- Mostrar solamente nombre y edad de los usuraios entre las edades de 15 y 20 años
SELECT nombre, edad FROM usuarios
WHERE edad BETWEEN 15 AND 20;