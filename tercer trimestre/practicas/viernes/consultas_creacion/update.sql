--para modificar un registro
USE empresa;
DESCRIBE usuarios;
SELECT * FROM usuarios;

--vamos a modificar la edad de ana con usuarios_id = 1
-- el WHERE evita modificar a los demas usuarios si existieran
UPDATE usuarios SET edad = 26 WHERE usuario_id = 1

-- verificamos unicamente el usuario modificado

SELECT * FROM usuarios WHERE usuario_id = 1

--modificamos varias columnas 
--  set permite cambiar varias columnas en una misma linea
UPDATE usuarios SET edad = 27, correo = 'ana.nuevo@gmail.com' WHERE usuario_id = 1

-- vamos a modificar utilizando otra clomuna lo podemos hacer utilizando con el correo

UPDATE usuarios SET apellido = 'rodriguez' WHERE correo = 'johan@gmail.com'