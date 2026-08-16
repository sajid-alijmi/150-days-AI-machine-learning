import numpy as np
import time

size = 1_000_000

#python list 
py_list = list(range(size))
start = time.time()
sq_list = [x**2 for x in py_list]
end = time.time()
print(f"python list time = {end-start} seconds")

np_arr = np.array(py_list)
start = time.time()
sq_array = np_arr ** 2
end = time.time()
print(f"numpy array time = {end-start} seconds")

import sys

print(f"python list size = {sys.getsizeof(py_list) * len(py_list)} bytes")

print(f"numpy array size = {np_arr.nbytes} bytes")

# create - from lists 
arr = np.array([1,2,3,4,5 ])

print(arr, type(arr), arr.shape)
arr2 = np.array([1,2,3,4,5, "sajid"])
print(arr2, type(arr), arr2.dtype)

arr1 = np.zeros((2, 3)) #prefill
print(arr1, arr1.shape)

arr2 = np.ones((2, 3))
print(arr2, arr2.shape)

arr3 = np.full((3,4),1000) #prefil wirh value
print(arr3, arr3.shape)

arr4 = np.eye(3) # identity matrix
print(arr4, arr4.shape)

arr5 = np.arange(0, 11, 2) #range element
print(arr5, arr5.shape)

arr6 = np.linspace(1, 100, 4) # evenly space arrays
print(arr6, arr6.shape)
array2d = np.array([[1,2,3],[4,5,6,], [7,8,9]])
print(array2d, array2d.shape)