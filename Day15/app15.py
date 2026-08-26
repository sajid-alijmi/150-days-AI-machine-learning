


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

s = pd.Series([1,2,3,4,5])
print(s)

# index 
print(s[0])
print(s[2])

# labeled
s = pd.Series([23,24, 25, 26], index=["Sajid", "Aaam", "Ankush", "Bob"])
print(s)
print(s["Sajid"])

