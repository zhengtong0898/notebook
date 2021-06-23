&nbsp; 
### HashFunction(哈希函数)
查找场景, 为每个 key 计算出一个存储位置, 被称为 hash_function.

> hash_function 算法  
> key 期望的是一个 int 类型, 因为只有 int 类型才可以做有效的求余.  
> index = key % hash_table_size  

&nbsp;   
### Collision(冲突)
写入场景, 当两个 key 被 hash_function 计算得出相同值时, 被称为冲突.  

> 冲突有三种情况   
> 1. 实际值相同, 采取 `忽略` 策略.
> 2. 实际值不同, 采取 `线性探查` 策略.
> 3. 出现`Overflow`, 采取 `Rehashing` 策略.


&nbsp;  
### Overflow(溢出)
写入场景, 当 hash_table 没有足够空间存储一个新的 key 时, 被称为溢出.   

&nbsp;  
### LinearProbing(线性探查: HashTable._collision_resolution)
写入场景, 当出现溢出情况时采取邻近(offset + 1)位置存储, 被称为线性探查.  
另外, 当出现溢出的位置是最后一个位置时, (offset + 1) == 0, 所以 hash_table 也被视为环形表.   

&nbsp;  
### Rehashing(哈希表扩容)
写入场景, 当哈希表因为 `Overflow` 而无法写入当前数据时, `Rehasing`会按照 `质数` 规律来扩容. 

> Rehashing 扩容算法  
> double_size = hash_table_size * 2  
> hash_table_size = next_prime(double_size)
> 
> 质数  
> 一个只能被 数字1 和 自己 整除的数, 被称为质数;   
> 质数的范围: [2, 3, 5, 7, 11, 13, 17, ...]   
> 为什么 9 不是质数, 因为它可以被 1, 3, 9 整除, 超出了定义范围.  



&nbsp;  
&nbsp;  
TODO:
1. python 的 hash_table 有没有桶的概念?
2. charge_factor 是 loading factor(负载因子) 吗?


参考:  
[hash_table.py](https://github.com/TheAlgorithms/Python/blob/master/data_structures/hashing/hash_table.py)  
[What is the significance of load factor in HashMap?](https://stackoverflow.com/questions/10901752/what-is-the-significance-of-load-factor-in-hashmap)   
[Hash Table](http://web.engr.oregonstate.edu/~sinisa/courses/OSU/CS261/CS261_Textbook/Chapter12.pdf)   
