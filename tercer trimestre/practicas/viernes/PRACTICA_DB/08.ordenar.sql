-- ORDER BY permitw ordear los resultados de una consulta
-- ASC  ordena ASCENDENTE 
-- DESC ordena DESCENDENTE

SELECT * FROM usuarios ORDER BY edad; apellido

SELECT * from usuarios ORDER BY edad ASC;

SELECT * FROM usuarios ORDER BY edad DESC;

-- busca los usuarios con apellido perez y los ordene por edad de mayor a mejor 

SELECT * FROM usuarios WHERE apellido = 'devia' ORDER BY apellido DESC;

SELECT nombre, edad from usuarios ORDER BY edad DESC

SELECT * FROM usuarios ORDER BY nombre ASC, edad DESC;

-- muestre nombre,apellido y edad de los usuarios
-- mayores de 15 annios, ordenados por edad

SELECT 
    nombre,apellido,edad 
FROM 
    usuarios 
WHERE 
    edad > 15 
ORDER BY 
    edad ASC;
    