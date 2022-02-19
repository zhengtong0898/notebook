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
