### 模式匹配的变量绑定

这个例子的 `main` 函数将 `Coin::Quarter(UsState::Alaska)` 传递给 `value_in_cents` 函数.  
因此 `coin == Coin::Quarter(UsState::Alaska)`, `match`会命中`Coin::Quarter(state)`,  
这里 `UsState::Alaska` 会被提取出来绑定到 `state` 变量上. 
```rust
#[derive(Debug)]
#[allow(dead_code)]
enum UsState {
    Alabama,
    Alaska,
    // --snip--
}


#[allow(dead_code)]
enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState),
}

fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter(state) => {                           // 这个例子的关键位置在这里.
            println!("State quarter from {:?}!", state);
            25
        }
    }
}

fn main() {
    value_in_cents(Coin::Quarter(UsState::Alaska));
}
```

&nbsp;  
### 什么情况下可以用变量绑定?

由于 `match` 采取的是穷尽式匹配, 案例中使用了 `i32` 类型来匹配,   
`Rust`会要求你把`i32`所有的值都填写出来, 否则在编译器就会报错,  
我不可能将`2147483647`这些多的数字全部列出来, 所以使用变量是唯一出路.  
```rust
// 这是一个编译失败的例子, 用来引导对穷尽式匹配的理解.  
fn match_i32_incorrect() {
    let items = [1, 2, 3, 4, 5];
    for item in items {
        match item {
            1 => println!("1"),
            3 => println!("3")
        }
    }
}

// 正确的使用方法是
fn match_i32_correct() {
    let items = [1, 2, 3, 4, 5];
    for item in items {
        match item {
            1 => println!("1"),
            3 => println!("3"), 
            other => println!("other: {other}")
        }
    }
}
```

通过变量解决了穷尽式匹配问题, 但是又延伸出来另外一个问题,   
如果`other`右边的代码块并不需要使用`other`变量, `Rust`将会报`变量未使用`的报错,      
`Rust`提供了一个解决办法, 就是变量名前面加一个下划线`_other`或直接用一个下划线当作变量`_`.
```rust
fn match_i32_unused_resolution() {
    let items = [1, 2, 3, 4, 5];
    for item in items {
        match item {
            1 => println!("1"),
            3 => println!("3"), 
            _ => ()
        }
    }
}
```

可运行的测试案例代码在[这里](practice/ch2-6-1_match_bind_variable).
