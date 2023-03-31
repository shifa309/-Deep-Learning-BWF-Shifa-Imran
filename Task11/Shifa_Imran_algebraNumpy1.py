import numpy as np

# Creating NumPy arrays 
a = np.array([[3, 4, 7], 
               [4, 2, 9], 
                [1, 3, 7]])
b = np.array([[3, 2, 2], 
               [9, 9, 5], 
               [3, 2, 4]])
c = np.array([4, 2, 1])
d = np.array([2, 5, 3])

# Matrix addition
print("\nMatrix addition:")
print(a + b)

# Matrix subtraction
print("\nMatrix subtraction:")
print(a - b)

# Matrix multiplication
print("\nMatrix multiplication: 1st method by matmul")
print(np.matmul(a, b))
print("\nMatrix multiplication: 2nd method by dot")
print(a.dot(b))

# Scalar multiplication
print("\nScalar multiplication:")
print(3 * a)

# Transpose of a matrix
print("\nTranspose of a matrix:")
print(np.transpose(a))

# Determinant of a matrix
print("\nDeterminant of a matrix:")
print(np.linalg.det(a))

# Rank of a matrix
print("\nRank of a matrix:")
print(np.linalg.matrix_rank(a))

# Inverse of a matrix
print("\nInverse of a matrix:")
print(np.linalg.inv(a))



