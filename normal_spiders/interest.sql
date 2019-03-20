/*
Navicat MySQL Data Transfer

Source Server         : Amazon
Source Server Version : 50725
Source Host           : localhost:3306
Source Database       : interest

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-03-20 14:20:32
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for bank_crawl_result
-- ----------------------------
DROP TABLE IF EXISTS `bank_crawl_result`;
CREATE TABLE `bank_crawl_result` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键自增ID',
  `crawl_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '爬取时间',
  `bank_name` varchar(255) NOT NULL COMMENT '爬取银行名称，示例：中国农业银行',
  `source_url` varchar(1000) NOT NULL COMMENT '爬取请求URL',
  `response` text NOT NULL COMMENT '爬取得到的响应Json字符串',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8 COMMENT='从银行网站找到的数据请求接口，爬取结果存储表。';

-- ----------------------------
-- Table structure for bank_info
-- ----------------------------
DROP TABLE IF EXISTS `bank_info`;
CREATE TABLE `bank_info` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键自增ID',
  `bank_crawl_result_id` bigint(20) NOT NULL COMMENT '银行爬取结果表主键ID',
  `bank_name` varchar(255) NOT NULL COMMENT '爬取银行名称，示例：abchina',
  `rmb_gold_customer_sell` decimal(10,2) NOT NULL COMMENT '人民币账户黄金用户卖出价格',
  `rmb_gold_update_beijing_time` datetime NOT NULL COMMENT '人民币账户黄金更新北京时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8 COMMENT='银行数据详情，目前只处理并保存了人民币黄金卖出价格。';

-- ----------------------------
-- Table structure for buy_info
-- ----------------------------
DROP TABLE IF EXISTS `buy_info`;
CREATE TABLE `buy_info` (
  `id` bigint(20) NOT NULL COMMENT '主键自增ID',
  `bank_name` varchar(255) NOT NULL COMMENT '银行名称',
  `product` varchar(255) NOT NULL COMMENT '产品名称',
  `price` decimal(10,2) NOT NULL COMMENT '价格',
  `quantity` bigint(20) NOT NULL COMMENT '数量',
  `time` datetime NOT NULL COMMENT '时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='购买记录。';

-- ----------------------------
-- Table structure for fund_info
-- ----------------------------
DROP TABLE IF EXISTS `fund_info`;
CREATE TABLE `fund_info` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键自增ID',
  `fund_name` varchar(255) NOT NULL COMMENT '爬取基金公司名称，示例：yhfund',
  `fund_code` varchar(255) NOT NULL COMMENT '基金代码，示例：000286',
  `time` date NOT NULL COMMENT '日期',
  `IOPV` decimal(10,3) NOT NULL COMMENT '单位净值',
  `LJJZ` decimal(10,3) NOT NULL COMMENT '累计净值',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1321 DEFAULT CHARSET=utf8 COMMENT='基金数据详情，目前只处理并保存了银华信用季季红债券A(基金代码：000286)的单位净值和累计净值。';
