import pymysql
import random
import string


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             port=3307,
                             database='practice_covering_index',
                             cursorclass=pymysql.cursors.DictCursor)


with connection:

    # 建表信息
    # create table ifpt (
    #     a int(11) not null primary key auto_increment,
    #     b TEXT not null
    # );

    # 插入 10万 条数据
    with connection.cursor() as cursor:
        for i in range(1, 100000):
            b = "".join(random.sample(string.ascii_letters, 10)) * 100

            sql = ("INSERT INTO `ifpt` (`b`) "
                   "VALUES (%s); ")
            params = (b, )
            cursor.execute(sql, params)
    connection.commit()
