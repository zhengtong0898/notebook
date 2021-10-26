### hive 创建的库保存在哪里?

1. 创建一个数据库
```shell
> create database if not exists zt_tmp_20211026;
```

2. 查看建表语句: 即, 元数据
```shell
> show create database zt_tmp_20211026;

+--------------------------------------------------------------------------------------------------+
|                   createdb_stmt                                                                  |
+--------------------------------------------------------------------------------------------------+
| CREATE DATABASE `zt_tmp_20210903`                                                                |
| LOCATION                                                                                         |
|   'hdfs://sandbox-hdp.hortonworks.com:8020/warehouse/tablespace/managed/hive/zt_tmp_20211026.db' |
+--------------------------------------------------------------------------------------------------+
```

3. 观察库路径
```shell
# 有两个线索.
[root@sandbox-hdp /]# hadoop fs -find /warehouse | grep "zt_tmp_20211026"
/warehouse/tablespace/external/hive/zt_tmp_20211026.db
/warehouse/tablespace/managed/hive/zt_tmp_20211026.db

# 它们都是目录
[root@sandbox-hdp /]# hadoop fs -ls /warehouse/tablespace/external/hive/
drwxrwxrwx+  - hive hadoop          0 2021-10-26 05:22 /warehouse/tablespace/external/hive/zt_tmp_20211026.db
[root@sandbox-hdp /]# hadoop fs -ls /warehouse/tablespace/managed/hive/
drwxrwxrwx+  - hive hadoop          0 2021-10-26 05:22 /warehouse/tablespace/managed/hive/zt_tmp_20211026.db

```

4. 目录结构的创建依据
```shell
[root@sandbox-hdp /]# vi /etc/hive/conf/hive-site.xml

<configuration  xmlns:xi="http://www.w3.org/2001/XInclude">

    ...

    <!-- 内部表目录结构依据 -->
    <property>
      <name>hive.metastore.warehouse.dir</name>
      <value>/warehouse/tablespace/managed/hive</value>
    </property>


    <!-- 外部表目录结构依据 -->
    <property>
      <name>hive.metastore.warehouse.external.dir</name>
      <value>/warehouse/tablespace/external/hive</value>
    </property>
    
    ...
    
</configuration>
```


5. 结论   
在 Hive 中创建一个库，并不会产生任何文件，而是仅在 hdfs 中生成两个目录路径。  
一个目录路径是外部表路径，一个目录路径是内部表路径。
