"""
Day 4 - Numpy operations and Broadcasting
Date: 20 June 2026

Topics:
- Ravel
- Transpose
- Stacking
- Splitting
- Fancy Indexing
- Indexing using boolean arrays 
- Broadcasting
- Rules of Broadcasting 
"""



import numpy as np 
arr4 = np.array([[6,7],[8,9],[10,11]])
print(arr4)
print(arr4.ndim)

# Ravel
print(arr4.ravel())  #change shape of numpy array 

#Transpose
print(arr4.transpose())  # row becomes column and column becomes row 

#Stacking = combining two arrays 
arr3 = np.array([[0,1,2],[3,4,5]])
arr5 = np.arange(12,18).reshape(2,3)

print(np.hstack((arr3,arr5)))  # hstack = horizontal stacking 
print(np.vstack((arr3,arr5)))  # vstack = vertical stack 

# Splitting = divides the array into parts 
print(np.hsplit(arr3,3))
print(np.vsplit(arr3,2))

#Fancy Indexing
arr8 = np.arange(24).reshape(6,4)
print(arr8)

print(arr8[[0,2,4]])

#Indexing using boolean arrays 

arr = np.random.randint(low=1,high=100,size=20).reshape(4,5)
print(arr)
print(arr[0][2])

print(arr>50)  # gives true or false output

print(arr[arr>50]) # indexing using boolean arrays 

print(arr[(arr>50) & (arr%2!=0)]) #numbers greater than 50 and odd
arr[(arr>50) & (arr%2!=0)]=0  # here we have assigned numbers greater than 50 and odd are assigned as 0
print(arr)


#plotting using numpy

x = np.linspace(-40,40,100)
print(x)

y = np.sin(x)
print(y.size)
print(y)

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()

y = x*x+2*x+6
plt.plot(x,y)
plt.show()

# Broadcasting = helps to add different shapes and create a new one i.e., performing arithmetic operation on dissimilar arrays  

a1 = np.arange(8).reshape(2,4)  #Scenario 1
a2 = np.arange(8,16).reshape(2,4)

print(a1)
print(a2)
print(a1+a2)


a3 = np.arange(9).reshape(3,3)
a4 = np.arange(3).reshape(1,3)

print(a3,a4)
print(a3+a4)    # here a4 element is added with every row of a3


# Rules of Broadcasting 

# 1. If x = m and y = n, operation will take place 

a1 = np.arange(8).reshape(2,4)
a2 = np.arange(8,16).reshape(2,4)

print(a1+a2)

# 2. If x = 1 and y = n, then also operation will take place 

a5 = np.arange(3).reshape(1,3)
a6 = np.arange(12).reshape(4,3)

print(a5+a6) # This is possible because 3 is same in both arrays 

a7 = np.arange(4).reshape(4,1)
a8 = np.arange(12).reshape(4,3)

print(a7+a8)  # This is possible as 4 is common but arrays are not of same dimensions

a9 = np.arange(3).reshape(1,3)
a10 = np.arange(16).reshape(4,4)

# print(a9+a10) = does not take place as arrays are completely dissimilar i.e., x = 1 but y!=n

# 3. If opposite dimensions are present, then operation takes place 

a11 = np.arange(3).reshape(1,3)
a12 = np.arange(3).reshape(3,1)

print(a11+a12)

# 4. If 1 is present in both x and y 

a13 = np.arange(1).reshape(1,1)
a14 = np.arange(12).reshape(4,3)

print(a13+a14) # Broadcasting takes place where a13 goes into a14

