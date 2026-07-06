use std::time::Instant;

fn main() {
    let start_time = Instant::now();

    // Loop and count to 200 million
    let mut count = 0;
    for _ in 0..200_000_000 {
        count += 1;
    }

    let execution_time = start_time.elapsed();
    println!("Rust Count: {}", count);
    println!("Rust Time Taken: {:.4?} seconds", execution_time);
}
