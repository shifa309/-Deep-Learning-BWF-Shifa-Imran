import pandas as pd
import numpy as np

df = pd.DataFrame({'Col1': ['hi', 'hi', 'hi', 'hello', 'are', 'is', 'is'],
                   'Col2': ['hi', 'hi', 'two', 'two', 'one', 'one', 'two'],
                   'Col3': ['hi', 'hi', 3, 4, 5, np.nan, 7],
                   'Col4': ['hi', 'hi', 10, 11, 12, 13, 14]})

print (df)

print("\nChecking for duplicate rows by duplicated(): ")
print(df.duplicated())

print("\nDrop duplicate rows: ")
df_new = df.drop_duplicates()
print(df_new)
