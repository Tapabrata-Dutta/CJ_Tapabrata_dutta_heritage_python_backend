
def linear_search_verbose(arr, target): 

    """Returns (index, steps_taken, percentage_searched)""" 

    n = len(arr) 

    for i in range(n): 

        steps = i + 1 

        if arr[i] == target: 

            pct = (steps / n) * 100 

            return { 

                'found': True, 

                'index': i, 

                'value': arr[i], 

                'steps': steps, 

                'percent_searched': f'{pct:.1f}%', 

                'complexity': f'O({steps}) this run' 

            } 

    return {'found': False, 'steps': n, 'percent_searched': '100%'} 

  

data = list(range(1, 101))   # [1, 2, 3, ..., 100] 

  

print(linear_search_verbose(data, 1))   # Best case: 1 step 

print(linear_search_verbose(data, 50))  # Average: 50 steps 

print(linear_search_verbose(data, 100)) # Worst: 100 steps 

print(linear_search_verbose(data, 999)) # Not found: 100 steps 

