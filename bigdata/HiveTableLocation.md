### hive 创建一张表保存在哪里?

1. 创建一张表
```shell
hive> CREATE TABLE `simple_table` (
  `id`    INT,
  `name`   STRING,
  `gender` STRING
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','           -- 声明列与列之间使用','来分隔
STORED AS TEXTFILE;                                     -- 以文本形式存储
```

2. 查看建表语句: 即, 元数据
```shell
hive> show create table `simple_table`;

+---------------------------------------------------------------------------------------------------------------+
|                   createtab_stmt                                                                              |
+---------------------------------------------------------------------------------------------------------------+
| CREATE TABLE `simple_table`(                                                                                  |
|   `id` int,                                                                                                   |
|   `name` string,                                                                                              |
|   `gender` string)                                                                                            |
| ROW FORMAT SERDE                                                                                              |
|   'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'                                                        |
| WITH SERDEPROPERTIES (                                                                                        |
|   'field.delim'=',',                                                                                          |
|   'serialization.format'=',')                                                                                 |
| STORED AS INPUTFORMAT                                                                                         |
|   'org.apache.hadoop.mapred.TextInputFormat'                                                                  |
| OUTPUTFORMAT                                                                                                  |
|   'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'                                                |
| LOCATION                                                                                                      |
|   'hdfs://sandbox-hdp.hortonworks.com:8020/warehouse/tablespace/managed/hive/zt_tmp_20211026.db/simple_table' |
| TBLPROPERTIES (                                                                                               |
|   'bucketing_version'='2',                                                                                    |
|   'transactional'='true',                                                                                     |
|   'transactional_properties'='insert_only',                                                                   |
|   'transient_lastDdlTime'='1635228313')                                                                       |
+---------------------------------------------------------------------------------------------------------------+
20 rows selected (0.176 seconds)

```

3. 观察表路径
```shell
# 有一个线索
[root@sandbox-hdp /]# hadoop fs -find /warehouse | grep "simple_table"
/warehouse/tablespace/managed/hive/zt_tmp_20211026.db/simple_table

# 是目录
[root@sandbox-hdp /]# hadoop fs -ls /warehouse/tablespace/managed/hive/zt_tmp_20211026.db
drwxrwxrwx+  - hive hadoop     0 2021-10-26 06:05 /warehouse/tablespace/managed/hive/zt_tmp_20211026.db/simple_table
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
在 Hive 中创建一张表，并不会产生任何文件，而是仅在 hdfs 中生成一个目录路径。
