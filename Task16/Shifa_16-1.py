import pandas as pd


df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                    'value1': [1, 2, 3, 4],
                    'value2': [10, 20, 30, 40]})
df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'],
                    'value1': [5, 6, 7, 8],
                    'value2': [50, 60, 70, 80]})
             
print("\nDataframe 1:\n ", df1)
print("\nDataframe 2:\n ", df2)

print("\nMerge the dataframes on the 'key' column: ")
merged_df = pd.merge(df1, df2, on='key', how='outer')
print(merged_df)

print("\nConcatenate the dataframes along the rows: ")
concat_df = pd.concat([df1, df2], axis=0)
print(concat_df)

df3 = pd.DataFrame({'key': ['C', 'D', 'E', 'F'],
                    'value1': [9, 10, None, None],
                    'value2': [90, 100, None, None]})
                    
print("\nDataframe 3:\n ", df3)                   

print("\nCombine df1 and df3, filling in missing values in df1 with values from df3: ")
combined_df = df1.combine_first(df3)
print(combined_df)
