### list_display
[admin.ModelAdmin.list_display](follow-tutorial/mysite/polls/admin.py#36) 
该属性用于控制字段显示, 即`change`列表的每行显示几个字段.   
<p align="center">
  <img src="follow-tutorial/mysite/list_display.jpg" alt="list_display"/>
</p>

&nbsp;   
&nbsp;   

### search_fields
[admin.ModelAdmin.search_fields](follow-tutorial/mysite/polls/admin.py#44) 
该属性用于模糊搜索指定字段, 模糊搜索在`sql`中采用的是 `like '%search%'`语法.   
<p align="center">
  <img src="follow-tutorial/mysite/search_fields.jpg" alt="search_fields"/>
</p>

&nbsp;  
&nbsp;   
### list_filter
[admin.ModelAdmin.list_filter](follow-tutorial/mysite/polls/admin.py#39) 
该属性用于指定字段分类筛选, 最佳实践适用于`bool`类型字段, 时间类型字段, 和少量`choices`类型字段.  
<p align="center">
  <img src="follow-tutorial/mysite/list_filter.jpg" alt="list_filter"/>
</p>


&nbsp;  
&nbsp;   

### actions
[admin.ModelAdmin.actions](admin-tutorial/AdminActions/actions/admin.py#L16)
该属性用于控制 `批量操作` 功能的表现;  
默认情况下, `批量操作栏` 会有一个 `delete selected` 功能; 除此之外也可以通过将函数或方法添加到`actions`集合中, 让`批量操作`下拉菜单拥有其他批量操作功能.   

`actions` 的值类型是 `None` 时, 表示不显示批量操作栏.     
`actions` 的值类型是 `list` 或 `tuple` 时, 显示批量操作栏.   
`actions` 的值类型是 `list` 或 `tuple` 时, 同时元素是字符串时, `Django`会通过反射语法来读取`self`的对应方法.
 
 - [`actions = [make_published, ]`](admin-tutorial/AdminActions/actions/admin.py#L16)
    <p align="center">
      <img src="admin-tutorial/AdminActions/actions/imgs/update_field_status.jpg" alt="update_field_status"/>
    </p>

- [`actions = ['make_published', ]`](admin-tutorial/AdminActions/actions_method/admin.py#L14)
    <p align="center">
      <img src="admin-tutorial/AdminActions/actions_method/imgs/update_field_status_by_method.jpg" alt="update_field_status_by_method"/>
    </p>

- [`actions = None`](admin-tutorial/AdminActions/actions_method/admin.py#L12)
    <p align="center">
      <img src="admin-tutorial/AdminActions/actions_method/imgs/hide_batch_operator.jpg" alt="hide_batch_operator"/>
    </p>

&nbsp;  
&nbsp;  
### actions_on_top
[admin.ModelAdmin.actions_on_top](admin-tutorial/AdminActions/actions_method/admin.py#L18)    
[admin.ModelAdmin.actions_on_bottom](admin-tutorial/AdminActions/actions_method/admin.py#L19)   
这两个属性分别控制`change`列表页面的批量操作栏目显示的位置, 它们两通常需要同时配置(一个为`True`, 另外一个为`False`).   
`actions_on_top=True`时, 表示在表单的上方显示批量操作栏目.  
`actions_on_top=False`时, 隐藏表单上方的批量操作栏目.   
`actions_on_bottom=True`时, 表示在表单的下方显示批量操作栏目.   
`actions_on_bottom=False`时, 隐藏表单下方的批量操作栏目.   

- 情况1   
  `actions_on_top=True`   
  `actions_on_bottom=True`   
  当两个属性都是`True`时, 表示在`change`列表的上方和下方都显示批量操作栏目(即: 显示两个一样的批量操作栏目).   
- 情况2
  `actions_on_top=False`      
  `actions_on_bottom=False`   
  当两个属性都是`False`时, 表示在`change`列表页面不显示批量操作栏目.   
- 情况3
  `actions_on_top=True`      
  `actions_on_bottom=False`   
  仅在`change`列表的上方显示操作栏目.   
- 情况4   
  `actions_on_top=True`      
  `actions_on_bottom=False`   
  仅在`change`列表的下方显示操作栏目.
  
  <p align="center">
    <img src="admin-tutorial/AdminActions/actions_method/imgs/action_on_bottom.jpg" alt="action_on_bottom"/>
  </p>
  

&nbsp;  
&nbsp;   
### actions_selection_counter
[admin.ModelAdmin.actions_selection_counter](admin-tutorial/AdminActions/actions_method/admin.py#L16)
该属性用于控制批量操作右侧已选中计数器的显示隐藏开关;     
`actions_selection_counter=True`时, 表示显示已选中的计数.     
`actions_selection_counter=False`时, 表示隐藏已选中的计数.      
<p align="center">
    <img src="admin-tutorial/AdminActions/actions/imgs/selected_counter.jpg" alt="selected_counter"/>
</p>
