--Creamos un usuario local aparte que en este caso en admin para utilizar --
CREATE USER 'admin'@'localhost' IDENTIFIED BY '12345';

-- Le otorgamos privilegios al usuario admin--
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost';