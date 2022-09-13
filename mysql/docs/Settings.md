 ### 配置清单  
| 字段名 | 默认值 | 描述 |   
| :--- | :--- | :--- |   
|datadir|C:\Program Files\MariaDB 10.5\data\| 数据库的数据目录 |
|innodb_page_size| 16384 (byte)| 每个 page 的大小|
|[innodb_file_per_table](../tests/innodb_file_per_table/README.md#描述)|On|每个表一个.ibd文件(称为表空间)|
|[innodb_data_file_path](./TableSpace.md)|C:\Program Files\MariaDB 10.5\data\ibdata1| 共享表空间(innodb_file_per_table=Off)时, <br>所有表信息都保存在共享表空间内. |
|tx_isolation|REPEATABLE-READ|可重复读|
