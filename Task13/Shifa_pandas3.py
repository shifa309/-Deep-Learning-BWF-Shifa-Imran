import pandas as pd

#Series with named index and values
s = pd.Series([22, 34, 14, 10], index=['A', 'B', 'C', 'D'], name='Age')

# assign names to Series and its index
s.name = 'Person's Age'
s.index.name = 'Name initial Abbreviation'

print(s)

