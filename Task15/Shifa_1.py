import numpy as np
import pandas as pd

df = pd.DataFrame({'Col1': [1, 2, np.nan, 4],
                   'Col2': [5, np.nan, np.nan, 8],
                   'Col3': [9, 10, np.nan, 12]})

print("\nCheck for missing values: ")
print(df.isnull())

print("\nDrop rows with missing values: ")
df_dropped = df.dropna()
print(df_dropped)

print("\nFill missing values with a specific value: ")
df_filled = df.fillna(0)
print(df_filled)

print("\nFill missing values with the mean of the column: ")
df_filled1 = df.fillna(df.mean())
print(df_filled1)

print("\nInterpolate missing values: ")
df_interpolated = df.interpolate()
print(df_interpolated)
