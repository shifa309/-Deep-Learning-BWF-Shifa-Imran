import pandas as pd

# read the Excel file 
df = pd.read_excel('example.xlsx', engine='openpyxl')

# display the resulting DataFrame
print(df.head())
