import numpy as np
random_array = np.random.randint(1, 21, (3, 3))
print("Original array:")
print(random_array)
array_mean = np.mean(random_array)
print("mean:",array_mean)
random_array[random_array < 10] = 0
print("Array after replacing elements less than 10 with 0:")
print(random_array)
