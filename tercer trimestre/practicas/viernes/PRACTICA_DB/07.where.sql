/*WHERE permite filtrar las filas que cumplen una condicion

para esto debemos saber que tambien exissten los operadores de comparacion

= igualdad 
<> diferente
!= diferente 
> mayor que 
< menor que 
>= mayor o igual que
<= menor o igual que 
*/

SELECT * FROM usuarios;
use miBase;
SELECT * from usuarios WHERE edad = 15; -- muestra todos los valores donde la columna de edad tenga un valor igual a 15

SELECT nombre from usuarios WHERE edad = 15; -- muestra solo los nombres donde la columna de edad sea igual a 15+

SELECT DISTINCT nombre from usuarios WHERE edad = 15; -- muestra solo los nombres donde la columna de edad sea igual a 15, aca estamos combinando DISTINCT y WHERE
SELECT DISTINCT * from usuarios WHERE edad > 20; -- muestra solo los nombres donde la columna de edad sea igual a 15, aca estamos combinando DISTINCT y WHERE

SELECT  * from usuarios WHERE nombre = 'sara'

SELECT * from usuarios WHERE nombre <> 'perez'

SELECT * from usuarios WHERE fechainicio >= '2020-01-01'