import pandas as pd

result = pd.Series([1, 2, 3, 4, 5], index=pd.Index(['a', 'b', 'c', 'd', 'e'], name='letters'))
df = pd.DataFrame({'left': result, 'right': result + 5}, columns=pd.Index(['left', 'right'], name='side'))

print(df)

print("\n\n")
unstacked_df = df.unstack(level='letters')

print(unstacked_df)

