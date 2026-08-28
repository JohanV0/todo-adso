-- GROUP BY agrupa reguistros que tienen el mismo valor se utiliza principalmente junto con funciones de agregacion como:

--COUNT() que cuenta regirstros
--SUM() 
--AVG()
--MIN()
--MAX()

--Vamos a mostrar cuantos usuarios existen para cada edad

SELECT edad, COUNT(*) AS cantidadUsuarios FROM usuarios GROUP BY edad;

--Agrupar y ordenar las edades de menor a mayor utilizando COUNT() y  colocando el alias de cantidadUsuarios
SELECT edad, COUNT(*) AS cantidadUsuarios 
FROM usuarios GROUP BY edad ORDER BY edad ASC;

-- Mostrar el promedio de edad por apellido utilizando GROUP BY y colocando el alias de edadPromedio
SELECT apellido, AVG(edad) AS edadPromedio
FROM usuarios GROUP BY apellido;