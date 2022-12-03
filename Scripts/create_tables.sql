CREATE TABLE `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ProductsName` varchar(45) DEFAULT NULL,
  `ProductsPrice` varchar(45) DEFAULT NULL,
  `ProductsRating` varchar(1000) DEFAULT NULL,
  `ProductsGuarentee` varchar(1000) DEFAULT NULL,
  `ProductsDelivery` varchar(1000) DEFAULT NULL,
  `ProductsUrl` varchar(1000) DEFAULT NULL,
  `ProductsBatchID` varchar(45) DEFAULT '0',
  `DateTimeInserted` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `audit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `BatchID` varchar(45) DEFAULT NULL,
  `NumberOfInserts` varchar(45) DEFAULT NULL,
  `DateTimeInserted` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
