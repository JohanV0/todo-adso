
--1.--
mysql> CREATE DATABASE IF NOT EXISTS cafeteria_sena
    -> CHARACTER SET utf8mb4
    -> COLLATE utf8mb4_spanish_ci;
Query OK, 1 row affected (0,02 sec)

--2.--
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| cafeteria_sena     |
| hello_mysql        |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0,01 sec)

--3.--
mysql> use cafeteria_sena
Database changed
mysql> select database();
+----------------+
| database()     |
+----------------+
| cafeteria_sena |
+----------------+
1 row in set (0,01 sec)

--4.--
mysql> create table productos(
    ->     producto_id int not null primary key auto_increment,
    ->     nombre varchar(100)not null,
    ->     categoria varchar(50) not null,
    ->     precio decimal(10,2)not null,
    ->     stock int null,
    ->     fecha_registro date null);
Query OK, 0 rows affected (0,08 sec)

--5.--
mysql> describe productos;
+----------------+---------------+------+-----+---------+----------------+
| Field          | Type          | Null | Key | Default | Extra          |
+----------------+---------------+------+-----+---------+----------------+
| producto_id    | int           | NO   | PRI | NULL    | auto_increment |
| nombre         | varchar(100)  | NO   |     | NULL    |                |
| categoria      | varchar(50)   | NO   |     | NULL    |                |
| precio         | decimal(10,2) | NO   |     | NULL    |                |
| stock          | int           | YES  |     | NULL    |                |
| fecha_registro | date          | YES  |     | NULL    |                |
+----------------+---------------+------+-----+---------+----------------+
6 rows in set (0,01 sec)
--6.--
mysql> show tables;
+--------------------------+
| Tables_in_cafeteria_sena |
+--------------------------+
| productos                |
+--------------------------+
1 row in set (0,00 sec)
--7.--
mysql> create table clientes(
    -> cliente_id int not null primary key auto_increment,
    -> nombre varchar(50) not null,
    -> apellido varchar(50) not null, 
    -> correo varchar(100) null,
    -> telefono varchar(20) null,
    -> fecha_registro date not null);
Query OK, 0 rows affected (0,07 sec)

mysql> show tables;
+--------------------------+
| Tables_in_cafeteria_sena |
+--------------------------+
| clientes                 |
| productos                |
+--------------------------+
2 rows in set (0,00 sec)

--8.--
mysql> insert into productos(nombre,categoria,precio,stock,fecha_registro) values ('Café tinto', 'Bebida caliente', 1500, 100, '2025-02-01');
Query OK, 1 row affected (0,02 sec)

+-------------+-------------+-----------------+---------+-------+----------------+
| producto_id | nombre      | categoria       | precio  | stock | fecha_registro |
+-------------+-------------+-----------------+---------+-------+----------------+
|           1 | Café tinto  | Bebida caliente | 1500.00 |   100 | 2025-02-01     |
+-------------+-------------+-----------------+---------+-------+----------------+
1 row in set (0,00 sec)

--9.--
mysql> INSERT INTO productos(nombre,categoria,precio,stock,fecha_registro) values 
    -> ('Aromática de frutas', 'Bebida caliente', 1800, 80, '2025-02-01'),
    -> ('Empanada de pollo', 'Comida', 2500, 50,'2025-02-01'),
    -> ('Arepa con queso', 'Comida', 3000, 40, '2025-02-01'),
    -> ('Jugo de mora Bebida', 'fría', 3500, 30,'2025-02-01');
Query OK, 4 rows affected (0,03 sec)
Records: 4  Duplicates: 0  Warnings: 0

--10.--
mysql> INSERT INTO productos(nombre,categoria,precio,fecha_registro) values 
    -> ('Galleta artesanal', 'Snack', 1800,'2025-02-05'),
    -> ('Sanduche mixto', 'Comida', 5000,'2025-02-05');
Query OK, 2 rows affected (0,02 sec)
Records: 2  Duplicates: 0  Warnings: 0;

--11.--
mysql> INSERT INTO clientes(nombre,apellido,correo,telefono,fecha_registro) values 
    -> ('Maria', 'Gomez','maria.gomez@sena.edu.co','3001234567', '2025-02-01'),
    -> ('Andres', 'Ramirez',NULL,'3109876543','2025-02-02'),
    -> ('Laura', 'Torres','laura.torres@sena.edu.co ',NULL, '2025-02-03'),
    -> ('Carlos', 'Perilla','carlos.p@sena.edu.co ','3155551122', '2025-02-04'),
    -> ('Sofía ', 'Vargas ','sofia.vargas@sena.edu.co ','3208889900 ', '2025-02-05');
Query OK, 5 rows affected (0,02 sec)
Records: 5  Duplicates: 0  Warnings: 0

--12.--
mysql> select * from productos;
+-------------+----------------------+-----------------+---------+-------+----------------+
| producto_id | nombre               | categoria       | precio  | stock | fecha_registro |
+-------------+----------------------+-----------------+---------+-------+----------------+
|           1 | Café tinto           | Bebida caliente | 1500.00 |   100 | 2025-02-01     |
|           2 | Aromática de frutas  | Bebida caliente | 1800.00 |    80 | 2025-02-01     |
|           3 | Empanada de pollo    | Comida          | 2500.00 |    50 | 2025-02-01     |
|           4 | Arepa con queso      | Comida          | 3000.00 |    40 | 2025-02-01     |
|           5 | Jugo de mora Bebida  | fría            | 3500.00 |    30 | 2025-02-01     |
|           6 | Galleta artesanal    | Snack           | 1800.00 |  NULL | 2025-02-05     |
|           7 | Sanduche mixto       | Comida          | 5000.00 |  NULL | 2025-02-05     |
+-------------+----------------------+-----------------+---------+-------+----------------+
7 rows in set (0,00 sec)

--13.--
mysql> SELECT COUNT(*) AS total_productos FROM productos;
+-----------------+
| total_productos |
+-----------------+
|               7 |
+-----------------+
1 row in set (0,00 sec)

--14.--
mysql> select * from clientes;
+------------+---------+----------+---------------------------+-------------+----------------+
| cliente_id | nombre  | apellido | correo                    | telefono    | fecha_registro |
+------------+---------+----------+---------------------------+-------------+----------------+
|          1 | Maria   | Gomez    | maria.gomez@sena.edu.co   | 3001234567  | 2025-02-01     |
|          2 | Andres  | Ramirez  | NULL                      | 3109876543  | 2025-02-02     |
|          3 | Laura   | Torres   | laura.torres@sena.edu.co  | NULL        | 2025-02-03     |
|          4 | Carlos  | Perilla  | carlos.p@sena.edu.co      | 3155551122  | 2025-02-04     |
|          5 | Sofía   | Vargas   | sofia.vargas@sena.edu.co  | 3208889900  | 2025-02-05     |
+------------+---------+----------+---------------------------+-------------+----------------+
5 rows in set (0,00 sec)

--15.--
mysql> create table empleados_cefeteria(
    -> empleado_id int not null primary key auto_increment,
    -> documento varchar(15) not null,
    -> nombre_completo varchar(150) not null,
    -> cargo varchar(50) default 'auxiliar',
    -> salario decimal(10,2) not null,
    -> fecha_ingreso date not null);
Query OK, 0 rows affected (0,08 sec)

mysql> SELECT * FROM empleados_cefeteria;
+-------------+------------+----------------------+----------------+------------+---------------+
| empleado_id | documento  | nombre_completo      | cargo          | salario    | fecha_ingreso |
+-------------+------------+----------------------+----------------+------------+---------------+
|           1 | 1105678901 | Marta Cecilia Ruiz   | Administradora | 2500000.00 | 2024-01-15    |
|           2 | 1023456789 | Jorge Iván Molina    | auxiliar       | 1400000.00 | 2024-06-01    |
|           3 | 1006789012 | Sandra Milena Ospina | Cajera         | 1600000.00 | 2025-01-20    |
+-------------+------------+----------------------+----------------+------------+---------------+
3 rows in set (0,00 sec)

mysql> show tables;
+--------------------------+
| Tables_in_cafeteria_sena |
+--------------------------+
| clientes                 |
| empleados_cefeteria      |
| productos                |
+--------------------------+
3 rows in set (0,01 sec)

