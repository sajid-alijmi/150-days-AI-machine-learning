
# import time

# size = 1_000_000

# #python list 
# py_list = list(range(size))
# start = time.time()
# sq_list = [x**2 for x in py_list]
# end = time.time()
# print(f"python list time = {end-start} seconds")

# np_arr = np.array(py_list)
# start = time.time()
# sq_array = np_arr ** 2
# end = time.time()
# print(f"numpy array time = {end-start} seconds")

# import sys

# print(f"python list size = {sys.getsizeof(py_list) * len(py_list)} bytes")

# print(f"numpy array size = {np_arr.nbytes} bytes")

# # create - from lists 
# arr = np.array([1,2,3,4,5 ])

# print(arr, type(arr), arr.shape)
# arr2 = np.array([1,2,3,4,5, "sajid"])
# print(arr2, type(arr), arr2.dtype)

# arr1 = np.zeros((2, 3)) #prefill
# print(arr1, arr1.shape)

# arr2 = np.ones((2, 3))
# print(arr2, arr2.shape)

# arr3 = np.full((3,4),1000) #prefil wirh value
# print(arr3, arr3.shape)

# arr4 = np.eye(3) # identity matrix
# print(arr4, arr4.shape)

# arr5 = np.arange(0, 11, 2) #range element
# print(arr5, arr5.shape)

# arr6 = np.linspace(1, 100, 4) # evenly space arrays
# print(arr6, arr6.shape)
# array2d = np.array([[1,2,3],[4,5,6,], [7,8,9]])
# print(array2d, array2d.shape)
# # today practice
# arr = np.array([1,2,3,4,5])

# print(arr.shape)
# print(arr.size)
# print(arr.dtype)
# print(arr.ndim)

# float_arr = arr.astype(np.float64)
# print(float_arr, float_arr.dtype)
# # Operation on arrays
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr, arr.shape)

# reshaped = arr.reshape((3, 2))
# print(reshaped, reshaped.shape)
# flattened = arr.flatten() # 2d 
# print(flattened, flattened.shape)

# arr = np.array([1,2,3,4,5,])

# print(arr[0])
# print(arr[3]) 

# idx = [0, 1, 3]
# print(arr[idx])

# print(arr[arr > 2])
# print(arr[arr % 2 == 0])
# print(arr[arr % 2 != 0])

# #slicing
# print(arr[1:4])

# # Copy vs View 
# nums = [1, 2, 3, 4, 5]
# sub_list = nums[1:3]
# print(sub_list)
# sub_list[0] = 200

# print(sub_list)
# print(nums)

# arr = np.array([1, 2, 3, 4, 5])
# sub_arr = arr[1:3]
# print(sub_arr)

# sub_arr[0] = 200

# print(sub_arr)
# print(arr)

# # Talking about data type 
# arr = np.array([1, 2, 3, 4, 5,])

# print(arr, arr.dtype)

# arr1 = np.array([3 + 5j])
# arr2 = np.array([2 + 8j])

# print(arr1+arr2)


# arr = np.array(["prime", {1 , 2, 3}, 3.14])

# print(arr, arr.dtype)

# arr2D = np.array([[1, 2, 3], [4, 5, 6], [7,8, 9]])
# print(arr2D)
# print(np.sum(arr2D))

# sum_of_columns = np.sum(arr2D, axis = 0)
# print(sum_of_columns)


# # 3d array
# arr3D = np.array([[[1,2 ], [3,4], [5,6]], [[11,21 ], [7,11], [8,9]]])

# print(arr3D, arr3D.shape)

# print(arr3D[0, 1, 1]) 


#day 15 works
# vectorization
import numpy as np
import pandas as pd

arr = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

print(arr ** 2)
print(arr + 10)
print(arr + arr2)

# broadcasting 
arr = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1,2,3,4,5,], [1,2,3,4,5]])
print(arr.shape)
print(arr2.shape)
print(arr + arr2)

# normalise
arr = np.array([[1,2],[3,4]])

print(np.sum(arr))
print(np.prod(arr))
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr))
print(np.argmax(arr))
print(np.std(arr))
print(np.median(arr))
print(np.var(arr))

arr = np.array([[1,2],[3,4]])
print(np.square(arr))
print(np.sqrt(arr))
print(np.log(arr))
print(np.log10(arr))
print(np.exp(arr))



# data frame
info = {
    "Name" : ["Sajid", "Rahul", "Rohit","Jiya"],
    "CGPA" : [9.5, 7.5, 8.5, 9.0]
}

df = pd.DataFrame(info)
print(df)

