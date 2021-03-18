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
