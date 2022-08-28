

### 当创建一张表时指定varchar(20)是什么意思?  
表示限定插入数据的长度, 也就是说当你插入对应字段的数据大于20个字符时, 会报错说: 
> ERROR 1406 (22001): Data too long for column 'name' at row 1.

- 测试  
    1). 建表
    ```shell
    CREATE TABLE test_1 (  
        `id` int,
        `name` VARCHAR(20) NOT NULL  
    )  CHARACTER SET = 'latin1';  
    ```
  
    2). 插入数据
    ```shell
    -- 插入21个a字母, mysql会抛异常.  
    mysql> insert into test_1 values(1, 'aaaaaaaaaaaaaaaaaaaaa');
    ERROR 1406 (22001): Data too long for column 'name' at row 1
    ```


&nbsp;  
### 关于字符集
1. 默认字符集是`latin-1`, 一个`ascii`字符占用`1byte`.  
2. 当字符集是`utf-8`时, 一个`ascii`字符占用`1byte`.  
3. 当字符集是`utf-8`时, 欧洲/中东语言的字符占用`2-byte`.  
4. 当字符集是`utf-8`时, 中文/韩文/日文的字符占用`3-byte`.  
5. 当字符集是`utf-8mb4`时, 扩展增加`symbols`, `emojis`支持, 字符占用`4-byte`. 


**测试utf-8的字符集**
```shell
CREATE TABLE `test_1` (
    `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` varchar(8000)
) ENGINE=InnoDB DEFAULT CHARSET=utf8; 


// utf-8, ascii字符, 8000 插入 3 次.
// 插入第三条相同数据, 就会分页.
insert into `test_1` select null, repeat('a', 8000);

// utf-8, 欧洲/中东字符, 4000 插入 3 次.
// 插入第三条相同数据, 就会分页.  
insert into `test_1` select null, repeat('ß', 4000);

// utf-8, 中文字符, 2500 插入 3 次.
// 插入第三条相同数据, 就会分页.  
insert into `test_1` select null, repeat('好', 2500);

```


**测试utf-8mb4的字符集**
```shell
$ cat /etc/my.cnf
[mysqld]
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock
symbolic-links=0
log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid

character-set-server = utf8mb4              # 增加这行
collation-server = utf8mb4_unicode_ci       # 增加这行
init_connect = 'SET NAMES utf8mb4'          # 增加这行
character-set-client-handshake = false      # 增加这行

[client]
default-character-set=utf8mb4               # 增加这行

[mysql]
default-character-set=utf8mb4               # 增加这行



CREATE TABLE `test_1` (
    `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` varchar(8000)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; 

// utf-8mb4, ascii字符, 8000 插入 3 次.
insert into `test_1` select null, repeat('a', 8000);

// utf-8mb4, 欧洲/中东字符, 4000 插入 3 次.
// 插入第三条相同数据, 就会分页.  
insert into `test_1` select null, repeat('ß', 4000);

// utf-8mb4, 欧洲/中东字符, 2500 插入 3 次.
// 插入第三条相同数据, 就会分页.  
insert into `test_1` select null, repeat('好', 2500);

// utf-8mb4, 欧洲/中东字符, 2000 插入 3 次.
// 插入第三条相同数据, 就会分页.  
insert into `test_1` select null, repeat('😜', 2000);

CREATE DATABASE zt  CHARACTER SET = utf8mb4;
DROP TABLE `test_1`;


```