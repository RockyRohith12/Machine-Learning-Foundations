"""
Day 1 - NumPy Fundamentals
Date: 17 June 2026

Topics:
- Array Creation
- 1D, 2D, 3D Arrays
- zeros()
- ones()
- identity()
- arange()
- linspace()
- copy()
"""

import numpy as np

arr1 = np.array([1,2,3,4,5])
print(arr1)

print(type(arr1))

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

arr3 = np.zeros((2,3))
print(arr3)

arr4 = np.ones((3,3))
print(arr4)

arr5 = np.identity(5)
print(arr5)

arr6 = np.arange(10)
print(arr6)

arr7 = np.linspace(10,20,4)
print(arr7)

arr8 = arr7.copy()
print(arr8)

print(arr2.shape)

arr9 = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])

print(arr9.shape)

print(arr9.ndim)
print(arr2.ndim)
print(arr1.ndim)

print(arr1.size)
print(arr9.size)