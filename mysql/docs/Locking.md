
### 共享锁(shared lock)  
当一个事务为数据加上读锁之后, 其他事务只能对该数据加读锁, 不能对该数据加写锁.  

### 排他锁(exclusive lock)  
当一个事务为数据加上写锁之后, 其他事务不能对该数据再加写锁, 也不能对该数据加读锁.  

### 表锁(table level lock)  
上锁的时候锁住的是整个表, 当下一个事务访问该表的时候, 必须等前一个事务释放了锁才能对表进行加锁(和访问).

### 行锁(row level lock)  
上锁的时候锁住一行或多行数据, 其他事务访问同一张表不同行的数据时, 互不影响.  

### 记录锁(record lock)
上锁的时候锁住一行数据, 其他事务访问同一张表不同行的数据时, 互不影响.  
命中条件字段必须是唯一索引或主键索引.  

### 间隙锁(gap lock)
上锁的时候锁住一个范围, 不允许其他事务插入这个范围内的数据, 例如下面这条语句:   
> SELECT c1 FROM t WHERE c1 BETWEEN 10 and 20 FOR UPDATE;  

它将会锁住 10 - 20 这个区间的数据, 如果此时有事务要插入15是不被允许的.  


### Next-Key Locks
看不懂.  


TODO: 怎么加锁?


[参考资料-1](https://dev.mysql.com/doc/refman/8.0/en/innodb-locking.html)   
[参考资料-2](https://www.bilibili.com/video/BV1Fb4y1h7Fe?p=30)  
