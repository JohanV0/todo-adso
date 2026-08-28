/* la sentencia COUNT() permite contar filas o valores

tenemos tres formas principales:

COUNT(*)
Cuenta todas las filas 

COUNT(Columna)
Cuenta los valores que no sean NULL

COUNT(DISTINCT columna)
Cuenta los valores diferentes y que no sean NULL
*/


-- cuenta todos los usuarios
SELECT COUNT(*) AS totalUsuarios FROM usuarios;

SELECT COUNT (DISTINCT edad) AS edadesDiferentes FROM usuarios;

--cuenta cuantas edades diferentes existen
-- los NULL no se encuentran

SELECT COUNT(DISTINCT edad) as edadesDiferentes FROM usuarios;

--cuente los usuarios que tienen correo gmail
SELECT COUNT(email) AS totalCorreos FROM usuarios;
SELECT COUNT(*) as usuariosGmail FROM usuarios WHERE email LIKE '%gmail.com'

--cuentes los usuarios con edad de 18 años o mas

SELECT COUNT(*) FROM usuarios WHERE edad >= 18

--cuente los usuarios cuyo correo es NULL

SELECT COUNT(*) FROM usuarios WHERE email IS NULL

--compare los 3 tipos de COUNT con el correo

SELECT COUNT(*) as totalUsuarios, COUNT(email) as usuariosEmail,COUNT(DISTINCT email) as usuariosDiferentes  FROM usuarios 

--utilizar COUNT y DISTINC y cuente los apellidos diferentes 
-- los NULL no se cuentan 

SELECT COUNT(DISTINCT apellido) as apellidoDiferentes FROM usuarios;