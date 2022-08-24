
### 大小写规范
库名、表名、表别名、字段名、字段别名都用小写。  

SQL关键字、函数名、绑定变量都用大写。  


&nbsp;  
**表别名**  
下面这条语句中的 `st` 就是表的别名. 
```shell
select * from student as st;
``` 

&nbsp;  
**字段别名**  
下面这条语句中的 `` 就是字段别名.   
```shell
select id as `identify` from student;
```


&nbsp;  
### 引号规范
字符串、日期时间、需要使用单引号.  



&nbsp;  
### 着重号  
当字段名、表明出现与关键字相同时, 就需要使用着重号. 

```shell
-- 错误的语法, 由于ORDER是一个关键字, 所以无法通过这种方式去查询ORDER表.
SELECT * FROM ORDER;

-- 解决办法, 使用着重号.
SELECT * FROM `order`;
```  

