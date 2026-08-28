/* el operador IN permite comprobar si un valor pertenece a una lista 
en ves de escribir
WHERE nombre = 'sara' OR nombre = 'Johanthan'
podemos escribir}:
WHERE nombre IN('sara','Jonathan')

el NOT IN hace lo contrario*/

-- BUscar ususarios cuyo apellido este en la lista 

SELECT * FROM usuarios WHERE apellido IN ('perez','lopez','castro')}

SELECT * FROM usuarios WHERE edad IN(18,15,20)

--buscamos usuarios cuya edad no sea 15 ni 42

SELECT * FROM usuarios WHERE edad NOT IN(18,40)

--Muestre los usuarios cuya edad sea 15 o 18 
--incluyendo los que no tengan edad registrada

--IN no sirve para buscar NULL
