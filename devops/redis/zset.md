### 排名(计数)  
zincrby topic:按天 number topic_id


### 合并集合
zunionstore topic:合并3天 3 topic:天1 topic:天2 topic:天3  


### 排名(提取)  
zrevrange topic:合并3天 0 9 withscores

> 反向排序    
> 从最高到最低.  
> 提取三天中排名最高的9条数据.  

