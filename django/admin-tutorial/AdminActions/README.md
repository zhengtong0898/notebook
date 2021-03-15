
django 默认情况下提供了批量删除功能, 
除此之外它也提供了
[批量操作](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/actions/#admin-actions)
支持(仅需要稍做配置和少量代码编写). 
下面将围绕 `django.contrib.admin.ModelAdmin.actions` 进行操作.

&nbsp;  

### 批量更新字段状态
[actions app](actions/__init__.py) 通过在 [admin.py](actions/admin.py#L16) 中声明 `actions = [make_published]`, 
`django admin` 会在 `change list` 页面的批量操作下拉菜单中加入该操作指令.
<p align="center">
  <img src="actions/imgs/update_field_status.jpg" alt="Sublime's custom image"/>
</p>

