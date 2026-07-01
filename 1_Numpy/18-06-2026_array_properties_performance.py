"""
Day 2 - Array Properties & Performance
Date: 18 June 2026

Topics:
- itemsize
- dtype
- astype()
- Memory Comparison
- Speed Comparison
"""

import numpy as np
import sys
import time

arr9 = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])

print(arr9.itemsize)

print(arr9.dtype)

arr9 = arr9.astype('float')

print(arr9.dtype)

# Memory Comparison

list_a = range(100)

arr11 = np.arange(100)

print(sys.getsizeof(87)*len(list_a))
print(arr11.itemsize*arr11.size)

print("\n")

# Speed Comparison

x = range(10000000)
y = range(10000000,20000000)

start_time = time.time()

c = [x+y for x,y in zip(x,y)]

print(time.time()-start_time)

print("\n")

a = np.arange(10000000)
b = np.arange(10000000,20000000)

start_time = time.time()

c = a+b

print(time.time()-start_time)