import numpy as np
print("Broadcasting a smaller array to a larger array")
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([15, 20, 32])
print(a + b)

print("\nBroadcasting arrays with different shapes")
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([15, 20])
print(a + b[:, np.newaxis])
