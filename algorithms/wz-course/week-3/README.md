### 递归和分治
> **分而治之**  
> 将原问题划分成多个规模更小且结构与原问题结构相同的子问题,  
> 先解决这些子问题, 然后再合并其结果, 最终得到原问题的结果.  
> 
> **递归**  
> 递归是一种变成技巧, 它也具有结构相同, 规模不同的特点,  
> 所以涉及到需要使用分而治之思想解决的问题, 比较适合使用递归来实现.  
> 
> **场景**  
> 经典的场景就是 [hadoop 的 mapreduce 编程模型](../../../bigdata/mapreduce-python/README.md),   
> 要求将大数据通过 map 将相同类型的数据提取出来,   
> 然后将它们拆分成更小的规模,   
> 再然后是下发到各个节点使用 reduce 计算出结果,  
> 最后是将各个节点的计算结果汇聚到主节点中进行合并, 得出最终的结果.    

1. [leet-code-0070. 爬楼梯（简单）](./0070-climb-stairs.py)
2. [classic1-cell-duplicate（复杂）](./classic1-cell-duplicate.py)
3. [剑指 Offer 10- I. 斐波那契数列 （简单）](./offer10-fibonacci.py)
4. [剑指 Offer 10- II. 青蛙跳台阶问题（简单）](./offer10-num-ways.py)
5. [面试题 08.01. 三步问题 （简单）](./interview0801-ways-to-step.py)  
6. [剑指 Offer 06. 从尾到头打印链表 （简单）](./offer06-reverse-print.py)
