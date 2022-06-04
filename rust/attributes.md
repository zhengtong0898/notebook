### 背景

第一次看到`#[allow(dead_code)]`会很好奇它是个什么东西,  
记得以前看 [Rust官方教程](https://doc.rust-lang.org/book/) 并没有单独描述它, 现在看 [中文书](https://course.rs/about-book.html) 也没有单独描述它,   
它像是有一层透明的面纱, 我既想了解它, 但又不知道用什么关键词去搜索它,   


也许是以前资料不充分, 总之现在找到了[说明](https://doc.rust-lang.org/reference/attributes.html), 这个东西叫做**Attributes**.  
由于它本身涵盖了非常多的内容, 我一时半会消化不掉,   
以后有机会涉及到更多这块知识再花时间跟它慢慢磨,   
为了节省时间只能给它做一个简单的总结和概括.   

&nbsp;  
### Attributes 概述
`Attributes`就像`Python`中的装饰器, 为目标对象附加特定的能力, 比如说:  

- `cfg`的[代码条件编译](https://doc.rust-lang.org/rust-by-example/attribute/cfg.html)  
- 标记当前项目的元数据信息(比如说: 版本号、当前项目作为一个库)  
- 禁用`lints`(就像`Python`中的`pylint`)
- 启用编译器功能（宏、全局导入等）
- 链接到外部三方库
- 将函数标记为单元测试  
- 将函数标记为基准中的一部分

&nbsp;  
### Attributes 表达形式

|表达形式|术语|描述|
|---|---|---|
|`#[Attr]`|OuterAttribute|定义在对象的头上, 像`Python`的装饰器一样.<br/>|  
|`#![Attr]`|InnerAttribute|可以定义在文件内头部位置<br>可以定义在函数内头部位置|

&nbsp;  
### OuterAttribute 样例代码
定义在对象的头上, 像`Python`的装饰器一样.
```rust
#[derive(Debug)]        // OuterAttribute
#[allow(dead_code)]     // OuterAttribute
enum PokerSuit {        // 枚举: 扑克
    Clubs,              // 成员: 梅花
    Spades,             // 成员: 黑桃
    Diamonds,           // 成员: 钻石(红方块)
    Hearts,             // 成员: 红心(红桃)
}


fn main() {
    println!("Hello, world!");
    
    let heart = PokerSuit::Hearts;
    let diamond = PokerSuit::Diamonds;

    println!("{:?}", heart);
    println!("{:?}", diamond);
}
```

&nbsp;  
### InnerAttribute 样例代码
可以定义在文件内头部位置
```rust
#![crate_type = "lib"]               // 生命当前文件是一个库


fn util_function() {
  
}
```

&nbsp;  
可以定义在函数内头部位置
```rust
fn some_unused_variables() {
  #![allow(unused_variables)]         

  let x = ();
  let y = ();
  let z = ();
}


fn main() {
  some_unused_variables();
}
```

&nbsp;  
### 参考链接
[rust-by-example:attribute](https://doc.rust-lang.org/rust-by-example/attribute.html)  
[rust-reference:attributes](https://doc.rust-lang.org/reference/attributes.html?search=dead_code)  
[rust-reference:attributes:built-in attributes index](https://doc.rust-lang.org/reference/attributes.html#built-in-attributes-index)  
[rust-reference:diagnostics](https://doc.rust-lang.org/reference/attributes/diagnostics.html#lint-check-attributes)  
[rust-reference:Procedural Macros](https://doc.rust-lang.org/reference/procedural-macros.html)  

