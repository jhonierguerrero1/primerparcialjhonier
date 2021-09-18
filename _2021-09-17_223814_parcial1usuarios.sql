/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/ parcial1usuarios /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE parcial1usuarios;

DROP TABLE IF EXISTS usuarios;
CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `nombre` varchar(250) NOT NULL,
  `correo` varchar(250) NOT NULL,
  `contraseña` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
INSERT INTO usuarios(id,nombre,correo,contraseña) VALUES(1,'stiven','uh@d.com','yueti123'),(2,'juan','yueti123@gmail.com','yueti123'),(3,'pepe','12@gmail.com','yueti123'),(4,'k','aq','11'),(5,'juan','juan123@gmail.com','juan123'),(6,'lucas','lucas123@gmail.com','lucas123'),(7,'a','a','a'),(8,'w','w','w'),(9,'EE','EE','Yueti123#'),(10,'pp','pp','Yueti1237'),(11,'rr','rr','Yueti1234'),(12,'yy','yy','Yueti1234'),(13,'gg','pp','Yueti1234');