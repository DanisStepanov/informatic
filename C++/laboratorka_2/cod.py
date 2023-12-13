import math
import time

def sin_n_times_python(n):
    start = time.time()
    for i in range(n):
        result = math.sin(1.57)
    end = time.time()
    return end - start


print(sin_n_times_python(10000000))
print(sin_n_times_python(100000000))
print(sin_n_times_python(1000000000))