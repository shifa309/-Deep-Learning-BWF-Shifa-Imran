import numpy as np
import pandas as pd

np.random.seed(123)
data = pd.DataFrame({'A': np.random.normal(0, 1, 50),
                     'B': np.random.normal(0, 1, 50),
                     'C': np.random.normal(0, 1, 50)})

# extract a single column from the DataFrame
col = data['C']

threshold = 0.5

# filter out the outliers in the selected column
col_filtered = col[np.abs(col) <= threshold]

# use the .loc accessor to filter out the outliers in the selected column
col_filtered1 = col.loc[np.abs(col) <= threshold]

print("Original column:\n", col)
print("\nFiltered column:\n", col_filtered)

print("\nFiltered column (.loc):\n", col_filtered1)
