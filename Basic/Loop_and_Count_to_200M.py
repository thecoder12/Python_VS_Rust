import time

start_time = time.time()

# Loop and count to 200 million
count = 0
for i in range(200_000_000):
    count += 1

execution_time = time.time() - start_time
print(f"Python Count: {count}")
print(f"Python Time Taken: {execution_time:.4f} seconds")