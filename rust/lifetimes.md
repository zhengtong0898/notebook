### 生命周期标识符
- `'a`、`'b`、`'c` 被称为: `lifetime parameters` 
- 函数或方法的参数带上`'a`时被称为: `input lifetimes parameters`
- 函数或方法的返回值带上`'a`时被称为: `output lifetimes parameters`

&nbsp;  
### 生命周期的作用
`Rust`的生命周期所作的所有事情都是为了确保当我们在访问或返回变量时, 变量是有效的.  
`Rust`的生命周期的主要目标是避免悬垂引用([Dangling References](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html#preventing-dangling-references-with-lifetimes)).  


&nbsp;  
### 生命周期的自动推理 

`Rust`的每个`引用`都有一个生命周期标识符, 在大多数的场景下`Rust`都可以通过推理计算出引用变量的有效性, 也就是说当我们在  
使用一个引用时虽然没有提供生命周期标识符, 但是`Rust`通过推理在编译期就帮我们加好了生命周期标识符, 这种行为被成为: 隐式声明.

`Rust`在生命周期上采取推理模式, 当有些场景涉及到 `返回值二义性`、`返回值生命周期长度不确定` 时, 就会要求我们明确指定生命周期标识符.  

> `Rust`在类型处理上也是采取推理模式, 也就是说我们在写代码时很多时候不需要指定类型, 它会根据上下文推理出来某个变量是什么类型;  
但还是有些场景涉及到一个变量可能是这个类型也可能是那个类型`Rust`无法推理的情况, 这时就会要求我们明确指定具体类型.



&nbsp;  
### 生命周期的消除规则
`Rust`的函数对所有`引用`形式参数都必须标注`生命周期标识符: 'a`,  
在写了大量的类似代码后，Rust 社区抱怨声四起，包括开发者自己都忍不  
了了，最终揭锅而起，这才有了生命周期消除的规则, 才有了生命周期的简化.    

1. 当函数有多个形参时, `Rust`为每个形参自动填充不同的生命周期标识符(多个形参的场景不会给返回值填充生命周期标识).
2. 当函数只有一个形参时, `Rust`为形参和返回值自动填充相同的生命周期标识符.  
3. 当函数是一个方法时, 不论有几个形参, `Rust`为返回值自动填充`&self`一样的生命周期标识符.  
    



&nbsp;  
### 生命周期面临的问题

**问题-1:** 跨越作用域(`Scope`)的变量引用问题
```rust
// 错误代码场景, 用于阐述引用的变量有效性.
{
    let r;                  // r变量在这里定义.
    {                     
        let x = 5;          
        r = &x;             // 在这里: x是被引用变量, r是引用变量
    }                       // x(被引用变量)在这里被销毁, 但是r(引用变量)在这里还没有被销毁, 
                            // 因此这里的引用被视为悬垂引用(Dangling References).                    
    println!("r: {}", r); 
}                           // r变量在这里被销毁
```

```rust
// 正确代码使用场景
{
    let x = 5;
    let r = &x;              
    println!("r: {}", r);
}                           // r(引用变量)先被销毁
                            // x(被引用变量)再被销毁
                            // 结论: x的生命周期比r要长, 所有表现都符合教程文字描述的预期.
                            // 关键词: x 比 r 生命周期更长.
```                            
   
```                         
// 也是正确代码的使用场景
{
    let r;
    let x = 5;
    r = &x;
    println!("r: {}", r);
}                           // x(被引用变量)先被销毁
                            // r(引用变量)再被销毁
                            // 结论: 只要在同一个Scope，就表示这两个变量的生命周期一样长.
                            // 关键词: x 和 r 生命周期一样长.  
```

**问题-2:** 二义性问题   
由于下面这个样例代码没有提供任何生命周期标识符, Rust会自动给每个参数创建一个不同的生命周期标识符, 创建后是这样子的:    
`fn longest(x: &'a str, y: &'b str) -> &str {}`  
由于返回值是一个引用, 因此也需要一个生命周期标识符, 但却不是创建, 而是从参数清单里面去选一个分配给返回值引用.    
所以这里的问题是, Rust不知道应该选哪一个生命周期标识符分配给返回值引用.   
```rust
// 错误代码场景 
fn longest(x: &str, y: &str) -> &str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}


fn main() {
    let string1 = String::from("abcd");                 
    let string2 = "xyz";

    let result = longest(string1.as_str(), string2);
    println!("The longest string is {}", result);
}
```
此时就需要人工去制定这个生命周期标识符.  
消除二义性的办法有两个:
- 告诉编译器这些参数的生命周期是一样长的
```rust
// 正确代码场景 
fn longest(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}


fn main() {
    let string1 = String::from("abcd");                 
    let string2 = "xyz";

    let result = longest(string1.as_str(), string2);
    println!("The longest string is {}", result);
}
```
- 告诉编译器谁的生命周期更长   
```rust
struct ImportantExcerpt<'a> {
    part: &'a str,
}

#[allow(dead_code)]
impl<'a> ImportantExcerpt<'a> {
    fn level(&self) -> i32 {
        3
    }
}

#[allow(dead_code)]
impl<'a> ImportantExcerpt<'a> {
    fn announce_and_return_part<'b>(&'a self, announcement: &'b str) -> &'b str 
    where 'a: 'b                                             // 关键在这里, 'a: 'b, 表示'a比'b的生命周期更长.  
                                                             // 由于函数体内返回的具体值是 self.part,  
                                                             // 很明显它self.part的生命周期是从'a出来,
                                                             // 但是返回值却强硬的写了'b, 这个动作叫做生命周期替换,
                                                             // 编译器并不知道'a和'b谁的生命周期更长, 
                                                             //   - 当'b比'a的生命周期更长时, 表明self这个对象都不存在了
                                                             //     self.part就会存在免悬垂引用(Dangling References)的风险.
                                                             //   - 当'a比'b的生命周期更长时, 表明self这个对象仍然存在,
                                                             //     self.part就没有这个风险.  
    {
        println!("Attention please: {}", announcement);
        self.part
    }
}

#[allow(unused)]
fn main() {
    let novel = String::from("Call me Ishmael. Some years ago...");
    let first_sentence = novel.split('.').next().expect("Could not find a '.'");
    let i = ImportantExcerpt {
        part: first_sentence,
    };
}
```


&nbsp;  
### 参考
[Rust Book](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html)  
[Rustonomicon Book](https://doc.rust-lang.org/nomicon/lifetimes.html)  
[Rust 翻译书](https://kaisery.github.io/trpl-zh-cn/ch10-03-lifetime-syntax.html)    
[Rust 中文书](https://course.rs/advance/lifetime/basic.html#%E5%80%9F%E7%94%A8%E6%A3%80%E6%9F%A5)
