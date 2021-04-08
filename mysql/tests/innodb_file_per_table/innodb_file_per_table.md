### 描述   
`innodb_file_per_table` 参数默认值是 `On`, 表示创建表时同步创建一个.ibd后缀的表空间文件, 表空间文件包含表数据和索引数据.

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
   运行 `innodb_file_per_table.py` 程序
6. 断言:   
   经观察, C:\Program Files\MariaDB 10.5\data\ibddata1 文件大小从 70M 增加到了 140M.
7. 删除 ifpt 表.   
   经观察, ifpt.frm 文件已经被删除, 但是 ibddata1 文件大小并没有发生变化.  
   重启电脑后, 在观察, ibddata1 文件大小仍然没有发生变化. TODO: 这是为什么呢?   

&nbsp;      
&nbsp;      
### 小结
1. 这是一个动态指令(更改即生效有效), 不需要重启数据库或操作系统.   
2. 经过测试了解该参数的运作原理.   

 
 