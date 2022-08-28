### DUAL 是什么?  
DUAL 是一个关键字, 用来表达这是一张伪表.  

一条最基本的SQL语句需要有 `SELECT column FROM table` 两个关键字构成.   
但很多时候我们会输入: `SELECT version();` 这种缩减版本的查询.  
要维持一个语句的平衡, 就可以使用`DUAL`关键字来保持这种基本构成.  

```shell
SELECT version() FROM DUAL;
```


&nbsp;  
### null值参与计算、比较  
 `null` 参与计算，结果一定也为`null`.
**解决办法:**
如果字段为 `null` , 那么将 `null` 替换为 `0` 
```shell
SELECT 1 + null FROM DUAL;              -- 输出: null

SELECT 1 + IFNULL(null, 0) FROM DUAL;   -- 输出: 1
```

 `null` 参与比较, 结果一定也为`null`.
**解决办法:**  
`<=>` 安全等于, 可以用来对`null`做比较.  
```shell
SELECT 1 <=> NULL FROM DUAL;      -- 输出: 0
SELECT NULL <=> NULL FROM DUAL;   -- 输出: 1
```

&nbsp;  
### 字符串隐士转换  
字符串存在隐士转换, 如果转换数值不成功, 则视为0.

```shell
SELECT 0 = 'a' FROM DUAL;    -- 输出: 1  
```

&nbsp;  
### 正则表达式 
```shell
SELECT 'shkstart' REGEXP '^s' FROM DUAL;              -- 输出: 1

SELECT column FROM table WHERE column REGEXP '^s';
```  

&nbsp;  
### XOR
当两边都是bool值时, `!=` 就是 `XOR`.  
```shell
SELECT 1 XOR 0 FROM DUAL;     -- 输出: 1
```


&nbsp;  
### 运算符优先级
http://c.biancheng.net/view/7399.html    


&nbsp;  
### count 函数

当 `count` 在遍历过程中遇到的值对象是 `null` 时, 不会统计该值, 因此可能存在统计遗漏.  
解决办法: 使用 `count(*)` 或者 `count(1)`; [这两个是没有区别的.](https://stackoverflow.com/a/181281)  


&nbsp;  
### 聚合函数

> **高亮-1:**  
> `GROUP BY` 中声明的字段可以不出现在 `SELECT` 中.  
> `SELECT columns FROM table GROUP BY column_a` 其中 `columns` 字段,   
> 要么是`GROUP BY`声明的字段、要么是`聚合函数`包字段, 不可以添其他字段(因为只会现实分组中的第一行数据).  
> 
> &nbsp;  
> **高亮-2:**  
> 当使用了 `GROUP BY` 分组函数后,   
> 只能使用 `HAVING` 来做分组后的数据进行条件过滤, 不能使用 `WHERE`.  

- count
- min
- max
- sum
- avg
- group by
- having


&nbsp;  
### SQL执行过程


> **高亮问题: 为什么WHERE的效率比HAVING高?**  
> 1. 从算法层面来看他们两并没有区别, 都是过滤数据.  
> 2. 从执行优先级的角度来看, 由于先执行了`WHERE`, `GROUP BY`计算的数据集小了,   
> `HAVING`计算的数据集也效率, 因此整体的执行效率是会有提升的.  


1. 先 `FROM` 读取表数据(含 `JOIN` ).  
2. 再 `WHERE` 过滤数据.  
3. 再 `GROUP BY` 分组数据.  
4. 再 `HAVING` 来做分组后的数据进行条件过滤.  
5. 再 `SELECT` 来对列进行筛选(指定具体数量的字段, 同时含聚合函数: `MIN/MAX/COUNT/SUM/AVG`).  
6. 再 `DISTINCT` 来对数据再次去重筛选(不能放在聚合函数的前面).  
7. 再 `ORDER BY` 来对数据进行排序.  
8. 再 `LIMIT` 来对数据进行数量限制/分页.  


&nbsp;  
### SELECT 生成多行数据

```shell
mysql> SELECT 1 as column_name FROM DUAL UNION ALL
    -> SELECT 2 FROM DUAL UNION ALL
    -> SELECT 3 FROM DUAL UNION ALL
    -> SELECT 4 FROM DUAL;
+-------------+
| column_name |
+-------------+
|           1 |
|           2 |
|           3 |
|           4 |
+-------------+
4 rows in set (0.00 sec)

```

&nbsp;  
### 查看当前使用的数据库

```shell
SELECT DATABASE() FROM DUAL;
```
