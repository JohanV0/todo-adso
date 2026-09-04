USE cafe_tolima;
CREATE TABLE sucursal(
    codigo_sucursal INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(80) NOT NULL,
    direccion VARCHAR(150) NOT NULL,
    ciudad VARCHAR(60) NOT NULL,
    telefono VARCHAR(20) NULL,
    fecha_apertura DATE NOT NULL,
    activa BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE categoria(
    id_categoria INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    descripcion VARCHAR(150) NULL
);

CREATE TABLE cliente(
    cedula CHAR(10) NOT NULL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NULL,
    correo VARCHAR(100) NULL,
    telefono VARCHAR(20) NULL,
    fecha_registro DATE NOT NULL,
    puntos INT NOT NULL DEFAULT 0
);

CREATE TABLE proveedor(
    nit VARCHAR(15) PRIMARY KEY,
    razon_social VARCHAR(100) NOT NULL,
    direccion VARCHAR(150) NULL,
    ciudad VARCHAR(60) NULL,
    telefono VARCHAR(20) NULL,
    correo VARCHAR(100) NULL,
    contacto_principal VARCHAR(100) NULL
);

CREATE TABLE insumo(
    codigo_insumo INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(80) NOT NULL,
    unidad_medida VARCHAR(10) NOT NULL,
    stock_actual DECIMAL (10,2) NOT NULL DEFAULT 0,
    stock_minimo DECIMAL(10,2) NOT NULL DEFAULT 0,
    stock_maximo DECIMAL(10,2) NOT NULL DEFAULT 0
);

SHOW TABLES;

CREATE TABLE producto(
    codigo_producto INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(200) NULL,
    precio_venta DECIMAL(10,2) NOT NULL,
    calorias INT NULL,
    id_categoria INT NOT NULL,
    CONSTRAINT producto_categoria 
        Foreign Key (id_categoria) 
        REFERENCES categoria(id_categoria),
    activo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE empleado(
    cedula CHAR(10) PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    direccion VARCHAR(150) NULL,
    telefono VARCHAR(20) NULL,
    fecha_nacimiento DATE NULL,
    fecha_ingreso DATE NOT NULL,
    sueldo_base DECIMAL (10,2) NOT NULL, CONSTRAINT chk_empleado_tipo CHECK (sueldo_base = 1300000),
    tipo_empleado VARCHAR(20) NOT NULL CONSTRAINT chk_empleado_sueldo CHECK (tipo_empleado IN ('BARISTA','MESERO','ADMINISTRATIVO')),
    codigo_sucursal INT NOT NULL,
        CONSTRAINT empleado_sucursal
            Foreign Key (codigo_sucursal) 
            REFERENCES sucursal(codigo_sucursal),
    activo BOOLEAN NOT NULL DEFAULT TRUE
);

#punto 7
CREATE TABLE pedido (
    numero_pedido INT PRIMARY KEY AUTO_INCREMENT,
    fecha_hora DATETIME NOT NULL,
    codigo_sucursal INT NOT NULL
        CONSTRAINT pedido_sucursal
            Foreign Key (codigo_sucursal) 
            REFERENCES sucursal(codigo_sucursal),
    cedula_mesero CHAR(10) NOT NULL,
        CONSTRAINT pedido_mesero
            Foreign Key (cedula_mesero) 
            REFERENCES empleado(cedula),
    cedula_cliente CHAR(10) NULL (FK a cliente puede ser NULL en pedidos anónimos),
    total DECIMAL(12,2) NOT NULL DEFAULT 0,
    metodo_pago VARCHAR(20) NULL
);
