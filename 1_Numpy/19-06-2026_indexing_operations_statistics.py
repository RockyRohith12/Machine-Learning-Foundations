"""
Day 3 - Indexing, Operations & Statistics
Date: 19 June 2026

Topics:
- Indexing
- Slicing
- Iteration
- nditer()
- Arithmetic Operations
- Matrix Multiplication
- Statistical Functions
"""

import numpy as np

arr1 = np.array([1,2,3,4,5])

arr12 = np.arange(24).reshape(6,4)

print(arr12)

# Indexing

print(arr1[3])
print(arr1[2:4])
print(arr1[-1])

# Slicing

print(arr12[:2])

print(arr12[:,2])

print(arr12[4:6,2:4])

# Iteration

for i in arr12:
    print(i+5)

for i in np.nditer(arr12):
    print(i)

# Arithmetic Operations

arr13 = np.array([1,2,3,4,5])
arr14 = np.array([6,7,8,9,10])

print(arr13-arr14)
print(arr13+arr14)
print(arr13*arr14)
print(arr13*2)

print(arr14>=7)

# Matrix Multiplication

arr15 = np.arange(6).reshape(2,3)
arr16 = np.arange(6,12).reshape(3,2)

print(arr15.dot(arr16))

# Statistics

arr17 = np.array([[6,7],[8,9],[10,11]])

print(arr17.max())
print(arr17.min())

print(arr17.min(axis=1))

print(arr17.sum())
print(arr17.sum(axis=1))

print(arr17.mean())
print(arr17.std())

print(np.sin(arr17))
print(np.exp(arr17))