/* Un alias es un nombre temporal que le asignamos a una columna o tabla 
el alias no modifica la base de datos
solo el nombre mostrado en el resultado 
*/

-- cambiemos temporalmente el nombre de la columna 

SELECT nombre AS nombreUsuarios FROM Usuarios;

-- asigne o cambie el nombre por nombreUsuario, apellido por apellidoUsuari y edad por edadUsuarios

SELECT nombre AS nombreUsuario, apellido AS apellidoUsuario, edad AS edadUsuario FROM Usuarios;

-- Asigna un nombre al resultado de MAX()

SELECT 
MAX(edad) AS edadMaxima 
FROM Usuarios;

--Alias con textos descriptivos para eso utilizamos los backticks(´) estos perimiten utilizar espacio en el alias

--Son utiles cuando el resultado sera presentado directament a un usuario

SELECT
    nombre AS `Nombre del usuarios`,
    apellido AS `Apellido del usuario`,
    edad AS `Edad del usuarios`
FROM
Usuarios;

-- podemos asiganarle un ALIAS a una tabla 
-- Esto es util cuando utilizamos varias tablas cuando estamos consultando una sola no es tan productivo
SELECT 
u.nombre, 
u.email, 
u.edad
FROM Usuarios AS u; 

--Cuente los usuarios y llame al resultado totalUsuarios

SELECT
COUNT(*) AS TotalUsuarios
FROM Usuarios;

-- utilice "u" como alias de usuarios y muestre nombre, edad, y email

SELECT 
u.nombre, 
u.edad, 
u.email
FROM usuarios AS u; 

-- utilice "u" como alias y muestre los usuraios mayores de 18 años

SELECT
u.nombre,
u.edad
FROM Usuarios AS u
WHERE u.edad > 18;