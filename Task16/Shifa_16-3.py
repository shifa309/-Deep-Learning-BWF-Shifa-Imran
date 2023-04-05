import pandas as pd

df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                    'value': [1, 2, 3, 4]})
df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'],
                    'value': [5, 6, 7, 8]})

print("Merge the dataframes on the 'key' column with suffixes: ")
merged_df = pd.merge(df1, df2, on='key', suffixes=('_left', '_right'))

print(merged_df)
