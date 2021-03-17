### 如何将orm操作的sql语句打印出来?
> 编辑 Lib/site-packages/django/db/models/sql/compiler.py 文件
```python
# 在文件头部导入logging
import logging
logger = logging.getLogger('django.compiler')

# 找到 class SQLCompiler.execute_sql 方法
# 在 cursor.execute(sql params) 前面增加两行代码.
def execute_sql(self, result_type=MULTI, chunked_fetch=False, chunk_size=GET_ITERATOR_CHUNK_SIZE):
    sql_info = sql % params                 # 在这里添加这行代码
    logger.info("sql: %s" % sql_info)       # 在这里添加这里代码
    cursor.execute(sql, params)             

```

&nbsp;  

### 快速的创建一个项目
```shell
# 创建项目 
django-admin startproject AdminActions

# 创建数据库
python AdminActions/manage.py migrate

# 创建管理员账号
# username: admin
# password: 123456
# email:    123@qq.com 
python AdminActions/manage.py createsuperuser

# 启动项目
python AdminActions/manage.py runserver
```

&nbsp;  

### Django Admin 操作清单
- [批量操作](admin-tutorial/AdminActions/README.md#L10)
- [时间分层器](admin-tutorial/AdminDateHierarchy/README.md)

