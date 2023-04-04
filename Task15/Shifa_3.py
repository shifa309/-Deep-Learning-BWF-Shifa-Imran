import pandas as pd
import numpy as np


df = pd.DataFrame({'Col1': [1, 2, np.nan, 4],
                   'Col2': [5, np.nan, np.nan, 8],
                   'Col3': [9, 10, np.nan, 12]})


print("\nFill missing values with last observed value, limit to 2 consecutive missing values: ")
df_filled = df.fillna(method='ffill', limit=2)
print(df_filled)

print("\nFill missing values with the mean of the column, modifying the calling object: ")
df.fillna(df.mean(), inplace=True)
print(df)
