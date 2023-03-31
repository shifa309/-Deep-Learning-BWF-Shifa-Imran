import numpy as np

arr1 = np.array([[3, 5, 7], [2, 4, 6]])
arr2 = np.array([[1, 5, 9], [2, 8, 12]])
print("arr1: " , arr1)
print("arr2: " , arr2)

# Performing arithmetic operations 
sum_array = arr1 + arr2
diff_array = arr1 - arr2
prod_array = arr1 * arr2
div_array = arr2 / arr1

# Printing the results to the console
print("\narr1 + arr2 =\n", sum_array)
print("\narr1 - arr2 =\n", diff_array)
print("\narr1 * arr2 =\n", prod_array)
print("\narr2 / arr1 =\n", div_array)

