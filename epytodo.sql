/*DROP DATABASE IF EXISTS epytodo;*/
CREATE DATABASE IF NOT EXISTS epytodo;

USE epytodo;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE IF NOT EXISTS `task` (
  `task_id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `begin` datetime DEFAULT current_timestamp(),
  `end` datetime DEFAULT NULL,
  `status` ENUM('not started', 'in progress', 'done') DEFAULT 'not started'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `task`
  ADD PRIMARY KEY (`task_id`);

ALTER TABLE `task`
   MODIFY `task_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

INSERT INTO `task` (`task_id`, `title`, `begin`, `end`, `status`) VALUES
(1, 'Test task', '2020-03-18 18:00:12', NULL, 'not started');

CREATE TABLE IF NOT EXISTS `user` (
  `user_id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `logged` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

INSERT INTO `user` (`user_id`, `username`, `password`, `logged`) VALUES
(1, 'simon', 'simon', 0);

CREATE TABLE IF NOT EXISTS `user_has_task` (
  `fk_user_id` int(11) NOT NULL,
  `fk_task_id` int(11) NOT NULL,
  FOREIGN KEY fka(fk_user_id) REFERENCES user(`user_id`),
  FOREIGN KEY fkb(fk_task_id) REFERENCES task(`task_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `user_has_task` (`fk_user_id`, `fk_task_id`) VALUES
(1, 1);

COMMIT;
