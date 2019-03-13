-- MySQL dump 10.13  Distrib 5.7.20, for Linux (x86_64)
--
-- Host: localhost    Database: spider_result
-- ------------------------------------------------------
-- Server version	5.7.20

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
-- Table structure for table `google_play`
--

DROP TABLE IF EXISTS `google_play`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `google_play` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `packageName` varchar(1000) NOT NULL DEFAULT '' COMMENT 'app唯一标识（包名）',
  `detail` text NOT NULL COMMENT '详细内容，json字符串',
  `need_purchased` tinyint(4) NOT NULL DEFAULT '0' COMMENT '0表示不需要购买，1表示需要购买',
  `done` tinyint(4) NOT NULL DEFAULT '0' COMMENT '0表示未下载，1表示已下载',
  `file_result` varchar(2000) NOT NULL DEFAULT '' COMMENT '文件下载结果',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49676 DEFAULT CHARSET=utf8 COMMENT='google play网站上的app';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `koodous`
--

DROP TABLE IF EXISTS `koodous`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `koodous` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `crawl_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '爬取时间',
  `tag` varchar(50) NOT NULL DEFAULT '' COMMENT '标签值',
  `source_url` varchar(1000) NOT NULL DEFAULT '' COMMENT '源url',
  `sha256` varchar(1000) NOT NULL DEFAULT '' COMMENT 'app的sha256值',
  `detail` text NOT NULL COMMENT '详细内容，json字符串',
  `done` tinyint(4) NOT NULL DEFAULT '0' COMMENT '0表示未下载，1表示已下载',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28724 DEFAULT CHARSET=utf8 COMMENT='koodous网站上的app';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `koodous_apps`
--

DROP TABLE IF EXISTS `koodous_apps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `koodous_apps` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `crawl_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '爬取时间',
  `tag` varchar(50) NOT NULL DEFAULT '' COMMENT '标签值',
  `source_url` varchar(1000) NOT NULL DEFAULT '' COMMENT '源url',
  `sha256` varchar(1000) NOT NULL DEFAULT '' COMMENT 'app的sha256值',
  `detail` text NOT NULL COMMENT '详细内容，json字符串',
  `file_url` varchar(1000) NOT NULL DEFAULT '' COMMENT 'app下载url',
  `file_result` varchar(2000) NOT NULL DEFAULT '' COMMENT '文件下载结果',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39231 DEFAULT CHARSET=utf8 COMMENT='koodous网站上的app';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-15  6:51:21
