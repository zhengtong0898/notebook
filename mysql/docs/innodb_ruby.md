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

观察一页16kb, 当插入的数据大于16kb, 页会怎么表现.
1. 如果一页只能存放一条时, 会把这条数据当作是blob, 不会增加索引页来存储, 而是增加blob页来存储.  
2. 当一页存储能存储两条或两条以上时, 数据就会存放在index页中.
3. 当隶属于该页中的所有行的所有列的值加起来大于16kb时, mysql会自动增加一页来存储后续的行.  


- 前置准备工作
    ```shell
    mysql> create database zt;
    mysql> use zt;
    
    mysql> CREATE TABLE `test_1` (
        `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
        `name` varchar(8000)
    ) ENGINE=InnoDB;  
    ```

- **space-page-type-regions(关键)**  
    Iterate through all pages in a space and print a summary of page types coalesced into “regions” of same-type pages:    
    显示test_2表都有哪些类型的页, 每个页的其实位置，页的数量.  
    ```shell
    [root@client_2 mysql]# innodb_space -f zt/test_1.ibd space-page-type-regions
    start       end         count       type                
    0           0           1           FSP_HDR             
    1           1           1           IBUF_BITMAP         
    2           2           1           INODE               
    3           5           3           INDEX               
    6           7           2           FREE (ALLOCATED)  
    ```


- **space-index-pages-summary(关键)**  
    The space-index-pages-summary mode will give us a count of records in each page.
    page 这一列对应的是上面的 space-page-type-regions 的 start 和 end 范围.  
    ```shell
    # 插入数据之前
    [root@client_2 mysql]# innodb_space -f zt/test_1.ibd space-index-pages-summary
    page        index   level   data    free    records 
    3           63      0       0       16252   0       
    4           0       0       0       16384   0       
    5           0       0       0       16384   0       

    # 插入一条数据
    mysql> insert into `test_1` select null, repeat('a', 8000);
    [root@client_2 mysql]# innodb_space -f zt/test_1.ibd space-index-pages-summary
    page        index   level   data    free    records 
    3           63      0       8025    8227    1       
    4           0       0       0       16384   0       
    5           0       0       0       16384   0   
  
    # 插入第二条数据
    mysql> insert into `test_1` select null, repeat('a', 8000);
    [root@client_2 mysql]# innodb_space -f zt/test_1.ibd space-index-pages-summary
    page        index   level   data    free    records 
    3           63      0       16050   202     2       
    4           0       0       0       16384   0       
    5           0       0       0       16384   0   
  
    # 插入第三条数据
    # 平衡二叉树，开始出现分叉
    mysql> insert into `test_1` select null, repeat('a', 8000);
    [root@client_2 mysql]# innodb_space -f zt/test_1.ibd space-index-pages-summary
    page        index   level   data    free    records 
    3           63      1       28      16224   2       
    4           63      0       8025    8227    1       
    5           63      0       16050   202     2
  
    # 插入第四条数据
    mysql> insert into `test_1` select null, repeat('a', 8000);
    [root@client_2 mysql]# innodb_space -f zt/test_1.ibd space-index-pages-summary
    page        index   level   data    free    records 
    3           63      1       42      16210   3       
    4           63      0       8025    8227    1       
    5           63      0       16050   202     2       
    6           63      0       8025    8227    1       
    7           0       0       0       16384   0   
    ```


- **space-page-type-summary**  
    Iterate through all pages and print a summary of total counts of pages by type:  
    遍历所有与test_2表相关的页, 并将各类型的页给列出来, 统计每个类型的页的数量.  
    ```shell
    [root@client_2 mysql]# innodb_space -s ibdata1 -T zt/test_2 space-page-type-summary
    type                count       percent     description         
    INDEX               3           37.50       B+Tree index        
    ALLOCATED           2           25.00       Freshly allocated   
    FSP_HDR             1           12.50       File space header   
    IBUF_BITMAP         1           12.50       Insert buffer bitmap
    INODE               1           12.50       File segment inode  
    ```
