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
