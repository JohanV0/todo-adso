/*LIKE permite buscar textos utilizando patrone
esto es util para buscar:

1.texto que empiece con algo
2. texto que termine con algo
*/

--Buscar los correos que terminen con gmail.com

SELECT * FROM usuarios WHERE email LIKE '%gmail.com';

--ahora buscamos lo nombres que comiencen con la letra S

SELECT * FROM usuarios WHERE nombre LIKE 's%';

--buscamos nombres que contengan la letra 'a'

SELECT * FROM usuarios WHERE nombre LIKE '%a%';

--buscamos nombres que contengan exactamente 4 caracteres

SELECT * FROM usuarios WHERE nombre LIKE '____';

-- buscamos los nombres que comiencen por la letra s y que contengan exactamente 4 caracteres

SELECT * FROM usuarios WHERE nombre LIKE 's___';
SELECT * FROM usuarios WHERE nombre LIKE 's%' AND nombre LIKE '____'

--buscamos correo que no trminen en gmail.com

SELECT * FROM usuarios WHERE email NOT LIKE '%gmail.com';

-- buscar apellido que contenga la letra 'e' en cualquier posicion

SELECT * FROM usuarios WHERE apellido LIKE '%e%';
