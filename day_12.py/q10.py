
import random, time 

def time_search(arr, target): 

    start = time.perf_counter() 

    result = linear_search(arr, target) 

    elapsed = (time.perf_counter() - start) * 1_000_000  # microseconds 

    return result, elapsed 

  

n = 100_000 

data = list(range(n)) 

_, t = time_search(data, 0) 

print(f'Best  case: {t:.2f} μs  (1 step)') 

_, t = time_search(data, n // 2) 

print(f'Avg   case: {t:.2f} μs  ({n//2} steps)') 

_, t = time_search(data, n - 1) 

print(f'Worst case: {t:.2f} μs  ({n} steps)') 

_, t = time_search(data, -1) 

print(f'Not found:  {t:.2f} μs  ({n} steps)') 

