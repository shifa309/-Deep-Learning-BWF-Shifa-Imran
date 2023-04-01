import pandas as pd

data = {'name': ['Shifa', 'Ali', 'Maryam'],
        'country': ['Pakistan', 'India', 'China'],
        'city': ['Islamabadd', 'Bombay', 'Yang']}
df = pd.DataFrame(data)

print("\nselect column based on label")
# loc allows you to select rows and columns by their index labels.
print(df.loc[:, 'name'])

print("\n Select multiple columns based on label") 
print(df.loc[:, ['name', 'city']])

print("\n select row based on index postion")
# iloc allows you to select rows and columns by their integer position
print(df.iloc[0])

print("\n select multiple row based on index postion")
print(df.iloc[[0, 2]])

