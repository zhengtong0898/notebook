 ### 参数表
| 字段名 | 默认值 | 描述 |   
| :--- | :--- | :--- |   
|datadir|C:\Program Files\MariaDB 10.5\data\| 数据库的数据目录 |
|innodb_page_size| 16384 (byte)| 每个 page 的大小|
|[innodb_file_per_table](./tests/innodb_file_per_table/innodb_file_per_table.md#描述)|On|每个表一个.ibd文件(称为表空间)|
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
### 数据库语言
> 参考资料:   
> https://sites.google.com/site/prgimr/sql

- DML  
  Data Manipulation Language: 数据操纵语言   
  select, insert, update, delete, merge, call, explain plan, lock table 语句都会在这里执行.

- DDL  
  Data Definition Language: 数据库定义语言   
  create, alter, drop, comment, truncate, rename 语句都会在这里执行.
  
- DCL
  Data Control Language: 数据库控制语言   
  grant, revoke 语句都会在这里执行.
  
- TCL  
  Transaction Control Language: 事务控制语言  
  commit, rollback, savepoint, set transaction 语句都会在这里执行.


&nbsp;  
&nbsp;  
### 外键操作(Referential Actions)
> 参考资料:   
> [create-table-foreign-keys](https://dev.mysql.com/doc/refman/8.0/en/create-table-foreign-keys.html)   
> [mysql-on-delete-cascade](https://www.mysqltutorial.org/mysql-on-delete-cascade/)   
> [difference-between-on-delete-cascade-on-update-cascade-in-mysql](https://dba.stackexchange.com/questions/74627/difference-between-on-delete-cascade-on-update-cascade-in-mysql)

- CASCADE  
  如果在父表中[删除](tests/foreign_keys/on_delete_cascade.sql)了一行数据, 子表中对应的关联数据也会被删除.   
  如果在父表中[更新](tests/foreign_keys/on_update_cascade.sql)了一行数据的`Primary Key`字段的值, 子表中对应的关联数据也会自动更新外键值.

- RESTRICT  
  如果在父表中[删除](tests/foreign_keys/on_delete_restrict.sql)一行数据, 该行数据被子表的数据关联, 那么就会报错(可以通过上面的`CASCADE`解决这个问题).   
  如果在父表中[删除](tests/foreign_keys/on_delete_restrict.sql)一行数据, 该行数据没有被子表的数据关联, 那么就可以正常删除.   
  
  如果再父表中[更新](tests/foreign_keys/on_update_restrict.sql)一行数据的`Primary Key`字段的值, 该行数据被子表的数据关联, 那么就会报错.   
  如果再父表中[更新](tests/foreign_keys/on_update_restrict.sql)一行数据的`Primary Key`字段的值, 该行数据没有被子表的数据关联, 那么就可以正常更新.   

- NO ACTION    
  当建表时声明了 `ON DELETE NO ACTION` 或 `ON UPDATE NO ACTION` 时, `MySQL`会将它视为`RESTRICT`.  
  在 `MySQL` 中没有 `NO ACTION` 机制, 因为更新或删除数据时, 会立即触发检查.    

- SET NULL   
  如果在父表中[删除](tests/foreign_keys/on_delete_set_null.sql)一行数据, 子表中对应的外键字段的值会被更改为`Null`.

- SET DEFAULT   
  `MySQL`不支持该机制.  
  当建表时声明了 `ON DELETE SET DEFAULT` 或 `ON UPDATE SET DEFAULT` 时, `MySQL`会忽略它;     
  即: 建表语句中不包含该机制声明, 采用的时默认机制(RESTRICT).   


  
&nbsp;  
&nbsp;  
### 慢查询日志
> 参考:  
> [mariadb:mysql.slow_log Table](https://mariadb.com/kb/en/mysqlslow_log-table/)  
> [MySQL技术内幕-InnoDB存储引擎](https://www.zhihu.com/topic/20875675/hot)

`MySQL`为性能分析提供了慢查询日志支持, 数据库会将那些慢查询的数据写入到日志中. 
- long_query_time  
  默认值: 10秒(10.000000), 支持最小设置是微妙(0.000001).      
  以默认值10秒为例, 数据库会把那些查询时间大于10秒的sql语句写入到慢查询日志中.   
  虽然最小可以设置为1微妙, 那几乎所有查询都会被写入到慢查询日志中, 因为几乎任何查询耗时都会大于1微妙.     
  所以根据实际情况设定一个符合预期的值来监控是比较好的选择, 比如说50毫秒(0.050000).
- log_queries_not_using_indexes   
  默认值是OFF.   
  当设置为ON时, 数据库将会把那些查询没有命中索引的sql语句写入到慢查询日志中.  
  
  `MySQL-5.6.5`版本增加了一个`log_throttle_queries_not_using_indexes`参数,  
  默认值: 0(表示没有限制); 以5为例, 数据库每分钟允许记录5条没有命中索引的sql语句写入到慢查询日志中.   
  `MariaDB`不支持`log_throttle_queries_not_using_indexes`参数. 
  
- log_output  
  默认值: `FILE`; 其他可选值: `TABLE`;  
  当值为 `FILE` 时, 慢查询日志写入到文件中, `Windows`下保存在: `C:\ProgramData\MySQL\MySQL Server 8.0\Data`;  
  当值为 `TABLE` 时, 慢查询日志写入到`mysql.slow_log`表中.  
  
- 慢查询日志的字段  

  | 字段名 | 描述 | 数据 |   
  | --- | --- | --- |    
  | start_time | 查询执行时间 | 2021-03-31 23:20:32.052430 |    
  | user_host | 用户和ip | root[root] @ localhost [::1] |   
  | query_time | 查询耗时 | 00:00:00.005817 |   
  | lock_time | 等待和加锁耗时 | 00:00:00.000092 |   
  | rows_sent | 查询返回数据的条目数 | 1 |   
  | rows_examined | 语句执行过程中扫描了多少行 | 10000 |   
  | db | 默认数据库 | myqueryset | 
  | last_insert_id | 插入数据时返回的自增id | 0 |   
  | insert_id | - | 0 |
  | server_id | - | 1 | 
  | sql_text | 完整的SQL语句 | select * <br>from bulk_create__product <br>where description='aaa-788' |
  | thread_id | 线程编号 | 8 |
  | rows_affected | `MariaDB-10.1.2` 开始支持<br>`update`和`delete`更改行数统计<br>`MySQL-8.0`仍没有支持 | - |
     

- 操作指令
  ```shell
  mysql> set global log_output='table';                                     # 将 log_output 改为 table
  mysql> select `start_time`,
                `user_host`, 
                `query_time`,
                `lock_time`, 
                `rows_sent`, 
                `rows_examined`, 
                `db`,
                `last_insert_id`,
                `insert_id`, 
                `server_id`, 
                CONVERT(sql_text USING utf8), 
                `thread_id` 
         from `mysql`.`slow_log`;                                           # 慢查询日志
  mysql> set global log_queries_not_using_indexes = 'on';                   # 启用未命中索引写入慢查询日志
  mysql> show variables like 'log_queries_not_using_indexes';               # 查看配置
  mysql> set global log_throttle_queries_not_using_indexes = 3;             # 每分钟允许写入三条
  mysql> show variables like 'log_throttle_queries_not_using_indexes';      # 查看配置
  ```

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
### 执行计划
