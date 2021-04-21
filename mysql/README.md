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
`MySQL`为性能分析提供的另外一个工具就是 `explain` 关键字, 用来描述一条 `SQL` 语句会以什么方式来运行(是否命中索引), 描述形式如下:    

- explain  

  |字段|含义|
  |---|---|
  |id|每个SELECT语句都会自动分配一个唯一的标识符, 标记整个SQL语句包含了多少次 SELECT. | 
  |select_type|每个select查询字句的类型, 标记当前 select 是最外层select, 还是子select, 还是select, 还是临时表的子select, 等等.| 
  |table|当前select查询的是哪个表| 
  |type|访问类型, 是全表扫描, 还是范围扫描, 还是索引查询, 还是join查询|
  |possible_keys|查询的字段涉及到了哪些索引|
  |key|实际采用哪个索引|
  |key_len|采用索引的key的长度|
  |ref|使用哪个字段来做索引查找|
  |rows|要匹配到查找值, 预估需要检查多少行.|
  |Extra|使用哪些方式来处理查询条件|

- select_type 
  
  |类型名|含义|
  |---|---|
  |SIMPLE|简单SELECT,不使用UNION或子查询等|
  |PRIMARY|最外层的select被标记为PRIMARY|
  |UNION|UNION中的第二个或后面的SELECT语句|
  |DEPENDENT UNION|UNION中的第二个或后面的SELECT语句，取决于外面的查询|
  |UNION RESULT|UNION的结果|
  |SUBQUERY|子查询中的第一个SELECT|
  |DEPENDENT SUBQUERY|子查询中的第一个SELECT，取决于外面的查询|
  |DERIVED|派生表的SELECT, FROM子句的子查询|
  |MATERIALIZED|表示是一个子查询, 采用虚拟表先查询出所有结果, 然后再与外层表做比较(避免多次n+1查询).|
  |UNCACHEABLE SUBQUERY|一个子查询的结果不能被缓存，必须重新评估外链接的第一行|
  |UNCACHEABLE UNION|一个UNION查询的结果不能被缓存，必须重新评估外链接的第一行|
 
- type
  
  |类型名|优先级|含义|
  |:---:|:---:|:---:|
  |system|1|表仅有一行|
  |const|2|匹配字段是 primary key 或 unique key|
  |eq_ref|3|使用primary key或者unique key作为多表连接的条件,仅从该表中读取一行|
  |ref|4|join是按非unique类型的索引来做联结的|
  |fulltext|5|全文索引检索, 倒排索引|
  |ref_or_null|6|和ref一致，但增加了NULL值查询支持|
  |index_merge|7|表示使用了索引合并优化方法|
  |unique_subquery|8|使用in + 子查询方式, 替代eq_ref|
  |index_subquery|9|使用in + 子查询方式, 替代ref|
  |range|10|只检索给定范围的行,使用一个索引来选择行|
  |index|11|全表扫描，但扫描表的方式是按索引的次序进行|
  |ALL|12|全表扫描的方式找到匹配的行|
  
- Extra

  |类型名|含义|
  |---|---|
  |Using where|列数据是从仅仅使用了索引中的信息而没有读取实际的行动的表返回的，|  
  |Using index|单子字段索引匹配, 直接返回结果|
  |Using temporary|表示MySQL需要使用临时表来存储结果集，常见于排序和分组查询|  
  |Using filesort|MySQL中无法利用索引完成的排序操作称为“文件排序”|  
  |Using join buffer|改值强调了在获取连接条件时没有使用索引，并且需要连接缓冲区来存储中间结果。如果出现了这个值，那应该注意，根据查询的具体情况可能需要添加索引来改进能。|  
  |Impossible where|这个值强调了where语句会导致没有符合条件的行。|  
  |Select tables optimized away|这个值意味着仅通过使用索引，优化器可能仅从聚合函数结果中返回一行|  
  
- 参考
  > https://stackoverflow.com/a/4528433   
  > https://segmentfault.com/a/1190000016591055   
  > https://dev.mysql.com/doc/refman/5.6/en/explain-output.html   



&nbsp;  
&nbsp;   
### 查询所有字段(select *) vs 查询指定字段(select column)

> 覆盖索引    
> 由于辅助索引(Secondary Index)的LeafNode的Key就是字段值,    
> 所以当`select column`是索引字段名时, 直接返回Key而不需要回表(这个过程被称为覆盖索引).
>    
> 回表    
> 但是当`select column`不是索引字段名时, 辅助索引就会根据value的值(指向聚集索引的key),   
> 到聚集索引去找到对应的key(这个过程被称为回表).

- 数据传输消耗      
  `select *`会每次返回所有字段, 当某些不用的字段是`Text`,    
  `MediumText`且该字段存储大量内容时, 读取/传输/渲染/都会占用大量内存和网络消耗.   
  
  因此, 不是每个功能的数据响应都需要全部字段, 所以最好是按需使用.   

- 绑定问题  
  如果查询语句是`join`, 那么`select *`就会出现相同字段名冲突.

- 覆盖索引问题   
  - where命中索引的情况下:   
    当 `select column` 不是一个索引字段时, 需要回表, 性能略差.   
    当 `select column` 是一个索引字段时, 不需要回表, 性能优.   
    
    对于单条数据的回表的性能问题不大, 但是当数据集较大时, 频繁的回表操作势必会   
    造成一定的性能影响, 因此能走覆盖索引就没有理由走回表.   

  - where没有命中索引的情况下:  
    全表扫描.


> 参考:   
> https://stackoverflow.com/questions/3639861/why-is-select-considered-harmful   
> https://blog.csdn.net/qq_15037231/article/details/87891683   
> https://www.jianshu.com/p/9b3406bcb199   
        

&nbsp;  
&nbsp;  
### 最左前缀匹配原则
一般情况下当我们说建一个索引, 对于`MySQL`的`InnoDB`来说就是创建一颗`B+树`.   
一个包含多字段的联合索引, 例如: (`name`, `cid`, `school`) 三个字段组成的联合索引;   
对应于`MySQL`的`InnoDB`来说, 就是创建一颗`B+树`(辅助索引), Key保存的是三个字段的值, Value是指向聚集索引的Key.   
在`B+树`中, 三个字段组成的Key是严格按照定义联合索引时, 指定的字段顺序来生成的.     
假设有四条数据, 它们分别是:   
```
数据一: name='zhangsan', cid='6', school='yi_zhong'        # 张三, 六年纪, 一中
数据二: name='lisi', cid='7', school='er_zhong'            # 李四, 初一, 二中
数据三: name='wangwu', cid='8', school='yi_zhong'          # 王五, 初二, 一中
数据四: name='zhangsan', cid='3', school='yi_zhong'        # 张三, 三年纪, 一中
```
对应于`MySQL`的`InnoDB`来说, 这三条数据生成的Key长这样:
```shell
# 由于存储是经过排序的, 所以存储顺序和插入数据顺序是不一样的,   
# 但是别搞混, key生成的顺序必须与定义索引时一致.   
('lisi', '7', 'er_zhong')
('wangwu', '8', 'yi_zhong')
('zhangsan', '3', 'yi_zhong')                             # 第一个字段相同, 按第二个字段值大小来排序.
('zhangsan', '6', 'yi_zhong')
```
单字段查询`where name='zhangsan'`, 使用索引, 因为`name`字段是经过排序的, 二分查找可以有效命中.   
单字段查询`where cid='6'`, 不使用索引, 因为`cid`字段并没有经过排序, 二分查找无法有效命中.   
两字段组合查询`where name='zhangsan' and cid='6'`, 使用索引, 
因为`name`字段经过排序, 同时因为在`name`的基础上`cid`也是经过排序的, 所以二分查找可以有效命中.   
下面列出完整的匹配清单, 观察索引命中的整体规则, 为了简化排列组合, 采用 a(name), b(cid), c(school) 命名.   

|组合|使用索引|描述|
|---|:---:|---|
|a|是|因为整表的`a`字段是经过排序的, 二分查找可以有效命中.|
|b|-|因为整表的`b`字段并没有经过排序, 二分查找无法有效命中.|
|c|-|因为整表的`c`字段并没有经过排序, 二分查找无法有效命中.|
|a, b|是|因为`a`字段经过排序, 同时因为在`a`的基础上`b`也是经过排序的, 所以二分查找可以有效命中.|
|a, c|-|由于`c`是基于`b`来分组排序的, 所以在`a`的基础上`c`肯定没有排序, 二分查找无法有效命中.|
|b, a|是|`MySQL`优化器会将`b`, `a`位置换成`a`, `b`然后在去查询, 因此会使用索引.|
|b, c|-|整表的`b`字段并没有经过排序, 二分查找无法有效命中, 所以后续的`c`也不会命中索引.|
|c, a|-|整表的`c`字段并没有经过排序.|
|c, b|-|整表的`c`字段并没有经过排序.|
|a,b,c|是|整表的`a`字段经过排序, 同时在`a`的基础上`b`经过排序, 同时在`b`的基础上`c`经过排序, 二分查找可以有效命中.|
|a,c,b|是|`MySQL`优化器会将其转换为a,b,c; 所以可以命中索引.|
|b,a,c|是|`MySQL`优化器会将其转换为a,b,c; 所以可以命中索引.|
|b,c,a|是|`MySQL`优化器会将其转换为a,b,c; 所以可以命中索引.|
|c,a,b|是|`MySQL`优化器会将其转换为a,b,c; 所以可以命中索引.|
|c,b,a|是|`MySQL`优化器会将其转换为a,b,c; 所以可以命中索引.|

`like` 和 `范围查询` 的情况:   

|组合|使用索引|描述|
|---|:---:|---|
|a like 'j%'|是|like 后置百分号, 由于前置字符是可以确定的, 可以采用常规比较.|
|a like '%j%'|是|like 前置百分号, 无法采用常规比较, 只能全表扫描.|
|a like '%j'|是|like 前置百分号, 无法采用常规比较, 只能全表扫描.|
|a='j' and b>2 and c='h'|是|根据key_len观察, 可以判断出仅使用到a和b的索引, c走全表扫描.|  

&nbsp;  
`范围查询`优化:   
通过开启 `MRR` 优化参数, 
没有开启`MRR`时, 当查询到大量数据时(辅助索引), 每行数据都回表一次.   
当开启`MRR`后, 当查询到大量数据时, 先建立聚集索引排序, 然后再按照排好序的id去回表查找, 这样邻近值就会被一次命中多条.   

&nbsp;  
`like`优化:   
通过开启 `index_condition_pushdown` 优化参数, 
这个参数可以在查找聚集索引时实时处理where过滤条件, 含 `like` . 


&nbsp;  
&nbsp;  
### 没有定义主键会发生什么?   
[官方有提到](https://dev.mysql.com/doc/refman/8.0/en/innodb-index-types.html)   
如果没有定义主键(Primary Key), `InnoDB`会尝试找唯一索引(Unique Key)来当聚集索引.   
如果即没有定义主键(Primary Key), 也没有定义唯一索引(Unique Key), 那么`MySQL`会简历一个隐藏的主键.

> 关于性能   
> 因为无法使用聚集索引特性, 那么在做where条件时自然就不能享受聚集索引的效率.  
> 但还是可以使用 辅助索引(普通索引/联合索引) 来提速.  
> 因此总体上来说问题不大.  



&nbsp;  
&nbsp;  
### int(11)是什么意思?  
从编程语言的角度去看一个`int`类型对象, 一个`int`占用`4`个字节,    
`Signed int`(默认)它的最小存储数字是`-2147483648`, 它最大存储的数字是`2147483647`,    
`UnSigned int`它的最小存储数字是`0`, 它最大存储的数字是`4294967295`.   

> 最大值最小值是怎么计算出来的?  
- Signed Int   
  `signed_min_int = 2 ** (4 * 8) / 2 * -1 == -2147483648`  
  `signed_max_int = 2 ** (4 * 8) / 2 - 1  == 2147483647`  
  
- UnSigned Int  
  `unsigned_min_int = 0`   
  `unsigned_max_int = 2 ** (4 * 8) - 1    == 4294967295`

> 以 `UnSinged int`为例, 观察二进制形式的规律.     

|字节(byte)|位(bit)|二进制(binary)|最大值|python表达式|
|:---:|:---:|:---:|:---:|:---:|
|1|8|11111111|255|int('0b11111111', 2)|  
|2|16|`11111111` `11111111`|65535|int('0b1111111111111111', 2)|  
|3|24|`11111111` `11111111` `11111111`|16777215|int('0b111111111111111111111111', 2)|  
|4|32|`11111111` `11111111` `11111111` `11111111`|4294967295|int('0b11111111111111111111111111111111', 2)|  

了解了`int`背后相关的知识之后, 再回来看数据库中的`int(11)`的问题,   
`MySQL`在存储时并不关注建表时定义的限定值, 比如说建表时定义了 `int(1)`,    
实际存储`10`, `100`, `1000` 都是可以存储的, 只要不超过`2147483647`,    
也就是说, 这个限定值对于`MySQL`来说是没有意义的.    

它的作用是, 让像`Django ORM`这种客户端程序来约束程序的规范.  
 
 


&nbsp;  
&nbsp;  
### 内存溢出
有些时候 MySQL 占用内存涨得特别快, 这很有可能是因为 MySQL 在执行过程中临时使用的内存是管理在连接对象里面的.  
这些资源会在连接断开的时候才释放, 所以如果长连接累积下来, 可能导致内存占用太大，被系统强行杀掉(OOM).   

解决办法:   
客户端程序在每次执行了大的查询之后, 可以通过执行`mysql_reset_connection`来重新初始化长连接, 使其释放掉内存.

