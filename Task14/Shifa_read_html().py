import pandas as pd

# Load the 1st HTML file 
filename = 'example.html'
dfs = pd.read_html(filename)

df = dfs[0]

# Print the DataFrame
print(df)

print("\nConcatenationg 2 html files")
# load from the 2nd HTML file
filename2 = 'example2.html'
dfs1 = pd.read_html(filename2)

# Concatenate both DataFrames 
df = pd.concat([dfs[0], dfs1[0]])

print(df)
