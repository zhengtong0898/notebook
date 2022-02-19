### 字符集
- mysql-server  
  mysql 各环节对象使用的字符集.
  ```shell
  > SHOW VARIABLES LIKE 'character_set_%';
  +--------------------------+----------------------------+
  | Variable_name            | Value                      |
  +--------------------------+----------------------------+
  | character_set_client     | utf8mb4                    |
  | character_set_connection | utf8mb4                    |
  | character_set_database   | latin1                     |
  | character_set_filesystem | binary                     |
  | character_set_results    | utf8mb4                    |
  | character_set_server     | latin1                     |
  | character_set_system     | utf8                       |
  | character_sets_dir       | /usr/share/mysql/charsets/ |
  +--------------------------+----------------------------+
  8 rows in set (0.01 sec)
  ```
  
  mysql 支持的全部字符集
  ```shell
  +----------+-----------------------------+---------------------+--------+
  | Charset  | Description                 | Default collation   | Maxlen |
  +----------+-----------------------------+---------------------+--------+
  | big5     | Big5 Traditional Chinese    | big5_chinese_ci     |      2 |
  | dec8     | DEC West European           | dec8_swedish_ci     |      1 |
  | cp850    | DOS West European           | cp850_general_ci    |      1 |
  | hp8      | HP West European            | hp8_english_ci      |      1 |
  | koi8r    | KOI8-R Relcom Russian       | koi8r_general_ci    |      1 |
  | latin1   | cp1252 West European        | latin1_swedish_ci   |      1 |
  | latin2   | ISO 8859-2 Central European | latin2_general_ci   |      1 |
  | swe7     | 7bit Swedish                | swe7_swedish_ci     |      1 |
  | ascii    | US ASCII                    | ascii_general_ci    |      1 |
  | ujis     | EUC-JP Japanese             | ujis_japanese_ci    |      3 |
  | sjis     | Shift-JIS Japanese          | sjis_japanese_ci    |      2 |
  | hebrew   | ISO 8859-8 Hebrew           | hebrew_general_ci   |      1 |
  | tis620   | TIS620 Thai                 | tis620_thai_ci      |      1 |
  | euckr    | EUC-KR Korean               | euckr_korean_ci     |      2 |
  | koi8u    | KOI8-U Ukrainian            | koi8u_general_ci    |      1 |
  | gb2312   | GB2312 Simplified Chinese   | gb2312_chinese_ci   |      2 |
  | greek    | ISO 8859-7 Greek            | greek_general_ci    |      1 |
  | cp1250   | Windows Central European    | cp1250_general_ci   |      1 |
  | gbk      | GBK Simplified Chinese      | gbk_chinese_ci      |      2 |
  | latin5   | ISO 8859-9 Turkish          | latin5_turkish_ci   |      1 |
  | armscii8 | ARMSCII-8 Armenian          | armscii8_general_ci |      1 |
  | utf8     | UTF-8 Unicode               | utf8_general_ci     |      3 |
  | ucs2     | UCS-2 Unicode               | ucs2_general_ci     |      2 |
  | cp866    | DOS Russian                 | cp866_general_ci    |      1 |
  | keybcs2  | DOS Kamenicky Czech-Slovak  | keybcs2_general_ci  |      1 |
  | macce    | Mac Central European        | macce_general_ci    |      1 |
  | macroman | Mac West European           | macroman_general_ci |      1 |
  | cp852    | DOS Central European        | cp852_general_ci    |      1 |
  | latin7   | ISO 8859-13 Baltic          | latin7_general_ci   |      1 |
  | utf8mb4  | UTF-8 Unicode               | utf8mb4_general_ci  |      4 |
  | cp1251   | Windows Cyrillic            | cp1251_general_ci   |      1 |
  | utf16    | UTF-16 Unicode              | utf16_general_ci    |      4 |
  | utf16le  | UTF-16LE Unicode            | utf16le_general_ci  |      4 |
  | cp1256   | Windows Arabic              | cp1256_general_ci   |      1 |
  | cp1257   | Windows Baltic              | cp1257_general_ci   |      1 |
  | utf32    | UTF-32 Unicode              | utf32_general_ci    |      4 |
  | binary   | Binary pseudo charset       | binary              |      1 |
  | geostd8  | GEOSTD8 Georgian            | geostd8_general_ci  |      1 |
  | cp932    | SJIS for Windows Japanese   | cp932_japanese_ci   |      2 |
  | eucjpms  | UJIS for Windows Japanese   | eucjpms_japanese_ci |      3 |
  +----------+-----------------------------+---------------------+--------+
  40 rows in set (0.04 sec)
  ```

- 库  
  默认字符集(不指定的情况下)是: `latin1`.
  ```shell
  > create database simple_db;
  > show create database simple_db;
  +-------------+------------------------------------------------------------------------+
  | Database    | Create Database                                                        |
  +-------------+------------------------------------------------------------------------+
  | csrfprotect | CREATE DATABASE `simple_db` /*!40100 DEFAULT CHARACTER SET latin1 */ |
  +-------------+------------------------------------------------------------------------+
  1 row in set (0.00 sec)
  ```
  创建库时, 指定字符集.
  ```shell
  > create database simple_db_2 character set utf8mb4 collate utf8mb4_general_ci;
  +-------------+-------------------------------------------------------------------------+
  | Database    | Create Database                                                         |
  +-------------+-------------------------------------------------------------------------+
  | simple_db_2 | CREATE DATABASE `simple_db_2` /*!40100 DEFAULT CHARACTER SET utf8mb4 */ |
  +-------------+-------------------------------------------------------------------------+
  1 row in set (0.01 sec)
  ```

- 表  
  默认字符集(不制定的情况下)是: 继承 `库` 的字符集.
  ```shell
  > use simple_db_2;  
  > create table aa (`sss` int(11) );
  Query OK, 0 rows affected (0.11 sec)
  
  > show create table aa;
  +-------+-------------------------------------------------------------+
  | Table | Create Table                                                |
  +-------+-------------------------------------------------------------+
  | aa    | CREATE TABLE `aa` (                                         |
  |       |   `sss` int(11) DEFAULT NULL                                |
  |       | ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4                     | 
  +-------+-------------------------------------------------------------+
  1 row in set (0.01 sec)
  ```
  创建表时, 指定字符集.
  ```shell
  > create table bb (`sss` int(11)) ENGINE=InnoDB DEFAULT CHARSET=gb2312;
  Query OK, 0 rows affected (0.01 sec)
  
  > show create table bb;
  +-------+-------------------------------------------------------------+
  | Table | Create Table                                                |
  +-------+-------------------------------------------------------------+
  | bb    | CREATE TABLE `bb` (                                         |
  |       |   `sss` int(11) DEFAULT NULL                                |
  |       | ) ENGINE=InnoDB DEFAULT CHARSET=gb2312                      | 
  +-------+-------------------------------------------------------------+
  1 row in set (0.01 sec)
  ```

> 参考  
> https://blog.csdn.net/weixin_34013044/article/details/94125760  
> http://c.biancheng.net/view/2413.html  


