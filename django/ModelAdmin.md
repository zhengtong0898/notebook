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