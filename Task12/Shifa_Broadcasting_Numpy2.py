import numpy as np

print("\nDemeaning rows of a 2-dimensional array")
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row_means = np.mean(a, axis =1) 
a_demeaned = a - row_means
print("Original array:\n", a)
print("Row means:\n", row_means.flatten())
print("Demeaned array:\n", a_demeaned)

print("\nDemeaning columns of a 2-dimensional array")
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
column_means = np.mean(a, axis=0) 
a_demeaned = a - column_means
print("Original array:\n", a)
print("Column means:\n", column_means.flatten())
print("Demeaned array:\n", a_demeaned)

print("\nDemeaning an array with a custom mean")
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
custom_mean = np.array([2, 4, 6])
a_demeaned = a - custom_mean[np.newaxis, :] 
print("\nOriginal array:\n", a)
print("Custom mean:\n", custom_mean)
print("Demeaned array:\n", a_demeaned)

