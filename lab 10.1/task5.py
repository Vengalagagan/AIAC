#time taken to execute this code
import time

start = time.perf_counter()

nums = [i for i in range(1,1000000)]
squares = []
for n in nums:
    squares.append(n**2)

end = time.perf_counter()
print(len(squares))
print(f"Execution time: {end - start:.4f} seconds")
