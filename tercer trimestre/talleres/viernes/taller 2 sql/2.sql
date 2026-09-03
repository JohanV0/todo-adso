CREATE USER 'cafe_admin'@'localhost' IDENTIFIED BY 'Cafe2024*';


SELECT user, HOST FROM mysql.user WHERE user = 'cafe_admin';

SELECT USER()