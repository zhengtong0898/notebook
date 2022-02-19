### 常见数据类型存储占位
- numeric  

  |类型|占位|最小值|最大值|
  |---|:---:|---|---|
  |tinyint|1 byte|-128|127|
  |smallint|2 byte|-32768|32767|
  |mediumint|3 byte|-8388608|8388607|
  |int|4 byte|-2147483648|2147483647|
  |bigint|8 byte|-9223372036854775808|9223372036854775807|
  
- float
  
  |类型|占位|
  |---|:---:|
  |float|4 byte|
  |double|8 byte|
  
- date  
 
  |类型|占位|
  |---|:---:|
  |year|1 byte|
  |date|3 byte|
  |time|3 byte|
  |datetime|8 byte|
  |timestamp|4 byte|

- string   
  每个字符大小, 取决于选择了什么[字符集](https://dev.mysql.com/doc/refman/5.7/en/charset-unicode.html).       
  `utf-8`字符集: `ascii`的字符占用`1-byte`, 欧洲/中东语言的字符占用`2-byte`, 中文/韩文/日文的字符占用`3-byte`.  
  `utf8mb4`字符集, 扩展增加`symbols`, `emojis`支持, 字符占用`4-byte`.   
  
  字符串字段的值不是固定大小, 取决于你存储的字符数量 * 字符集类型占位, 下面假设字符串存储都是中文(utf8mb4).   
  
  |类型|占位|最大长度|
  |---|---|---:|
  |char| 3-byte * 文字数量 |-|
  |varchar| 3-byte * 文字数量 + 1-byte 或 2-byte; |65532 byte; 21844个字符|
  |blob, text| 3-byte * 文字数量 + 1-byte; |65532(2^16) byte; 21844个字符|
  |mediumblob, mediumtext| 3-byte * 文字数量 + 1-byte; |16777212(2^24) byte; 5592404个字符|