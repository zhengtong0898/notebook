TODO: 7. [InnoDB的行级锁的原理](./docs/InnoDBLineLock.md)  

&nbsp;  
### 常见数据类型存储占位




&nbsp;  
&nbsp;  


&nbsp;  
&nbsp;  

&nbsp;  
&nbsp;   


&nbsp;  
&nbsp;  


&nbsp;  
&nbsp;  
### 索引添加原则
当 `联合索引` 和其他字段组成查询条件时, 需要额外增加索引;   
索引添加规则需根据 [索引最左前缀匹配原则](./README.md#索引最左前缀匹配原则) 指导来进行, 例如:  
```shell script
-- 创建一张 geek 表
CREATE TABLE `geek` (
  `a` int(11) NOT NULL,
  `b` int(11) NOT NULL,
  `c` int(11) NOT NULL,
  `d` int(11) NOT NULL,
  PRIMARY KEY (`a`,`b`),
) ENGINE=InnoDB;

-- select * from `geek` where c=10 and a=10;
-- 首先这个(c, a)组合的查询条件, 无法使用索引. 
-- 要建立一个有效的索引有两种方式: 
--     1. 建立一个 (c, a) 的联合索引;   alter table `geek` add index idex_c_a (`c`, `a`);
--     2. 建立一个单独的 c 的索引;      alter table `geek` add index idex_c (`c`);
--     3. 查看建立的索引;              show index from `geek`;
-- 当选择建立(c,a)联合索引时, 可命中索引; 因为 (c, a) 索引会带上聚集索引字段(a, b), 但由于 a 已使用, 所以优化器会仅选择 b; 即: c, a, b 顺序
-- 当选择建立单独 c 索引时, 也可命中索引; 因为 c 索引会带上聚集索引的字段(a, b); 即: c, a, b 顺序
-- 在这种情况下, (a,b,c)/(a,c,b)/(b,a,c)/(b,c,a)/(c,a,b)/(c,b,a)组合查询, 优化器会选择(a,b)聚集索引, 直接从聚集索引的行中读取c字段值.   
```


&nbsp;   
&nbsp;   


&nbsp;  
&nbsp;  
 ### 参数表
| 字段名 | 默认值 | 描述 |   
| :--- | :--- | :--- |   
|datadir|C:\Program Files\MariaDB 10.5\data\| 数据库的数据目录 |
|innodb_page_size| 16384 (byte)| 每个 page 的大小|
|[innodb_file_per_table](tests/innodb_file_per_table/README.md#描述)|On|每个表一个.ibd文件(称为表空间)|
|[innodb_data_file_path](./README.md#表空间)|C:\Program Files\MariaDB 10.5\data\ibdata1| 共享表空间(innodb_file_per_table=Off)时, <br>所有表信息都保存在共享表空间内. |


&nbsp;  
&nbsp;  
### 查看历史操作记录
查看数据库历史操作之前, 需要先开启日志功能.   


- 日志保存在文件中  
   `windows` 默认保存路径是: `C:\ProgramData\MySQL\`
   ```shell
   > SET GLOBAL log_output = "TABLE";
   > SET GLOBAL general_log = 'ON';
   ```
  
- 日志保存在表中(`mysql.general_log`)  
   ```shell
   SET GLOBAL log_output = "FILE";
   SET GLOBAL general_log = 'ON';
   ```

&nbsp;  
&nbsp;  

&nbsp;  
&nbsp;  
### 

  
&nbsp;  
&nbsp;  

&nbsp;  
&nbsp;  
### 表空间
`MySQL`的表空间是一个.ibd后缀的实体文件.   
表空间文件内由段(`segment`), 区(`extent`), 页(`page`), 行(`row`)组成.   
它们之间的关系是包含关系: 段包含区, 区包含页, 页包含行, 而一行就代表着实际的表中的一行(多个字段)数据.  
由于`InnoDB`存储引擎是按照聚集索引形式来组织数据的分布, 因此数据即索引, 索引即数据.   

- 段(segment)   
  常见的段有: 叶子节点段(Leaf node segment), 非叶子节点(Non-Leaf node segment), 回滚段(Rollback segment).

- 区(extent)   
  在任何情况下每个区的大小都是`1MB`, 每个页(page)默认大小是`16KB`拿, `64`个页可以填满一个区, `64 * 16KB`即为`1M`.  

- 页(page)   
  每个页存放的行记录数量规则是: 2 ~ 7992(16kb / 2 - 200) 行.
  
- 行(row)  
  表中一行各字段的数据实际的数据.  


&nbsp;  
&nbsp;  




&nbsp;  
&nbsp;  
