# 时区的坑

### 问题现象
库里有数据, 但是折线图不显示, 将数据转换成table后发现数据的时间不正确, 往前走了8个小时.  

### 排查过程

- 系统时区
> 1. 检查系统时区, 发现时区不正确.
> 2. 修正系统时区: `cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime`  
> 3. 重启系统后, 发现折线图仍然不显示.


- grafana 全局时区设置  
> 同步设置为Shanghai
> 重启grafana, 发现折线图仍然不显示.


- grafana Dashboard时区设置
> 同步设置为Shanghai
> 重启grafana, 发现折线图仍然不显示.


### 解决办法  
使用 `$__timeGroupAlias` 和 `$__interval`.  
```sql
-- 将
select 时间戳字段 from table;
-- 更改为
select $__timeGroupAlias(时间戳字段, $__interval) from table;
```