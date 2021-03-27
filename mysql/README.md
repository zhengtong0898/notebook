### 查看历史操作记录
查看数据库历史操作之前, 需要先开启日志功能.   


- 日志保存在文件中  
   `windows` 默认保存路径是: `C:\ProgramData\MySQL\`
   ```shell
   > SET GLOBAL log_output = "TABLE";
   > SET GLOBAL general_log = 'ON';
   ```
  
- 日志保存在表中(`mysql.general_log`)  
   ```shell
   SET GLOBAL log_output = "FILE";
   SET GLOBAL general_log = 'ON';
   ```

### 数据库语言

- DML  
  Data Manipulation Language: 数据操纵语言   
  select, insert, update, delete, merge, call, explain plan, lock table 语句都会在这里执行.

- DDL  
  Data Definition Language: 数据库定义语言   
  create, alter, drop, comment, truncate, rename 语句都会在这里执行.
  
- DCL
  Data Control Language: 数据库控制语言   
  grant, revoke 语句都会在这里执行.
  
- TCL
  Transaction Control Language: 事务控制语言
  commit, rollback, savepoint, set transaction 语句都会在这里执行.

