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
- BaseModelAdmin

  | 属性 | 描述 | 位置 |
  |---|:---:| :---: |
  |autocompelete_fields = ()| [让外键下拉菜单支持搜索功能](./BaseModelAdmin.md#autocompelete_fields) | 新增、编辑页面 |
  |raw_id_fields = ()| [将下拉菜单替换成文本输入框](./BaseModelAdmin.md#raw_id_fields) | 新增、编辑页面 |
  |fields = None| [表单字段排版](./BaseModelAdmin.md#fields) | 新增、编辑页面 |
  |exclude = None| [表单中排除字段](./BaseModelAdmin.md#exclude) | 新增、编辑页面 |
  |fieldsets = None| [表单字段排版(支持分组)](./BaseModelAdmin.md#fieldsets) | 新增、编辑页面 |
  |form = forms.ModelForm |   | - |
  |filter_vertical = ()| [多对多字段的表单纵向控件装饰](./BaseModelAdmin.md#filter_vertical) | 新增、编辑页面 |
  |filter_horizontal = ()| [多对多字段的表单横向控件装饰](./BaseModelAdmin.md#filter_horizontal) | 新增、编辑页面 |
  |radio_fields = {}|  [将下拉菜单替换成radio控件](./BaseModelAdmin.md#radio_fields) | 新增、编辑页面 |
  |prepopulated_fields = {}| [自动填值功能(需配合slugField字段)](./BaseModelAdmin.md#prepopulated_fields)  | 新增、编辑页面 |
  |formfield_overrides = {}| [表单字段控件替换](./BaseModelAdmin.md#formfield_overrides) | 新增、编辑页面 |
  |readonly_fields = ()|  [只读字段](./BaseModelAdmin.md#readonly_fields) |新增、编辑、`change`列表页面 |
  |ordering = None| [按给定的字段排序显示数据](./BaseModelAdmin.md#ordering)  | `change`列表页面 |
  |sortable_by = None| [仅允许指定字段头拥有排序功能](./BaseModelAdmin.md#sortable_by)  | `change`列表页面 |
  |view_on_site = True| [快捷跳转到于该数据象关的页面hook](./BaseModelAdmin.md#view_on_site) | 编辑页面 |
  |show_full_result_count = True| [搜索右侧计数器的总合数字](./BaseModelAdmin.md#show_full_result_count) | `change`列表页面 |
  |checks_class = BaseModelAdminChecks |  | - |

- ModelAdmin   

  | 属性 | 描述 | 位置 |
  |---|:---:| :---: |
  |list_display = ('\_\_str\_\_',) | [控制字段显示](./ModelAdmin.md#list_display) | `change`列表页面 | 
  |list_display_links = () | [将编辑数据的链接显示在指定字段](./ModelAdmin.md#list_display_links) | `change`列表页面 |
  |list_filter = () | [按分类筛选](./ModelAdmin.md#list_filter) | `change`列表页面 |
  |list_select_related = False | [是否查询关联表](./ModelAdmin.md#list_select_related) | `change`列表页面 | 
  |list_per_page = 100 | [每页显示几行数据](./ModelAdmin.md#list_per_page) | `change`列表页面 |
  |list_max_show_all = 200 | [`show_all`链接显示几行数据](./ModelAdmin.md#list_per_page) | `change`列表页面 |
  |list_editable = () | [同时编辑多行数据](./ModelAdmin.md#list_editable) | `change`列表页面 |
  |search_fields = () | [指定模糊查询字段](./ModelAdmin.md#search_fields) | `change`列表页面 |
  |date_hierarchy = None | [时间分层器](./ModelAdmin.md#date_hierarchy) | `change`列表页面 |
  |save_as = False | [用编辑的表单数据创建新数据](./ModelAdmin.md#save_as)| 编辑页面 |
  |save_as_continue = True | [是否跳转回列表页面](./ModelAdmin.md#save_as_continue)| 编辑页面 |
  |save_on_top = False | [表单上方显示按钮保存栏](./ModelAdmin.md#save_on_top)| 编辑页面 |
  |paginator = Paginator | | - |
  |preserve_filters = True | [保留搜索内容](./ModelAdmin.md#preserve_filters)| `change`列表页面 |
  |inlines = [] | [关联表数据展示](./ModelAdmin.md#inlines) | 编辑页面 |
  | | | -|
  |add_form_template = None| | -|
  |change_form_template = None| | -|
  |change_list_template = None| | -|
  |delete_confirmation_template = None| | -|
  |delete_selected_confirmation_template = None| | -|
  |object_history_template = None| | -|
  |popup_response_template = None| | -|
  | | -|
  |actions = []| [批量更新字段](./ModelAdmin.md#actions) | `change`列表页面 |
  |action_form = helpers.ActionForm| | - |
  |actions_on_top = True| [批量操作栏目位置](./ModelAdmin.md#actions_on_top) | `change`列表页面 |
  |actions_on_bottom = False| [批量操作栏目位置](./ModelAdmin.md#actions_on_top) | `change`列表页面 |
  |actions_selection_counter = True| [批量操作右侧已选中计数器](./ModelAdmin.md#actions) | `change`列表页面 |
  |checks_class = ModelAdminChecks| | - |
