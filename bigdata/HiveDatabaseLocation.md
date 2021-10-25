### hive 创建的库保存在哪里?

```
# hive
> create database if not exists zt_tmp_20210903;
> show create database zt_tmp_20210903;

+-----------------------------------------------------------------------------------------+
|                   createdb_stmt                                                         |
+-----------------------------------------------------------------------------------------+
| CREATE DATABASE `zt_tmp_20210903`                                                       |
| LOCATION                                                                                |
|   'hdfs://hdp-1.example.com:8020/warehouse/tablespace/external/hive/zt_tmp_20210903.db' |
+-----------------------------------------------------------------------------------------+
```

存储的路径是由 /etc/hive/conf/hive-site.xml 的 hive.metastore.warehouse.external.dir 参数来定义.

```shell
  <property>
    <name>hive.metastore.warehouse.external.dir</name>
    <value>/warehouse/tablespace/external/hive</value>
  </property>
```

数据库结构

```shell
# 注意: 这是一个文件夹
[zt@sandbox ~]$ hadoop fs -ls /apps/hive/warehouse/ | grep "zt_tmp_20210903"
drwxrwxrwx   - zt hdfs     0 2021-09-14 17:52    /apps/hive/warehouse/zt_tmp_20210903.db
```

总结   
创建一个库，体现在 hdfs 中的是一个文件夹，并没有看到一个实体的数据库文件。