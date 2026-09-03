--DELETE elimina filas de una tabla especifica no elimina la estructura de la tabla

--ahora vamos a eliminar usuarios especificos
USE empresa;
DELETE FROM usuarios WHERE usuario_id = 1

-- eliminar usuarios cuyo ID esten en la lista 

DELETE FROM usuarios WHERE usuario_id IN (8,12,13)