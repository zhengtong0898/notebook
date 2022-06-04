### 关闭未使用代码警告

使用`#[allow(dead_code)]`来关闭未使用的代码的警告.

```rust
#[allow(dead_code)]     
enum PokerSuit {        // 枚举: 扑克
    Clubs,              // 成员: 梅花
    Spades,             // 成员: 黑桃
    Diamonds,           // 成员: 钻石(红方块)
    Hearts,             // 成员: 红心(红桃)
}


#[allow(unused)]
fn main() {
    println!("Hello, world!");
    
    let heart = PokerSuit::Hearts;
    let diamond = PokerSuit::Diamonds;
    
}
```

如果对`#[allow(dead_code)]`是什么感兴趣的话, [点击这里](./attributes.md).
