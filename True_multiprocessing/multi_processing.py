import multiprocessing
import time

def heavy_cpu_task(n):
    count = 0
    for i in range(n):
        count = (count + i) % 999_999
    return count

def main():
    # 600 Million iterations
    N = 600_000_000
    
    # Spawning Processes instead of Threads
    p1 = multiprocessing.Process(target=heavy_cpu_task, args=(N,))
    p2 = multiprocessing.Process(target=heavy_cpu_task, args=(N,))
    
    print("Python multiprocessing starting... (Watch your CPU usage spike to 200%!)")
    start_time = time.time()
    
    # Starts separate OS processes with their own GILs
    p1.start()
    p2.start()
    
    # Wait for both processes to finish
    p1.join()
    p2.join()
    
    end_time = time.time()
    print(f"Python multiprocess execution time: {end_time - start_time:.2f} seconds")

# CRITICAL: This protection block is strictly required for multiprocessing to work
if __name__ == "__main__":
    main()