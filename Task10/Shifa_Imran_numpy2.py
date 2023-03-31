import numpy as np

# Generate some random data
data = np.random.randn(2, 3)
print("RANDOM DATA")
print (data)

# Creating a 2-D array
print("\nPrinting original array: ")
array = np.array([[4, 7, 9], [1, 3, 8]])
print(array)

# Performing arithmetic operations on a NumPy array
print("\n!!!!!!! Arithmetic operations on 2D array are as follows !!!!!! ")
print("--> Addition: ", array + 5)     # adding 
print("--> Subtraction: ", array - 3)     # subtracting
print("--> Multiplication: ", array * 3)     # multiplying 
print("--> Division: " , array / 4)     # dividing 
print("--> Sqauring:" , array ** 2)    # squaring 

