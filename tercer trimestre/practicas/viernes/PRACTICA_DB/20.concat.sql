/*CONCAT() permite uni rvarios textos o valores en uno solo 

--vamos a unir nombre y apellido*/

SELECT CONCAT(nombre, ' ', apellido ) AS nombreCompleto
FROM usuarios;

--Muestre el usuario jonathan tiene 35 años utilizando CONCAT() 
SELECT CONCAT('El usuario ', nombre, ' tiene ', edad, ' años.') AS informacion
FROM usuarios;

--concatenar nombre apellido y correo y colocarle el alias de informacionContacto
SELECT CONCAT(nombre, ' ', apellido, ' ', email) AS informacionContacto
FROM usuarios;  

-- para remplazar un valor NULL utilizamos IFNULL()


SELECT
CONCAT(nombre, " ", IFNULL(apellido, "Sin apellido")) AS nombreCompleto
FROM Usuarios;


-- CONCAT_WS() une los valores utilizando un separador y ademas ignora valores NULL 


SELECT
CONCAT_WS('-', nombre, apellido, email) AS informacionUsuarios
FROM Usuarios;


-- Utilizar CONCAT() con UPPER() y comvertir apellido a mayusculas y colocarle el alias de nombreCompleto


SELECT 
CONCAT('-', nombre, UPPER(apellido), email) AS nombreCompleto
FROM Usuarios;