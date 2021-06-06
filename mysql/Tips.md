
&nbsp;  
### docker mysql
```shell
# 下载 centos 系统容器
docker pull centos:7

# 启动 容器.
docker run --name mariadb-container -itd -p 3307:3306 centos:7
 
# 配置 mariadb 容器.
docker exec -it mariadb-container bash

# 配置-1: 增加 mariadb 仓库源.
[root@localhost]# tee /etc/yum.repos.d/mariadb.repo<<EOF
[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.5/centos7-amd64
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1
EOF

# 配置-2: 安装必要的工具和 mariadb-server
[root@localhost]# yum makecache
[root@localhost]# yum install vim epel-release mlocate net-tools MariaDB-server MariaDB-client -y

# 配置-3: 编辑 my.cnf 文件
[root@localhost]# vim /etc/my.cnf

[client-server]

[mysqld]
socket=/var/lib/mysql/mysql.sock
general_log=on
general_log_file=/var/lib/mysql/log/mariadb.log
log-error=/var/lib/mysql/log/mariadb-error.log
pid-file=/var/lib/mysql/mysql.pid

!includedir /etc/my.cnf.d  

# 配置-4: 建立文件夹和分配权限
[root@localhost]# mkdir -p /var/lib/mysql/log
[root@localhost]# chown -R mysql.mysql /var/lib/mysql/log

# 配置-5: 启动服务
[root@localhost]# su -s /bin/bash -c "mysqld" mysql &

# 配置-6: 开启本地验证
#        未设置root密码之前, 在本机可以直接输入mysql进入交互模式.
#        当设置了root密码之后, 输入mysql无法进入交互模式, 必须提供正确的密码.
[root@localhost]# mysql
MariaDB [(none)]> alter user 'root'@'localhost' identified by '123456';
MariaDB [(none)]> exit

# 配置-7: 开启远程验证
[root@localhost]# mysql -uroot -p'123456'
MariaDB [(none)]> create user 'root'@'%' identified by '123456';
MariaDB [(none)]> grant all privileges on *.* to 'root'@'%' with grant option;
MariaDB [(none)]> flush privileges;
MariaDB [(none)]> exit;


# 宿主机(192.168.101.83)连接到容器中的mariadb
macos:~ zt$ /usr/local/opt/mysql-client/bin/mysql --port=3307 -uroot -h 127.0.0.1 -p'123456'
mysql> 


# 局域网中其他设备(192.168.101.85)连接到容器中的mariadb
[root@localhost ~]# mysql -uroot -h 192.168.101.83 --port=3307 -p'123456' 
mysql> 
```


&nbsp;  
&nbsp;   
### 优化器
表里有多个索引, `MySQL`决定使用哪个索引;   
多表关联join时, `MySQL`决定先使用哪个表;   
TODO: 决策细节?


&nbsp;  
&nbsp;   
### 执行器
- 无索引的情况下  
  1. 检查权限
  2. 打开表
  3. 读取第一行数据, 判断匹配条件是否满足(假设不满足).
  4. 读取第二行数据, 判断匹配条件是否满足(假设不满足).
  5. 读取第三行数据, 判断匹配条件是否满足(假设满足, 添加到返回结果集).
  6. 读取第四行数据, 判断匹配条件是否满足(假设满足, 添加到返回结果集).
  7. 读取到最后一行, 将所有匹配条件满足的数据都加入到返回结果集中.
  8. 结果集返回给客户端.
- 有索引的情况  
  TODO: 待补充  


&nbsp;  
&nbsp;   
### Redo Log 和  BinLog
> 参考: 
> https://cloud.tencent.com/developer/article/1497297

当有一条记录需要更新的时候，InnoDB 引擎就会先把记录写到 redo log 里面，并更新内存.  
在系统比较空闲的时候, InnoDB 引擎会将这个操作记录更新到 binlog 里面.  
TODO: redo log 是磁盘文件吗? 在哪里? 
TODO: binlog 是磁盘文件吗? 在哪里?  


&nbsp;  
&nbsp;  
### 快查表
| 字段名 | 描述 |   
| :--- | :--- |
|[Aggregate Function](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_group-concat)|`group_concat` `count` `avg` `max` `min` `sum` `...`|


