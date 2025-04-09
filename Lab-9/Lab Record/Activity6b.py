import numpy as np
np.random.seed(42)
matrix_A = np.random.randint(1, 11, (3, 3))
matrix_B = np.random.randint(1, 11, (3, 3))
print("Matrix A")
print(matrix_A)
print("Matrix B")
print(matrix_B)
subtraction = matrix_A - matrix_B
print("subtraction:")
print(subtraction)
division = matrix_A / matrix_B
print("Division:")
print(np.round(division, 2))
