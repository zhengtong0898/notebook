-- 建表: 父表
CREATE TABLE `author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
);


-- 建表: 子表
CREATE TABLE `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `content` mediumtext NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `author_id` (`author_id`),

  -- `author`表在这里被视为是`article`表的父表.
  -- ON UPDATE CASCADE: `author`一行的`Primary Key`被更改时, 当前表中对应的关联数据的`author_id`也会被更改.
  FOREIGN KEY (`author_id`) REFERENCES `author` (`id`) ON UPDATE CASCADE
);


-- 插入数据
insert into `author` (`name`) values ('zhang_san'), ('li_si'), ('lao_wang');
insert into `article` (`title`, `content`, `author_id`) values ('文章-1', '内容-1', '1');
insert into `article` (`title`, `content`, `author_id`) values ('文章-2', '内容-2', '1');
commit;


-- 测试: 更改 `author`.`id` 的值
update `author` set `id`=1000 where `id`=1;


-- 断言: -- 断言: 确认 `article` 表中的'文章-1' 和 '文章-2' 这两条数据的`author_id`字段的值被同步地更新为1000.
select * from `article`;


-- 恢复: 删除表 `author` 和 `article`
delete from `article`;		-- 先清空子表
delete from `author`;       -- 再清空父表
drop table `article`;       -- 先删除子表(referencing table)
drop table `author`;        -- 再删除父表(referenced table)
