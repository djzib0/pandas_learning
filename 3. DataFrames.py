import pandas as pd

data = {
    'calories': [420, 380, 390],
    'duration': [50, 40, 45]
}

myvar = pd.DataFrame(data)
print(myvar)

"""" locate row with loc()"""
df = pd.DataFrame(data)
print(df)
# refer to the row index
print(df.loc[0])

# return row 0 and 1
print(df.loc[[0, 1]])

"""Named indexes"""
df = pd.DataFrame(data, index=['day1', 'day2', 'day3'])
print(df)

"""Locate Named Indexes"""
#refer to the named index
print(df.loc['day2'])

