
import time, math 

  

def measure(fn, sizes): 

    for n in sizes: 

        data = list(range(n)) 

        start = time.perf_counter() 

        fn(data) 

        elapsed = (time.perf_counter() - start) * 1000 

        print(f'n={n:>8,}  →  {elapsed:8.3f} ms') 

  

# O(n) function 

def linear(arr): 

    total = 0 

    for x in arr: total += x 

    return total 

  

# O(n²) function 

def quadratic(arr): 

    count = 0 

    for i in arr: 

        for j in arr: 

            count += 1 

    return count 

  

print('--- O(n) ---') 

measure(linear, [1_000, 10_000, 100_000]) 

