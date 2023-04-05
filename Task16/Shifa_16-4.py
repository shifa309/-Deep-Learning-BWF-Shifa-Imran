import pandas as pd

df = pd.DataFrame({'A': ['hi', 'hello', 'hi', 'hello', 'hi', 'hello', 'hi', 'hi'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': [1, 2, 3, 4, 5, 6, 7, 8],
                   'D': [10, 20, 30, 40, 50, 60, 70, 80]})

print("Use stack to pivot the 'wide' dataframe to a 'long' dataframe: ")
stacked_df = df.stack()
print(stacked_df)

print("\nUse unstack to pivot the 'long' dataframe back to a 'wide' dataframe: ")
unstacked_df = stacked_df.unstack()
print(unstacked_df)


print("\nUse stack to pivot the 'wide' dataframe back to a 'long' dataframe: ")
unstacked_df = stacked_df.unstack().stack()
print(unstacked_df)


