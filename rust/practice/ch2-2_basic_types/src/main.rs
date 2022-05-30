use std::mem::size_of_val;


fn main() {
    let a: u8    = 1;
    let b: i8    = 1;
    let c: u16   = 1;
    let d: i16   = 1;
    let e: u32   = 1;
    let f: i32   = 1;
    let g: u64   = 1;
    let h: i64   = 1;
    let i: u128  = 1;
    let j: i128  = 1;
    let k: usize = 1;   // 若 CPU 是 32 位，那么这个类型是 32 位，
    let l: isize = 1;   // 若 CPU 是 64 位，那么这个类型是 64 位。
    println!("\n==================================int====================================");
    println!("u8:    {:>2}; min: {:>40}; max: {:>40}; ", size_of_val(&a),    u8::MIN,    u8::MAX);
    println!("i8:    {:>2}; min: {:>40}; max: {:>40}; ", size_of_val(&b),    i8::MIN,    i8::MAX);
    println!("u16:   {:>2}; min: {:>40}; max: {:>40}; ", size_of_val(&c),   u16::MIN,   u16::MAX);
    println!("i16:   {:>2}; min: {:>40}; max: {:>40}; ", size_of_val(&d),   i16::MIN,   i16::MAX);
    println!("u32:   {:>2}; min: {:>40}; max: {:>40}; ", size_of_val(&e),   u32::MIN,   u32::MAX);
    println!("i32:   {:>2}; min: {:>40}; max: {:>40}; ", size_of_val(&f),   i32::MIN,   i32::MAX);
    println!("u64:   {:>2}; min: {:>40}; max: {:>40}; ", size_of_val(&g),   u64::MIN,   u64::MAX);
    println!("i64:   {:>2}; min: {:>40}; max: {:>40}; ", size_of_val(&h),   i64::MIN,   i64::MAX);
    println!("u128:  {:>2}; min: {:>40}; max: {:>40}; ", size_of_val(&i),  u128::MIN,  u128::MAX);
    println!("i128:  {:>2}; min: {:>40}; max: {:>40}; ", size_of_val(&j),  i128::MIN,  i128::MAX);
    println!("usize: {:>2}; min: {:>40}; max: {:>40}; ", size_of_val(&k), usize::MIN, usize::MAX);
    println!("isize: {:>2}; min: {:>40}; max: {:>40}; ", size_of_val(&l), isize::MIN, isize::MAX);

    let m: f32 = 0.1;
    println!("\n==================================float 32====================================");
    println!("f32:  {};", size_of_val(&m));
    println!("f32 min: {:>20}; ", f32::MIN);
    println!("f32 max: {:>20}; ", f32::MAX);

    let n: f64 = 0.1;
    println!("\n==================================float 64====================================");
    println!("f64:  {};", size_of_val(&n));
    println!("f64 min: {:>20}; ", f64::MIN);
    println!("f64 max: {:>20}; ", f64::MAX);

    println!("\n==================================char==================================");
    let o = 'z';
    let p = 'ℤ';
    let q = '国';
    let r = '😻';
    println!("char: z: {}", std::mem::size_of_val(&o));
    println!("char: ℤ: {}", std::mem::size_of_val(&p));
    println!("char: 国: {}", std::mem::size_of_val(&q));
    println!("char: 😻: {}", std::mem::size_of_val(&r));

    println!("\n==================================&str==================================");
    let s = "z";
    let t = "ℤ";
    let u = "国";
    let v = "😻";
    println!("char: z: {}", std::mem::size_of_val(&s));
    println!("char: ℤ: {}", std::mem::size_of_val(&t));
    println!("char: 国: {}", std::mem::size_of_val(&u));
    println!("char: 😻: {}", std::mem::size_of_val(&v));

    println!("\n==================================String==================================");
    let w = String::from("z");
    let x = String::from("ℤ");
    let y = String::from("国");
    let z = String::from("😻");
    println!("char: z: {}", std::mem::size_of_val(&w));
    println!("char: ℤ: {}", std::mem::size_of_val(&x));
    println!("char: 国: {}", std::mem::size_of_val(&y));
    println!("char: 😻: {}", std::mem::size_of_val(&z));    
}
