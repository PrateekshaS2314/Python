import numpy as np
ls = [1,2,3,4]
arr= np.array(ls)
print(arr)
print(arr.shape)
print(arr.dtype)
print(arr.size)
print(arr.ndim)
print(type(arr))
print(arr.itemsize)
print("Bytes:", arr.size*arr.itemsize)
