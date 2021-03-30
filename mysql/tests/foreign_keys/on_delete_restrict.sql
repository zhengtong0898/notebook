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
  -- ON DELETE CASCADE: `author`数据被删除时, 也会对应删除当前表关联的数据.
  FOREIGN KEY (`author_id`) REFERENCES `author` (`id`) ON DELETE RESTRICT
);


-- 插入数据
insert into `author` (`name`) values ('zhang_san'), ('li_si'), ('lao_wang');
insert into `article` (`title`, `content`, `author_id`) values ('文章-1', '内容-1', '1');
insert into `article` (`title`, `content`, `author_id`) values ('文章-2', '内容-2', '1');
commit;


-- 测试-1: 删除没有被关联的数据,
delete from `author` where id=2;
-- 断言-1: 可以正常更改.
select * from `author`;


-- 测试-2: 删除 `author`.`id` = 1 的数据
delete from `author` where id=1;
-- 断言-2: 期望在删除数据时, 数据库会报错, 不让删除.
-- 所以: 解决办法是, 先删除掉子表中对应的关联数据, 然后再更改或删除父表中的数据.
-- Error: Cannot delete or update a parent row: a foreign key constraint fails (`sss`.`article`, CONSTRAINT `article_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `author` (`id`))


-- 恢复: 删除表 `author` 和 `article`
delete from `article`;		-- 先清空子表
delete from `author`;       -- 再清空父表
drop table `article`;       -- 先删除子表(referencing table)
drop table `author`;        -- 再删除父表(referenced table)

