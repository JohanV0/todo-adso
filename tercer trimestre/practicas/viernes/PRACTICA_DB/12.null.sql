--NULL representa ausencia de valor

/*NULL no signica 
0
''

false

para comprobar NULL No utilizamos 

= NULL
<> NULL

lo que utilizamos es 

IS NULL
IS NOT NULL

*/

SELECT * FROM usuarios WHERE email IS NULL;
SELECT * FROM usuarios WHERE email IS NOT NULL;

--combines a IS NOT NULL mas AND
--mostrar los usuarios que tiene correo y ademas tienen 15 años 

SELECT * FROM usuarios WHERE email is not null and edad = 18

--vamos a contar los valores NULL

--cuente los valores que no tienen correo 
SELECT COUNT(*) as usuario_sin_correo FROM usuarios WHERE email IS NULL

SELECT * FROM usuarios

--cuente los usuarios que si tienen correo
SELECT COUNT(*) as usuario_sin_correo FROM usuarios WHERE email IS NOT NULL

--ahora veremos IFNULL

-- si el valor no es NULL el devuelve el valor original
--si el valor es NULL devuelve el valor por defecto

--si edad es NULL, mostrar 0

SELECT IFNULL(edad,0) as edad from usuariosa

--si el email es NULL mostrar un mensaje que diga sin correo registrado

SElect IFNULL(email,'sin correo registrado') as correo from usuarios

-- si fechaInicio es NULL, muestre la fecha indicada
SELECT nombre,IFNULL(fechaInicio,'2026-01-01') FROM usuarios;

-- convertir a masyusculas utilizando UPPER y si es NULL muestra 'SIN APELLIDO'

SELECT UPPER(nombre), UPPER(IFNULL(apellido,'SIN APELLIDO')) as NuevoApellido FROM usuarios

-- mostrar nombre y edad. Si edad es NULL, mostrar 0

SELECT nombre,IFNULL(edad,0) as edad_modificada FROM usuarios