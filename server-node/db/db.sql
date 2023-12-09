CREATE TABLE multas (
  id INT PRIMARY KEY AUTO_INCREMENT,
  placa VARCHAR(10) NOT NULL,
  motivo VARCHAR(255) NOT NULL,
  fecha_hora_infraccion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  correo VARCHAR(255) NOT NULL
  FOREIGN KEY (placa) REFERENCES propietario(placa)

);

CREATE TABLE PROPIETARIO (
  nombre VARCHAR(255) NOT NULL,
  correo VARCHAR(255) NOT NULL,
  placa VARCHAR(10) NOT NULL

);

ALTER TABLE multas ADD FOREIGN KEY (placa) REFERENCES propietario(placa);

CREATE TABLE registro_consultas (
  id INT PRIMARY KEY AUTO_INCREMENT,
  placa VARCHAR(10) NOT NULL,
  fecha_consulta TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (placa) REFERENCES propietario(placa)
);