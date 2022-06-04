### 将对象打印出来

使用`#[derive(Debug)]`来为结构体增加通用的`std::fmt::Display`实现，让结构体可以正常打印出来.

```rust
#[derive(Debug)]        // OuterAttribute
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

如果对`#[derive(Debug)]`是什么感兴趣的话, [点击这里](./attributes.md).
