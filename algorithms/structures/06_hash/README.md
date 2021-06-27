### HashTable(哈希表)
哈希表是数组的一种扩展.  
哈希表由数组演化而来.  
哈希表通过依赖`hash_function`和 `collision` 将数据转换成具体的数组位置, 即:   
哈希表底层逻辑是依赖数组的下标快速访问元素的特性.


&nbsp;   
### HashFunction(哈希函数)
hash_function的作用是: 为每个 key 计算出一个索引位置(index).  
> 算法:  
> index = key % hash_table_size  
> 
> 由于最终目的是计算索引位置(index), key 必须是 int 类型.    
> 如果 key 是一个字符串, 则需要特定算法先将其转换成 int 然后才能进行索引位置计算.


&nbsp;   
### Collision(哈希冲突)
哈希冲突指的是, 两个不同的值, 通过 `hash_function` 计算后得出相同的索引位置.  
再好的哈希函数也无法避免哈希冲突，即便像业界著名的 MD5、SHA、CRC 等哈希算法，也无法完全避免哈希冲突.   
解决哈希冲突的常用办法有两种: `open address(开放寻址法)` 和 `chaining(链表法)`.  


#### OpenAddress(开放寻址法)
一旦出现哈希冲突，就通过重新探测新位置的方法来解决冲突，典型的探测方法有三种: 
1. linear probing(线性探测法)  
   当向哈希表插入数据时，如果某个数据经过哈希函数计算之后，对应的索引位置已经被占用，  
   就从这个位置开始在数据中一次往后查找，直到找到空闲位置为止.  
   需要注意的是，当查找到数组最后一个元素依旧没有找到空闲位置时, 会从第0个索引位置继续查找  
   直到找到空闲位置为止, 所以 `HashTable` 也被视为环形表.  
&nbsp;  
2. quadratic probing(二次探测法)  
   二次探测法与线性探测法很像，线性探测法的探测步长是1，而二次探测法的探测步长是原来的 `二次方`，例如：  
   线性探测的下标序列是: `hash(key)+0`，`hash(key)+1`，`hash(key)+2`，`hash(key)+3`...  
   二次探测的下标序列是: `hash(key)+0^2`，`hash(key)+1^2`，`hash(key)+2^2`，`hash(key)+3^2`...  
&nbsp;   
3. double hashing(双重哈希法)   
   准备多个 `hash_function`, 如果第一个哈希函数计算得到的索引位置已被占用，  
   再用第二个哈希函数重新计算索引位置，以此类推，直到找到空闲的索引位置为止。


#### Chaining(链表法)
`hash_function`计算得出的索引位置, 如果该索引位置空闲时, 创建一个链表将值写入链表，将链表写入索引位置(这个索引位置也被成为`slot(槽)`).  
`hash_function`计算再次得出相同索引位置时(哈希冲突), 直接在该索引位置的链表中写入值.  
这两个动作描述的是链表法的写入场景，时间复杂度是O(1).  
当要查找、删除数据时，同样需要通过 `hash_function` 计算出对应的索引位置(`slot(槽)`)，然后遍历链表找到匹配的数据.  

> `hash_function`计算得出索引位置, 找到具体的`slot`, 时间复杂度是O(1).  
> 但是要找到具体的值, 取决于 `slot` 的长度,   
> 当 `slot` 长度不大时, 时间复杂度是O(1).  
> 当 `slot` 很大时, 时间复杂度是O(n).  
> 当 `slot` 很大时, 当 `slot` 是跳表结构时, 时间复杂度时 O(logn).  


&nbsp;  
### LoadFactor(装载因子)
装载因子越大，说明链表长度越长，哈希表的性能就越低.  
> 算法  
> load_factor = hash_size / slots



&nbsp;  
### Overflow(溢出)
写入场景, 当 hash_table 没有足够空间存储一个新的 key 时, 被称为溢出.   

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
