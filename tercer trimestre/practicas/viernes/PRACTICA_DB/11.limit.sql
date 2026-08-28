--LIMIT indica cuantas lineas queremos obtener como maximo
SELECT * FROM usuarios LIMIT 3;

-- vamos a combinar limit con where

-- filtrar los usuarios mayores de 18 annios y despues limitamos el resultado a 2 filas

SELECT * FROM usuarios WHERE edad > 18 LIMIT 2;

--ahora vamos a combinar LIMIT con ORDER BY

--ordenar de mayor a menor la edad y mostrar solamente las tres primeras edades

SELECT * FROM usuarios ORDER BY edad DESC LIMIT 3;

--desplazamientto mas cantidad

--saltar los primeros 2 usuarios y mostrar los siguientes 3

SELECT * FROM usuarios LIMIT 2,3;

--OFFSE este hace lo mismo que el LIMIT este indica cuantas filas debe saltar

SELECT * FROM usuarios LIMIT 3 OFFSET 2;