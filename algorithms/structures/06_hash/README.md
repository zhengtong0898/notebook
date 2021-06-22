&nbsp; 
### HashFunction(哈希函数)
查找场景, 为每个 key 计算出一个存储位置, 被称为 hash_function.

&nbsp;   
### collision(冲突)
写入场景, 当两个 key 被 hash_function 计算得出相同值时, 被称为冲突.   

&nbsp;  
### overflow(溢出)
写入场景, 当 hash_table 没有足够空间存储一个新的 key 时, 被称为溢出.   

&nbsp;  
### LinearProbing(线性探查)
写入场景, 当出现溢出情况时采取邻近(offset + 1)位置存储, 被称为线性探查.  
另外, 当出现溢出的位置是最后一个位置时, (offset + 1) == 0, 所以 hash_table 也被视为环形表.   




TODO:
1. python 的 hash_table 有没有桶的概念?
2. charge_factor 是 loading factor(负载因子) 吗?


参考:

[What is the significance of load factor in HashMap?](https://stackoverflow.com/questions/10901752/what-is-the-significance-of-load-factor-in-hashmap)   
[Hash Table](http://web.engr.oregonstate.edu/~sinisa/courses/OSU/CS261/CS261_Textbook/Chapter12.pdf)   
