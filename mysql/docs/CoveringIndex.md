### 覆盖索引    
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
        
