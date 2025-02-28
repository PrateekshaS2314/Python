import numpy as np
# Create a row matrix (1D array)
row_matrix = np.array([1, 2, 3, 4])
# Reshape into a column matrix (2D array with shape (4, 1))
column_matrix = row_matrix.reshape(-1, 1)
print("Row Matrix:\n", row_matrix)
print("Column Matrix:\n", column_matrix)
