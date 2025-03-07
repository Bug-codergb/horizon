/*
 Navicat Premium Dump SQL

 Source Server         : PythonMySQL
 Source Server Type    : MySQL
 Source Server Version : 80040 (8.0.40)
 Source Host           : localhost:3306
 Source Schema         : horizon_db

 Target Server Type    : MySQL
 Target Server Version : 80040 (8.0.40)
 File Encoding         : 65001

 Date: 07/03/2025 22:16:44
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
BEGIN;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (1, 'file', '0001_initial', '2025-03-05 13:31:04.670653');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (2, 'user', '0001_initial', '2025-03-05 13:31:04.686611');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (3, 'file', '0002_alter_file_table', '2025-03-05 13:35:01.119251');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (4, 'user', '0002_alter_user_table', '2025-03-05 13:35:01.126574');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (5, 'user', '0003_alter_user_avatar', '2025-03-05 13:37:22.812984');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (6, 'file', '0003_file_type', '2025-03-06 12:30:14.627019');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (7, 'role', '0001_initial', '2025-03-07 12:54:09.851313');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (8, 'role', '0002_alter_role_table_alter_userrole_table', '2025-03-07 12:55:17.767888');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (9, 'role', '0003_alter_userrole_role_id_alter_userrole_user_id', '2025-03-07 13:04:50.858363');
COMMIT;

-- ----------------------------
-- Table structure for file
-- ----------------------------
DROP TABLE IF EXISTS `file`;
CREATE TABLE `file` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `url` varchar(255) DEFAULT NULL,
  `originalname` varchar(255) DEFAULT NULL,
  `dest` varchar(125) DEFAULT NULL,
  `filename` varchar(125) NOT NULL,
  `size` int NOT NULL,
  `createTime` datetime(6) NOT NULL,
  `updateTime` datetime(6) NOT NULL,
  `type` varchar(125) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url` (`url`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of file
-- ----------------------------
BEGIN;
INSERT INTO `file` (`id`, `url`, `originalname`, `dest`, `filename`, `size`, `createTime`, `updateTime`, `type`) VALUES (15, '/media/7069100727988ae093e0fc635f606548/1741267913783.mp4', '1521900461-1-16.mp4', 'media/7069100727988ae093e0fc635f606548', '1741267913783.mp4', 28659734, '2025-03-06 13:31:53.792139', '2025-03-06 13:31:53.793427', 'video/mp4');
INSERT INTO `file` (`id`, `url`, `originalname`, `dest`, `filename`, `size`, `createTime`, `updateTime`, `type`) VALUES (16, '/media/634546cf1fbb14c2a8abc986dba3da6e/1741267921680.jpg', '3183845842.jpg', 'media/634546cf1fbb14c2a8abc986dba3da6e', '1741267921680.jpg', 10796, '2025-03-06 13:32:01.681561', '2025-03-06 13:32:01.683509', 'image/jpeg');
INSERT INTO `file` (`id`, `url`, `originalname`, `dest`, `filename`, `size`, `createTime`, `updateTime`, `type`) VALUES (17, '/media/7069100727988ae093e0fc635f606548/1741267931361.mp4', '水中花.mp4', 'media/7069100727988ae093e0fc635f606548', '1741267931361.mp4', 56324848, '2025-03-06 13:32:11.385885', '2025-03-06 13:32:11.387127', 'video/mp4');
INSERT INTO `file` (`id`, `url`, `originalname`, `dest`, `filename`, `size`, `createTime`, `updateTime`, `type`) VALUES (18, '/media/f3459d88a01501e64fe6c19ef16f1c9c/1741267939363.mp3', '人间烟火.mp3', 'media/f3459d88a01501e64fe6c19ef16f1c9c', '1741267939363.mp3', 9349958, '2025-03-06 13:32:19.374671', '2025-03-06 13:32:19.375904', 'audio/mpeg');
INSERT INTO `file` (`id`, `url`, `originalname`, `dest`, `filename`, `size`, `createTime`, `updateTime`, `type`) VALUES (19, '/media/7069100727988ae093e0fc635f606548/1741268217239.mp4', 'gidle.mp4', 'media/7069100727988ae093e0fc635f606548', '1741268217239.mp4', 87063330, '2025-03-06 13:36:57.278413', '2025-03-06 13:36:57.280158', 'video/mp4');
COMMIT;

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(125) NOT NULL,
  `createTime` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of role
-- ----------------------------
BEGIN;
INSERT INTO `role` (`id`, `name`, `createTime`) VALUES (1, '管理员', '2025-03-07 13:00:06.933525');
INSERT INTO `role` (`id`, `name`, `createTime`) VALUES (2, '总监', '2025-03-07 13:00:23.806337');
INSERT INTO `role` (`id`, `name`, `createTime`) VALUES (3, '商家', '2025-03-07 13:00:27.989667');
INSERT INTO `role` (`id`, `name`, `createTime`) VALUES (4, '游客', '2025-03-07 13:00:34.224002');
INSERT INTO `role` (`id`, `name`, `createTime`) VALUES (5, '普通用户', '2025-03-07 13:00:39.282035');
INSERT INTO `role` (`id`, `name`, `createTime`) VALUES (6, 'UI', '2025-03-07 13:00:46.434571');
INSERT INTO `role` (`id`, `name`, `createTime`) VALUES (8, '运维', '2025-03-07 13:00:58.508871');
INSERT INTO `role` (`id`, `name`, `createTime`) VALUES (9, '测试', '2025-03-07 13:01:02.492869');
INSERT INTO `role` (`id`, `name`, `createTime`) VALUES (10, 'VIP', '2025-03-07 13:02:21.989836');
INSERT INTO `role` (`id`, `name`, `createTime`) VALUES (11, '客服', '2025-03-07 13:05:38.902169');
COMMIT;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user_id` varchar(100) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `gender` int NOT NULL,
  `password` varchar(255) NOT NULL,
  `description` longtext,
  `avatar` bigint DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_name` (`user_name`),
  KEY `user_avatar_2d14d89e_fk_file_id` (`avatar`),
  CONSTRAINT `user_avatar_2d14d89e_fk_file_id` FOREIGN KEY (`avatar`) REFERENCES `file` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` (`user_id`, `user_name`, `gender`, `password`, `description`, `avatar`) VALUES ('1741261813698', '叶子', 1, '123', '第一人', NULL);
INSERT INTO `user` (`user_id`, `user_name`, `gender`, `password`, `description`, `avatar`) VALUES ('1741263123265', 'coder', 1, '123', '第三人', NULL);
INSERT INTO `user` (`user_id`, `user_name`, `gender`, `password`, `description`, `avatar`) VALUES ('1741263200749', 'ai', 1, '123', '第五人', NULL);
COMMIT;

-- ----------------------------
-- Table structure for user_role
-- ----------------------------
DROP TABLE IF EXISTS `user_role`;
CREATE TABLE `user_role` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `createTime` datetime(6) NOT NULL,
  `role_id` bigint NOT NULL,
  `user_id` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `role_userrole_user_id_id_role_id_id_3860b917_uniq` (`user_id`,`role_id`),
  KEY `user_role_role_id_6a11361a_fk_role_id` (`role_id`),
  CONSTRAINT `user_role_role_id_6a11361a_fk_role_id` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`),
  CONSTRAINT `user_role_user_id_12d84374_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of user_role
-- ----------------------------
BEGIN;
INSERT INTO `user_role` (`id`, `createTime`, `role_id`, `user_id`) VALUES (1, '2025-03-07 13:18:10.916913', 1, '1741261813698');
INSERT INTO `user_role` (`id`, `createTime`, `role_id`, `user_id`) VALUES (2, '2025-03-07 13:18:44.006907', 2, '1741261813698');
INSERT INTO `user_role` (`id`, `createTime`, `role_id`, `user_id`) VALUES (3, '2025-03-07 13:18:50.234481', 6, '1741261813698');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
