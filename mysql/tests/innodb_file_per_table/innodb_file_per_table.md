### 描述   
`innodb_file_per_table` 参数默认值是 `On`, 表示创建表时同步创建一个.ibd后缀的表空间文件.
- 当参数值为`ON`时   
  新建的表(的索引, 数据)都存储在.ibd文件(独立表空间)中, 表结构存储在.frm文件中; 回滚信息, 事务信息, 二次写缓冲等信息统一写在ibddata1文件(共享表空间)中.
- 当参数值为`OFF`时
  新建的表, 其表结构存储在.frm文件中, 索引、数据、回滚信息、事务信息、二次写缓冲等信息全部写在ibddata1文件(共享表空间)中.

&nbsp;   
&nbsp;   
### 测试
1. 将`innodb_file_per_table` 参数设置为 `Off`.  
   `set global innodb_file_per_table = 'OFF';`
2. 创建一张表`ifpt`.   
   `create table ifpt ( a int(11) not null primary key auto_increment);`
3. 断言: ifpt.ibd(表空间文件)不存在.  
   经观察, ifpt.ibd(表空间文件)不存在, 但是会有一个 ifpt.frm 文件(这是一个表结构信息文件).
4. 恢复 `innodb_file_per_table` 参数值为 `On`.   
5. 插入10万条数据.  
   运行 [`innodb_file_per_table.py`](./innodb_file_per_table.py) 程序
6. 断言:   
   经观察, C:\Program Files\MariaDB 10.5\data\ibddata1 文件大小从 70M 增加到了 140M.
7. 删除 ifpt 表.   
   经观察, ifpt.frm 文件已经被删除, 但是 ibddata1 文件大小并没有发生变化.  
   重启电脑后, 在观察, ibddata1 文件大小仍然没有发生变化.       
   
   > MySQL技术内幕 InnoDB存储引擎, 94页, 最后一段    
   > InnoDB不会回收这些空间, 但是它会将这些空间标记为可用空间.  
   
&nbsp;      
&nbsp;      
### 小结
1. 这是一个动态指令(更改即生效有效), 不需要重启数据库或操作系统.   
2. 经过测试了解该参数的运作原理.   

 