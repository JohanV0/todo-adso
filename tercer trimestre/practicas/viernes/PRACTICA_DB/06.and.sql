/*operadores logicos permiten combinar condiciones dentro del WHERE
    AND todas las condiciones se deben cumplir 
    OR almenos una condicion se debe cumplir
    NOT niega una condicion 
*/

--vamos a mostrar los usuarios cuyo correo no sea el indicado

SELECT * FROM usuarios WHERE NOT email = 'saraandreade@gmail.com'

SELECT * FROM usuarios WHERE NOT email <> 'saraandreade@gmail.com'

--mostrar con la condicion AND que edad = 15 y el correo diferente de sara@gmail.com
SELECT * FROM usuarios WHERE edad = 18 AND email <> 'saraandreade@gmail.com'

-- buscar usuarios menores de 20 annios que tengan correo o Outlook utilizando AND y OR

SELECT * FROM usuarios WHERE edad < 20 and email LIKE '%gmail.com' OR '$outlook.com'

--mostrar usuarios cuya edad estre entre 15 y 30 años. Utilizando And

SELECT * FROM usuarios WHERE edad > 15 and edad < 30