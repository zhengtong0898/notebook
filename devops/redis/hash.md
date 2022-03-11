### 二维列表, 适合一对一关系的存储.  
hmset key:id field1 value field2 value field3 value field4 value


### 适合高频一对多关系计算场景  
购物车有多少个商品, 每个商品有多少数量.  
购物车是1, 商品是n, 商品数量是n.  
关系: 购物车与商品是 1:n 关系.    
关系: 商品与商品数量是 1:n 关系.  
层级关系: 购物车是root层, 商品是树干层, 商品数量是叶子层.
> hmset key sub_key_1 sub_key_1_value sub_key_2 sub_key_2_value  
> hmset cart:001 prod:001 10 prod:002 20

