import threading
import time

def heavy_cpu_task(n):
    count = 0
    for i in range(n):
        # Modulo forces Python to compute every iteration, preventing optimizations
        count = (count + i) % 999_999
    return count

def main():
    # 600 Million iterations
    N = 600_000_000
    
    t1 = threading.Thread(target=heavy_cpu_task, args=(N,))
    t2 = threading.Thread(target=heavy_cpu_task, args=(N,))
    
    print("Python threads starting... (Grab a coffee, this will take a bit)")
    start_time = time.time()
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    end_time = time.time()
    print(f"Python threaded execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()