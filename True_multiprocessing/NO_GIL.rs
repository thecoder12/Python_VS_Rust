use std::thread;
use std::time::Instant;

fn heavy_cpu_task(n: u64) -> u64 {
    let mut count = 0;
    for i in 0..n {
        count = (count + i) % 999_999;
    }
    count
}

fn main() {
    let n = 600_000_000;

    print!("Rust threads starting... ");
    let start = Instant::now();

    // Spawn two threads running truly in parallel
    let handle1 = thread::spawn(move || heavy_cpu_task(n));
    let handle2 = thread::spawn(move || heavy_cpu_task(n));

    // Join threads and get results (printing ensures the compiler doesn't skip the work)
    let res1 = handle1.join().unwrap();
    let res2 = handle2.join().unwrap();

    let duration = start.elapsed();
    println!("Done!");
    println!("Results to prevent compiler skipping: {} and {}", res1, res2);
    println!("Rust threaded execution time: {:.4?} seconds", duration);
}