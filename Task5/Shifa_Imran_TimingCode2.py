import timeit  

print('x' * 4)  
print('x' + 'x' + 'x' + 'x')  

print(timeit.timeit("y = 'x' * 4", number=10))  
print(timeit.timeit("xy = 'x' + 'x' + 'x' + 'x'", number = 10))  
