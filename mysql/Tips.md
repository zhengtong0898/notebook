### 内存溢出
有些时候 MySQL 占用内存涨得特别快, 这很有可能是因为 MySQL 在执行过程中临时使用的内存是管理在连接对象里面的.  
这些资源会在连接断开的时候才释放, 所以如果长连接累积下来, 可能导致内存占用太大，被系统强行杀掉(OOM).   

解决办法:   
客户端程序在每次执行了大的查询之后, 可以通过执行`mysql_reset_connection`来重新初始化长连接, 使其释放掉内存.


&nbsp;  
&nbsp;   
### 优化器
表里有多个索引, `MySQL`决定使用哪个索引;   
多表关联join时, `MySQL`决定先使用哪个表;   
TODO: 决策细节?


&nbsp;  
&nbsp;   
### 执行器
- 无索引的情况下  
  1. 检查权限
  2. 打开表
  3. 读取第一行数据, 判断匹配条件是否满足(假设不满足).
  4. 读取第二行数据, 判断匹配条件是否满足(假设不满足).
  5. 读取第三行数据, 判断匹配条件是否满足(假设满足, 添加到返回结果集).
  6. 读取第四行数据, 判断匹配条件是否满足(假设满足, 添加到返回结果集).
  7. 读取到最后一行, 将所有匹配条件满足的数据都加入到返回结果集中.
  8. 结果集返回给客户端.
- 有索引的情况  
  TODO: 待补充  


&nbsp;  
&nbsp;   
### Redo Log 和  BinLog
> 参考: 
> https://cloud.tencent.com/developer/article/1497297

当有一条记录需要更新的时候，InnoDB 引擎就会先把记录写到 redo log 里面，并更新内存.  
在系统比较空闲的时候, InnoDB 引擎会将这个操作记录更新到 binlog 里面.  
TODO: redo log 是磁盘文件吗? 在哪里? 
TODO: binlog 是磁盘文件吗? 在哪里?  


&nbsp;  
&nbsp;  
### 执行计划(Explain)
> 参考:   
> https://mengkang.net/1124.html   
> https://mysqlserverteam.com/mysql-explain-analyze/   
> https://dev.mysql.com/doc/index-other.html   
> https://dev.mysql.com/doc/refman/5.6/en/explain-output.html#explain-join-types   
> https://dev.mysql.com/doc/workbench/en/wb-performance-explain.html   
> https://dev.mysql.com/doc/sakila/en/   
> http://www.cnitblog.com/aliyiyi08/archive/2008/09/09/48878.html   


