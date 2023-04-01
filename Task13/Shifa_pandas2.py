import pandas as pd

data = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
s = pd.Series(data)

print("Accessing elements of a Series using index")
print("a: ", s['a'])


print(s[['a', 'c']]) 

print("\nSome arithmetic operations")
op1 = pd.Series([1, 2, 3])
op2= pd.Series([4, 5, 6])
op = op1 + op2
print(op)  

print("\nFiltering")
s = pd.Series([1, 2, 3, 4, 5, 6 , 7])
mask = s > 3
print(s[mask]) 
