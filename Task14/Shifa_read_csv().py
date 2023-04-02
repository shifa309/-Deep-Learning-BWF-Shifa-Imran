import pandas as pd

# Load the CSV file 
df = pd.read_csv('example.csv')

# Print rows of the DataFrame
print(df)
print("Rows:")
print(pd.options.display.max_rows) 

print("\nReading data differently from csv file: ")
df = pd.read_csv('example.csv', header=0, usecols=["Name"], nrows=2, delimiter=',')

#NOTE: GIVING ERROR WHEN I ADD MORE THAN 1 COLUMN NAME IN USECOLS, EVEN THOUGH I HAVE COLUMN IN MY .CSV FILE
#usecols=["Name", "AGE"] --> gives error on this saying "Usecols do not match columns, columns expected but not found: ['Age']"
print(df)

