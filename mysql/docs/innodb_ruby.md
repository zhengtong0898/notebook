# 注意事项
innodb_ruby 不支持 mysql-8.0


# centos-7.9 安装 mysql-5.7
```shell
# 先确认当前环境的mysql已卸载
rpm -qa | grep -i mysql

# 逐一删除mysql
yum remove mysql-community*

# 删除残留的mysql文件
rm /var/lib/mysql* -rf

# 安装yum源
$ yum localinstall https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm

# 安装 mysql-5.7
$ yum install mysql-community-server -y

# 启动 mysql
$ systemctl start mysqld

# 获取临时密码
$ cat /var/log/mysqld.log | awk -F "root@localhost: " '/A temporary password/{print $NF}' | tail -n 1
I:aW4uC+tZt)
  
# 修改密码
$ mysql -u root -p'I:aW4uC+tZt)'
mysql> set global validate_password_policy=LOW;
mysql> set global validate_password_length=6;
mysql> SET PASSWORD = PASSWORD('123456');

# 连接 mysql
$ mysql -u root -p'123456'
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)

```


# 安装 ruby-2.6
> rvm remove 2.2.4  
> rvm install 2.6.6  

https://tecadmin.net/install-ruby-2-2-on-centos-rhel/  


# 安装 innodb_ruby
https://github.com/jeremycole/innodb_ruby/wiki#quick-start


# 使用 innodb_ruby

- 前置准备工作
    ```shell
    mysql> create database zt;
    mysql> use zt;
    
    -- 创建第一张表
    mysql> CREATE TABLE test_1 (
        `id` INT,
        `name` VARCHAR(20) NOT NULL
    )  CHARACTER SET = 'latin1';
    
    -- 创建第二张表
    mysql> CREATE TABLE test_2 (
        `col1` INT PRIMARY KEY,                -- 1个索引
        `col2` INT NOT NULL,
        `col3` INT NOT NULL,
        `col4` VARCHAR(20),
        INDEX test_2_idx_23 (col2, col3),      -- 1个索引
        INDEX test_2_idx_34 (col3, col4)       -- 1个索引
    );
    ```

- **system-spaces**  
    List all tablespaces available from the system, including some basic stats. This is basically a list of tables:    
    列出所有有效的表的表空间.
    ```shell
    [root@client_2 mysql]# innodb_space -s ibdata1 system-spaces
    name                            pages       indexes     
    (system)                        768         7           
    mysql/engine_cost               6           1           
    mysql/gtid_executed             6           1           
    mysql/help_category             7           2           
    mysql/help_keyword              18          2           
    mysql/help_relation             10          1           
    mysql/help_topic                576         2           
    mysql/innodb_index_stats        6           1           
    mysql/innodb_table_stats        6           1           
    mysql/plugin                    6           1           
    mysql/server_cost               6           1           
    mysql/servers                   6           1           
    mysql/slave_master_info         6           1           
    mysql/slave_relay_log_info      6           1           
    mysql/slave_worker_info         6           1           
    mysql/time_zone                 6           1           
    mysql/time_zone_leap_second     6           1           
    mysql/time_zone_name            6           1           
    mysql/time_zone_transition      6           1           
    mysql/time_zone_transition_type 6           1           
    sys/sys_config                  6           1           
    zt/test_1                       6           1           
    zt/test_2                       8           3   
    ```

- **space-indexes**  
    List all indexes available from the space (system space or file-per-table space):  
    列出具体表空间中的所有索引.
    ```shell
    [root@client_2 mysql]# innodb_space -s ibdata1 -T zt/test_1 space-indexes
    id          name                            root        fseg        fseg_id     used        allocated   fill_factor 
    42          GEN_CLUST_INDEX                 3           internal    1           1           1           100.00%     
    42          GEN_CLUST_INDEX                 3           leaf        2           0           0           0.00%
  
    [root@client_2 mysql]# innodb_space -s ibdata1 -T zt/test_2 space-indexes
    id          name                            root        fseg        fseg_id     used        allocated   fill_factor 
    49          PRIMARY                         3           internal    1           1           1           100.00%     
    49          PRIMARY                         3           leaf        2           0           0           0.00%       
    50          test_2_idx_23                   4           internal    3           1           1           100.00%     
    50          test_2_idx_23                   4           leaf        4           0           0           0.00%       
    51          test_2_idx_34                   5           internal    5           1           1           100.00%     
    51          test_2_idx_34                   5           leaf        6           0           0           0.00% 
    ```
