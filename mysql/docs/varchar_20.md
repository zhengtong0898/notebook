

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


