import numpy as np
ls2=[[[1,2,3,4],[5,6,7,8]], [[9,8,7,6],[6,5,4,3]]]
arr2=np.array(ls2)
print(arr2)
print(arr2.shape)
print(arr2.size)
print(arr2.dtype)
print(arr2.itemsize)
print(type(arr2))
print("bytes:", arr2.size*arr2.itemsize)
print(arr2.ndim)
