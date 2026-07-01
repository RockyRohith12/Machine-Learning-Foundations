"""
Day 5 - Advanced NumPy for Machine Learning
Date: 21 June 2026

Topics:
- Random Module
- Random Seed
- Random Numbers
- Uniform Distribution
- Random Integer Generation
- Reshaping Random Arrays
- Maximum and Minimum Values
- Argmax and Argmin
- Boolean Masking
- Conditional Selection using np.where()
- Array Sorting
- Percentile Calculation
"""


import numpy as np 

print(np.random.random())

np.random.seed(1)  # after using seed function np.random gives you constant value
print(np.random.random())


print(np.random.uniform(3,10))  # uniform function is used for getting values in range.. 3 = start and 10 = end 

print(np.random.uniform(1,100,10))  # here 10 = number of items that we need 

print(np.random.uniform(1,100,20).reshape(5,4))  # we can also use reshape in it 

print(np.random.randint(1,10))  # randint gives integer value 

print(np.random.randint(1,100,30).reshape(10,3))  # same as uniform we can use reshape here too.

# MIN and MAX

a = np.random.randint(1,10,6)
print(a)

print(np.max(a))  # give max value of that particular array
print(np.min(a))  # give min value of that particular array

print(np.argmax(a))  # argmax gives index of max value 
print(np.argmin(a))  # argmin gives index of min value 

print(a[np.argmax(a)])  # prints max value i.e., like a verification code 

a = np.random.randint(1,10,5)
print(a)

a[a%2==1] = -1      #this step assignes every odd value of that array to be -1
print(a)   # Boolean masking 


a = np.random.randint(1,50,10) 
print(a)

print(np.where(a%2==1,-1,a))    # syntax = where(condition,True,False)

out = np.where(a%2==1,-1,a)  # storing the condition array into another variable
print(out)


print(np.sort(a))  # helps to sort the array 

print(np.percentile(a,50))    # percentile helps to calculate value like a middle one between that value and lowest value 