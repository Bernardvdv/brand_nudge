CREATE TABLE `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ProductsName` varchar(45) DEFAULT NULL,
  `ProductsPrice` varchar(45) DEFAULT NULL,
  `ProductsRating` varchar(1000) DEFAULT NULL,
  `ProductsGuarentee` varchar(1000) DEFAULT NULL,
  `ProductsDelivery` varchar(1000) DEFAULT NULL,
  `ProductsUrl` varchar(1000) DEFAULT NULL,
  `DateTimeInserted` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4;
