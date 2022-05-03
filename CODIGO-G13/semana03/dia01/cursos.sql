-- MySQL dump 10.13  Distrib 5.7.33, for Win64 (x86_64)
--
-- Host: localhost    Database: cursos
-- ------------------------------------------------------
-- Server version	5.7.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alumno`
--

DROP TABLE IF EXISTS `alumno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alumno` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombres` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `pais` varchar(100) DEFAULT 'Perú',
  `nota` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumno`
--

LOCK TABLES `alumno` WRITE;
/*!40000 ALTER TABLE `alumno` DISABLE KEYS */;
INSERT INTO `alumno` VALUES (1,'Ewan','Normanville','enormanville0@nationalgeographic.com','Peru',18),(2,'Carree','Baalham','cbaalham1@narod.ru','Ecuador',10),(3,'Sherwin','Krollman','skrollman2@narod.ru','Colombia',15),(4,'Zandra','Bernaldo','zbernaldo3@omniture.com','Argentina',14),(5,'Kalie','Locker','klocker4@squidoo.com','Argentina',11),(6,'Nicolina','Livingston','nlivingston5@com.com','Brazil',10),(7,'Leopold','Janik','ljanik6@spiegel.de','Brazil',11),(8,'Wilfred','Delacroux','wdelacroux7@cloudflare.com','Peru',19),(9,'Lacey','St. Ledger','lstledger8@guardian.co.uk','Brazil',11),(10,'Roarke','Andell','randell9@ft.com','Peru',20),(11,'Malvina','Ell','mella@discovery.com','Argentina',11),(12,'Brendon','Audritt','baudrittb@goo.gl','Brazil',11),(13,'Consalve','Doy','cdoyc@auda.org.au','Brazil',17),(14,'Raquel','Andrusyak','randrusyakd@noaa.gov','Colombia',18),(15,'Tobie','Cheshir','tcheshire@goo.gl','Argentina',16),(16,'Giulio','O\'Lenechan','golenechanf@cornell.edu','Colombia',12),(17,'Manya','Rivilis','mrivilisg@pcworld.com','Brazil',11),(18,'Daphne','Burley','dburleyh@forbes.com','Colombia',20),(19,'Bendicty','Fitter','bfitteri@fema.gov','Brazil',20),(20,'Alfonse','Penticoot','apenticootj@unblog.fr','Brazil',16),(21,'Sondra','Seacroft','sseacroftk@discovery.com','Brazil',11),(22,'Georgianne','Frowde','gfrowdel@godaddy.com','Brazil',11),(23,'Jaye','Macrae','jmacraem@lulu.com','Argentina',15),(24,'Dorthea','Tollady','dtolladyn@biglobe.ne.jp','Brazil',20),(25,'Irma','Marler','imarlero@si.edu','Brazil',13),(26,'Tallia','Pinsent','tpinsentp@imdb.com','Brazil',12),(27,'Patton','Bealing','pbealingq@wiley.com','Brazil',11),(28,'Garik','Borne','gborner@archive.org','Brazil',16),(29,'Tabatha','Rushsorth','trushsorths@google.ca','Colombia',14),(30,'Chrisse','Lenihan','clenihant@newsvine.com','Brazil',17),(31,'Prinz','Shee','psheeu@examiner.com','Brazil',14),(32,'Bibi','Cary','bcaryv@quantcast.com','Brazil',19),(33,'Khalil','Schwaiger','kschwaigerw@microsoft.com','Argentina',18),(34,'Dennie','Bigly','dbiglyx@wikia.com','Colombia',14),(35,'Kermy','Strauss','kstraussy@live.com','Brazil',11),(36,'Saunderson','Firebrace','sfirebracez@aboutads.info','Peru',11),(37,'Zak','Jzak','zjzak10@comsenz.com','Colombia',12),(38,'Sandie','Tripp','stripp11@geocities.com','Colombia',11),(39,'Janelle','Krook','jkrook12@sbwire.com','Brazil',19),(40,'Lavina','Leifer','lleifer13@biblegateway.com','Brazil',14),(41,'Kelvin','Coppock.','kcoppock14@oakley.com','Brazil',18),(42,'Aundrea','Tumbridge','atumbridge15@guardian.co.uk','Colombia',17),(43,'Cookie','Silverwood','csilverwood16@wikia.com','Peru',19),(44,'Elnore','Dutton','edutton17@cbsnews.com','Brazil',12),(45,'Zachariah','Georgeon','zgeorgeon18@answers.com','Peru',14),(46,'Baryram','Oley','boley19@foxnews.com','Chile',16),(47,'Dulcine','Basil','dbasil1a@canalblog.com','Argentina',10),(48,'Morgen','Giraldez','mgiraldez1b@shutterfly.com','Brazil',14),(49,'Lyn','Southcott','lsouthcott1c@example.com','Brazil',20),(50,'Lodovico','Starkey','lstarkey1d@yellowbook.com','Brazil',15),(51,'Ayn','Sollner','asollner1e@sfgate.com','Peru',18),(52,'Archy','Eagle','aeagle1f@who.int','Colombia',11),(53,'Carroll','Algar','calgar1g@mozilla.org','Peru',18),(54,'Laurena','Frankland','lfrankland1h@goo.ne.jp','Brazil',11),(55,'Joni','McKeggie','jmckeggie1i@angelfire.com','Venezuela',20),(56,'Reinaldo','Learmonth','rlearmonth1j@patch.com','Colombia',18),(57,'Chaim','Beall','cbeall1k@youku.com','Brazil',11),(58,'Care','Farncomb','cfarncomb1l@ocn.ne.jp','Brazil',12),(59,'Cornelle','Shand','cshand1m@nba.com','Chile',13),(60,'Mathe','Enevold','menevold1n@acquirethisname.com','Brazil',20),(61,'Christal','Michin','cmichin1o@miitbeian.gov.cn','Peru',12),(62,'Mohandas','McChruiter','mmcchruiter1p@mapquest.com','Argentina',19),(63,'Cirillo','Stook','cstook1q@stumbleupon.com','Brazil',12),(64,'Angelo','Milksop','amilksop1r@sourceforge.net','Argentina',20),(65,'Sarette','Denyukhin','sdenyukhin1s@wikipedia.org','Peru',19),(66,'Pris','Moulin','pmoulin1t@wordpress.org','Ecuador',15),(67,'See','Stanhope','sstanhope1u@earthlink.net','Peru',13),(68,'Karia','Lidington','klidington1v@statcounter.com','Argentina',17),(69,'Barnett','Dilrew','bdilrew1w@businessinsider.com','Argentina',13),(70,'Page','Bernardos','pbernardos1x@microsoft.com','Brazil',18),(71,'Aretha','Weed','aweed1y@indiegogo.com','Chile',12),(72,'Esmeralda','Parbrook','eparbrook1z@youtu.be','Colombia',13),(73,'Lorilyn','Trotton','ltrotton20@uiuc.edu','Brazil',15),(74,'Odella','Akred','oakred21@taobao.com','Brazil',16),(75,'Cal','Wilshaw','cwilshaw22@unblog.fr','Peru',18),(76,'Saundra','Kennan','skennan23@amazon.co.jp','Peru',14),(77,'Elsa','Gunbie','egunbie24@moonfruit.com','Colombia',15),(78,'Zebadiah','Rhyme','zrhyme25@webeden.co.uk','Brazil',20),(79,'Barbee','Langeley','blangeley26@1und1.de','Brazil',12),(80,'Wendall','Summerlee','wsummerlee27@discuz.net','Brazil',16),(81,'Harrie','Gilliland','hgilliland28@aol.com','Argentina',11),(82,'Dominic','Caren','dcaren29@time.com','Colombia',12),(83,'Alfons','De Freyne','adefreyne2a@de.vu','Argentina',13),(84,'Alvira','Lockart','alockart2b@usnews.com','Argentina',15),(85,'Blaine','Sinkinson','bsinkinson2c@seesaa.net','Brazil',17),(86,'Tuckie','Youel','tyouel2d@ucla.edu','Venezuela',19),(87,'Mendel','Ribey','mribey2e@jimdo.com','Bolivia',17),(88,'Yorker','Craik','ycraik2f@wix.com','Brazil',18),(89,'Swen','MacLachlan','smaclachlan2g@java.com','Brazil',16),(90,'Rebecka','Roughan','rroughan2h@hexun.com','Peru',10),(91,'Giulia','Brazear','gbrazear2i@youtube.com','Peru',16),(92,'Reid','Saurin','rsaurin2j@sun.com','Brazil',17),(93,'Susannah','Bilam','sbilam2k@seesaa.net','Argentina',20),(94,'Hannah','Cassey','hcassey2l@nsw.gov.au','Venezuela',11),(95,'Meggi','Getcliffe','mgetcliffe2m@yellowbook.com','Brazil',20),(96,'Xavier','Corde','xcorde2n@is.gd','Colombia',16),(97,'Vince','MacGaughy','vmacgaughy2o@devhub.com','Colombia',13),(98,'Madelin','Begbie','mbegbie2p@google.nl','Venezuela',11),(99,'Matthiew','Skeete','mskeete2q@prweb.com','Peru',11),(100,'Thane','Stubbings','tstubbings2r@dailymail.co.uk','Brazil',11);
/*!40000 ALTER TABLE `alumno` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-26 22:54:53
