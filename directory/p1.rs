pub fn bigger(a: i32, b: i32) -> i32 {
    // Complete this function to return the bigger number!
    // Do not use:
    if a > b{
        return a;
    }
    else{
        return b;
    }
}

fn main(){
    let mut a = 10;
    let mut b = 15;

    println!("{}", bigger(a, b));
    a = 100;
    println!("{}", bigger(a, b));
}