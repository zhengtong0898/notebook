# 教程大纲总结
### [tutorial-01](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)
创建项目
```shell
# django-admin startproject mysite
```

创建app
```shell
python mysite/manage.py startapp polls
```

启动服务
```shell
# python mysite/manage.py runserver
``` 

MVC模型
> django采用 MVC 模型(设计模式)驱动代码的开发,     
> M: Model          对应 django.models   
> V: View           对应 polls.views 业务代码入口   
> C: Controller     对应 polls.urls  url映射入口   

View 和 Controller 配置
> mysite/urls.py     
> polls/urls.py   
> polls/views.py   

&nbsp;  
&nbsp;  

### [tutorial-02](https://docs.djangoproject.com/en/3.1/intro/tutorial02/)

数据库配置
> mysite/settings.py
```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

APP配置
> mysite/settings.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

内置迁移
> 这里的迁移针对 `INSTALLED_APPS` 中的应用, 它们是django内置提供的应用;  
> 由于它们已经预设好 migrations 目录及其内部指令文件, 所以不需要单独执行 makemigration 去生成这些目录和指令文件了.   
> 直接执行 migrate, 读取 migrations/指令文件, 同步到数据库中.  
```
# python mysite/manage.py migrate
```

应用迁移
> 1. 编辑 polls.models.py 文件, 创建(编码) models 对象.
> 2. 编辑 mysite/settings.py 文件, 将 polls 纳入到 INSTALLED_APPS 中.
> 3. 执行 python mysite/manage.py makemigrations, 生成 migration 目录和指令文件.
> 4. 执行 python mysite/manage.py migrate, 读取 migrations/指令文件, 同步到数据库中.

&nbsp;  
操作ORM(Playing with the API)

&nbsp;   
创建django的管理员账户
```shell
# python mysite/manage.py createsuperuser
```

&nbsp;  
将 polls 这个 app 显示到 admin 后台页面中
> polls/admin.py
```python
from django.contrib import admin

from .models import Question

admin.site.register(Question)
``` 

&nbsp;  
&nbsp;  

