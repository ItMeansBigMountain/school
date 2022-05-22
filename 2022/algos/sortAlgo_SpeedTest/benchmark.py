from functools import wraps
import tracemalloc
from time import perf_counter

# measures the memory usage and time taken to execute a given function
def measure_performance(func):
    '''Measures the memory usage and time taken to execute the provided function'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        print(args)
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()
        print(f'Function: {func.__name__}')
        print(f'Memory usage:\t\t {current / 10**6:.6f} MB \n'
              f'Peak memory usage:\t {peak / 10**6:.6f} MB ')
        print(f'Time elapsed is seconds: {finish_time - start_time:.6f}')
        print(f'{"-"*40}')
        tracemalloc.stop()
    return wrapper