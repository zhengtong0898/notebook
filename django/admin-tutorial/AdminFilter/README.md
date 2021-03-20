默认情况下, `Django Admin`针对 `ManyToMany`字段 采用的是 `select multiple`(html tag 标签) 来显示, 
除此之外 `Django Admin` 还提供了下面两个属性来修饰 `ManyToMany` 字段, 让它支持搜索功能 和 多次操作功能. 
 
&nbsp;  

[admin.ModelAdmin.filter_horizontal](filter_horizontal_/admin.py#L7) 横向选择多个关联对象.
<p align="center">
  <img src="filter_horizontal_/imgs/filter_horizontal.jpg" alt="filter_vertical"/>
</p>

&nbsp;  
   
[admin.ModelAdmin.filter_vertical](filter_horizontal_/admin.py#L8) 纵向选择多个关联对象.   

<p align="center">
  <img src="filter_horizontal_/imgs/filter_vertical.jpg" alt="filter_vertical"/>
</p>

&nbsp;  
### list_display_links
[admin.ModelAdmin.list_display_links](filter_horizontal_/admin.py#L11) 将链接显示在指定字段, 默认是显示在第一个字段.   

<p align="center">
  <img src="filter_horizontal_/imgs/list_display_links.jpg" alt="list_display_links"/>
</p>

&nbsp;   
### list_per_page
[admin.ModelAdmin.list_per_page](filter_horizontal_/admin.py#L13) `change`列表页面, 每页显示多少条数据.     
[admin.ModelAdmin.list_max_show_all](filter_horizontal_/admin.py#L14) 列表页面下方的分页最右侧的`Show all`, 显示多少条数据.      
<p align="center">
  <img src="filter_horizontal_/imgs/list_per_page.jpg" alt="list_per_page"/>
</p>


&nbsp;   
### list_select_related
当访问 `chang` 列表页面时, `Django`默认不会去提取关联表信息(select_related);     
只有一种情况会主动去查询关联表信息, 即: 当`list_display` 集合中包含了外键字段时, 才会主动去查询关联表信息(select_related).   
另外一种情况那就是当 `list_select_related` 属性是 `True` 时, `Django`也会主动去查询关联表信息(select_related).   

`select_related`方法回归到原始`sql`是采用了 `inner join` 把两张表的字段都提取出来;

&nbsp;  
### ordering
[admin.ModelAdmin.ordering](ordering_/admin.py#9) 在 `change` 列表页面, 按给定的字段排序显示数据.  
<p align="center">
  <img src="ordering_/imgs/ordering.jpg" alt="ordering"/>
</p>

&nbsp;  
### sortable_by
[admin.ModelAdmin.sortable_by](ordering_/admin.py#10) 在 `change` 列表页面, 限定可排序字段.   
默认情况下, `Django` 允许所有字段拥有排序功能(即: 点击字段头可以进行该字段的升序或降序功能).  
通过定义 `sortable_by` 字段, 告诉 `Django` 只有这个范围的字段可以排序, 其他字段关闭排序功能.
<p align="center">
  <img src="ordering_/imgs/sortable_by.jpg" alt="sortable_by"/>
</p>