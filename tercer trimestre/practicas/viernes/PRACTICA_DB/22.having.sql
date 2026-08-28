-- HAVING perimite filtrar los grupos creados mediante GROUP BY

-- la diferencia principal es
-- WHERE filtra registros Antes de agrupar 
-- HAVING filtra grupos despues de agrupar

-- vamos a mostrar las edades que tienen mas de un usuario

SELECT edad, 
COUNT(*) AS cantidadUsuarios 
FROM Usuarios
GROUP BY edad 
HAVING COUNT(*) > 1 --Este solo conserva los grupos que tiene mas de un usuario

-- filtrar los usuarios mayores de 15 años y luego filtrar los grupos que tengan mas de un usuario aplicando WHERE y HAVING
SELECT edad, COUNT(*) AS cantidadUsuarios 
FROM Usuarios
WHERE edad > 15
GROUP BY edad
HAVING COUNT(*) > 1;