> 无序的集合  


### set key数量
2^32 - 1 = 4294967295 = 40亿个


### 抽奖活动  
1). 触发参与活动按钮.  
sadd key value  
sadd act:活动编号 用户ID

2). 取消参加
srem act:活动编号 用户ID

3). 抽奖(2个人), 不移除已抽奖人  
> set random member

srandmember act:活动编号 2  

4). 抽奖(2个人), 移除已经抽奖人  
spop 2


### 交集
sinter set_key1 set_key2  

> 朋友圈关注场景    
> 关注了 set_key1 的人(集合A),   
> 关注了 set_key2 的人(集合B),  
> 共同关注: intersection  


### 并集
sunion set_key1 set_key2


### 差集
sdiff set_key1 set_key2
sdiff set_key2 set_key1


### 是否在集合里面
sismember set_key1 zhangsan
sismember set_key2 zhangsan  

> 朋友圈关注场景  
> 我关注的 zhangsan 是不是也关注了 set_key1.


