-- la funcion min() y max() obtiene el valor minimo y el valor maximo , esta ignora los valores NULL

SELECT MAX(edad) FROM usuarios;

SELECT MIN(edad) FROM usuarios;

SELECT MIN(edad) as edad_minima,MAX(edad) as edad_maxima, MAX(edad) - MIN(edad) as diferencia from usuarios;

-- obtener la fecha mas antigua y la fecha mas reciente 

SELECT MAX(fechainicio) as fecha_reciente, MIN(fechainicio) as fecha_antigua from usuarios

-Obtener el primer nombre segun el abecedario
SELECT UPPER(MIN(nombre)) as primerNombre FROM usuarios;

-Obtener el ultimo nombre segun el abecedario

SELECT UPPER(MAX(nombre)) as primerNombre FROM usuarios;

--obtener el nombre alfabetico menor y que devuelva la primera fila completa con MIN()

SELECT * FROM usuarios WHERE nombre = ( SELECT MIN(nombre) FROM usuarios)

--obtener el nombre alfabetico mayor y que devuelva la primera fila completa con MAX()

SELECT * FROM usuarios WHERE nombre = ( SELECT MAX(nombre) FROM usuarios)

-- obtener la menor edad entre los usuarios mayores a 18

SELECT MIN(edad) edadMinimaDeEdadMInima FROM usuarios WHERE edad > 18

--obtener el mayor de edad entre los ususarios que tiene un correo registrado

SELECT MAX(edad) as edadMaxima FROM usuarios WHERE email IS NOT NULL;

--obtener el usuario mas joven

SELECT * FROM usuarios WHERE edad = (SELECT MIN(edad) FROM usuarios);

-- encontrar el usuario mayor
SELECT * FROM usuarios WHERE edad = (SELECT MAX(edad) FROM usuarios);
