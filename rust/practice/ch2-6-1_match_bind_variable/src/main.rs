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
        Coin::Quarter(state) => {
            println!("State quarter from {:?}!", state);
            25
        }
    }
}


fn match_i32_incorrect() {
    // let items = [1, 2, 3, 4, 5];
    // for item in items {
    //     match item {
    //         1 => println!("1"),
    //         3 => println!("3")
    //     }
    // }
}


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


fn main() {
    value_in_cents(Coin::Quarter(UsState::Alaska));
    match_i32_correct();
    match_i32_incorrect();
    match_i32_unused_resolution();
}