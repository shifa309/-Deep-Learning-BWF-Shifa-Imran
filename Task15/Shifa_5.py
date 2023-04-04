import pandas as pd

data = pd.DataFrame({'col1': ['one', 'two', 'one', 'two', 'one', 'two', 'two'],
                     'col2': ['x', 'x', 'y', 'y', 'x', 'x', 'y'],
                     'col3': [1, 2, 3, 4, 5, 6, 7],
                     'col4': [10, 20, 30, 40, 50, 60, 70]})

print(data)

print("\nRemove duplicate rows based on columns k1 and k2, keeping only the last occurrence: ")
data_new = data.drop_duplicates(['col1', 'col2'], keep='last')

print(data_new)
