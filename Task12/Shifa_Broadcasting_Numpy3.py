import numpy as np

print("Broadcasting over a 1D array")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

#np.newaxis creates a new axis of length 1 at the second position -- shape(3,1)
c = a[:, np.newaxis] + b

print("Array a: ", a)
print("Array b: ", b)
print("a[:, np.newaxis]:\n", a[:, np.newaxis])
print("a[:, np.newaxis] + b:\n", c)
