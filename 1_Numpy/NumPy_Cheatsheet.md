# NumPy Cheat Sheet

> A quick reference guide for essential NumPy operations used in Data Analysis and Machine Learning.

---

# Import NumPy

```python
import numpy as np
```

---

# Creating Arrays

```python
np.array([1,2,3])

np.array([[1,2],[3,4]])

np.zeros((3,3))

np.ones((2,4))

np.eye(3)

np.arange(0,10)

np.arange(0,20,2)

np.linspace(0,1,5)

np.random.rand(3,3)

np.random.randint(1,100,10)
```

---

# Array Attributes

```python
arr.shape

arr.ndim

arr.size

arr.dtype

arr.itemsize

arr.nbytes
```

---

# Indexing & Slicing

```python
arr[0]

arr[-1]

arr[2:6]

arr[:5]

arr[::2]

arr[::-1]

arr[1,2]

arr[:,1]

arr[1,:]
```

---

# Reshaping Arrays

```python
arr.reshape(3,4)

arr.flatten()

arr.ravel()

arr.transpose()

arr.T
```

---

# Joining Arrays

```python
np.concatenate((a,b))

np.vstack((a,b))

np.hstack((a,b))

np.column_stack((a,b))
```

---

# Splitting Arrays

```python
np.split(arr,2)

np.vsplit(arr,2)

np.hsplit(arr,2)
```

---

# Mathematical Operations

```python
arr + 10

arr - 5

arr * 2

arr / 3

arr ** 2

np.sqrt(arr)

np.exp(arr)

np.log(arr)

np.sin(arr)

np.cos(arr)
```

---

# Statistical Functions

```python
np.mean(arr)

np.median(arr)

np.std(arr)

np.var(arr)

np.min(arr)

np.max(arr)

np.sum(arr)

np.prod(arr)

np.argmin(arr)

np.argmax(arr)
```

---

# Sorting & Searching

```python
np.sort(arr)

np.argsort(arr)

np.where(arr > 10)

np.unique(arr)
```

---

# Boolean Masking

```python
arr[arr > 10]

arr[(arr > 5) & (arr < 20)]

arr[arr % 2 == 0]
```

---

# Broadcasting

```python
arr + 5

arr * 10

matrix + vector
```

---

# Random Module

```python
np.random.seed(42)

np.random.rand()

np.random.randn()

np.random.randint(1,10)

np.random.choice(arr)

np.random.shuffle(arr)
```

---

# Linear Algebra

```python
np.dot(a,b)

a @ b

np.linalg.det(a)

np.linalg.inv(a)

np.linalg.eig(a)

np.linalg.solve(a,b)
```

---

# Useful Functions

```python
np.clip(arr,0,100)

np.round(arr)

np.abs(arr)

np.ceil(arr)

np.floor(arr)
```

---

# Copy vs View

```python
copy = arr.copy()

view = arr.view()
```

---

# Performance Tip

Prefer **vectorized operations** instead of loops.

❌ Slow

```python
result = []

for i in arr:
    result.append(i * 2)
```

✅ Fast

```python
result = arr * 2
```

---

# Best Practices

* Use vectorized operations whenever possible.
* Avoid unnecessary Python loops.
* Use broadcasting instead of manual iteration.
* Choose the appropriate data type to optimize memory usage.
* Set a random seed for reproducible experiments.
* Keep arrays homogeneous for better performance.

---

# Machine Learning Workflow

```
Python
   ↓
NumPy
   ↓
Pandas
   ↓
Matplotlib
   ↓
Scikit-learn
   ↓
Machine Learning
```

---

## Quick Revision Checklist

* ✅ Array Creation
* ✅ Indexing & Slicing
* ✅ Reshaping
* ✅ Broadcasting
* ✅ Universal Functions
* ✅ Statistical Functions
* ✅ Sorting & Searching
* ✅ Boolean Masking
* ✅ Random Module
* ✅ Linear Algebra
* ✅ Vectorization
* ✅ Copy vs View

---

**Author:** V Rohith
**Repository:** Building ML Foundations with NumPy
