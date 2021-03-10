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

### [tutorial-03](https://docs.djangoproject.com/en/3.1/intro/tutorial03/)

动态的url配置
> polls/urls.py  
```python
from django.urls import path

from . import views

# 备注:
# django 从 2.0 版本开始就一直采用 path(非正则表达式), 在此之前采用的是 url(正则表达式).
# path是一种 DSL, 用于简化表达式, 但是其内部最终还是要转换回到标准的正则表达式.
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```
> polls/views.py
```python
from django.http import HttpResponse

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

&nbsp;  

编写一个模板页面
> 1. 创建 polls/templates/polls/index.html 模板文件   
> 2. 编辑 polls/views.py 文件, 重构 def index 函数   
> 3. 在 def index 函数中使用 django.shortcuts.render 渲染模板文件   


&nbsp;  

关于报错
> All Django wants is that HttpResponse. Or an exception. 

&nbsp;
  
抛出一个404例子
> 1. 创建 polls/templates/polls/detail.html 模板文件   
> 2. 编辑 polls/views.py 文件, 重构 def detail 函数   
> 3. 在 def detail 函数中使用 orm 查询数据库:   
>    q = Question.objects.get(pk=question_id)   
>    如果q存在, 那么就返回正常的 detail 渲染结果;   
>    如果q不存在, 那么就主动抛出一个Http404异常.   

&nbsp;  

使用模板语言
> 模板语言支持变量引用, orm操作, for, if 等语法操作.  

&nbsp;  
urls中的命名空间
> 在 polls.urls.py 中添加 app_name = 'polls' 变量.    
> 在模板文件中使用 {% url 'polls.detail' question.id %},  
> 其中'polls.detail'对应的是 app_name 和 path中的name='detail',  
> question 是 def detail 中 render 提供的变量: render(request, 'polls/detail.html', {'question': question}) 


&nbsp;  
&nbsp;   
 
 ### [tutorial-04]()
 
 模板关语法介绍
```text
{% csrf_token %}            # Cross Site Request Forgeries(跨站请求伪造)
                            # Django 提供 csrf_token 防止跨站请求伪造机制, 
                            # post表单的模板中, 只要使用 {% csrf_token %} 就可以解决此问题.

{{ forloop }}               # 这是Django提供的一个template tag(数据对象), 用于记录循环统计信息.
                            # forloop.parentloop: 父循环对象.
                            # forloop.counter:    遍历次数, 从1开始.
                            # forloop.revcounter: 集合总数, 从总数开始递减.
                            # forloop.first:      是否第一次.
                            # forloop.last:       是否最后一次.
``` 

