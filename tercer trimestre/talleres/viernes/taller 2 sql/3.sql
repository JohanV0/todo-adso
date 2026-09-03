DROP DATABASE IF EXISTS cafe_tolima;

CREATE DATABASE cafe_tolima
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_spanish_ci;

GRANT ALL PRIVILEGES ON cafe_tolima. * TO 'cafe_admin'@'localhost';
FLUSH PRIVILEGES;

SHOW GRANTS FOR 'cafe_admin'@'localhost';