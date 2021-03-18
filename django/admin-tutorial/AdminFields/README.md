[admin.ModelAdmin.exclude](exclude_/admin.py#L18) 属性作用于 `add` 和 `change` 表单页面中(服务于表单字段), 
表示: 定义在 `exclude` 集合中的字段, 将不会显示在表单中.
  <p align="center">
    <img src="exclude_/imgs/exclude_indirectly_void_form_validation.jpg" alt="exclude"/>
  </p>

&nbsp;  

[admin.ModelAdmin.fields](fields_/admin.py#L8) 属性作用于 `add` 和 `change` 表单页面(控制于表单字段);   
表单中仅显示那些定义在 `fields` 集合中的字段, `fields`除了控制字段的显示之外, 还可以控制字段的排版(顺序, 分行).
    <p align="center">
    <img src="fields_/imgs/fields_order_and_splitbyline.jpg" alt="fields"/>
  </p>

