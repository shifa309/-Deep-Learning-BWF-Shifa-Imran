import pandas as pd
import numpy as np

df = pd.DataFrame({'Col1': [1, 2, np.nan, 4],
                   'Col2': [np.nan, np.nan, np.nan, np.nan],
                   'Col3': [9, 10, np.nan, 12]})

print(df)

print("\nDrop rows: ")
df_dropped = df.dropna(how='all')
print(df_dropped)

print("\nDrop columns: ")
df_dropped1 = df.dropna(how='all', axis=1)
print(df_dropped1)
