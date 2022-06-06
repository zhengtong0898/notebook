### AssociatedFunctions: 关联函数

> 参考资料  
> https://course.rs/basic/method#%E5%85%B3%E8%81%94%E5%87%BD%E6%95%B0   
> https://doc.rust-lang.org/book/ch05-03-method-syntax.html#associated-functions  

`Rust`的`关联函数`等价于`Python`中的静态方法.  
`Rust`的`关联函数`是为了让相关的函数内聚在一个结构对象中, 有利于代码组织和管理.  
`Rust`的`关联函数`的特点是不需要声明`&self`作为第一个形式参数.    
`Rust`的`关联函数`采用`对象::关联函数`来调用.  
