import pandas as pd

# display settings
pd.options.display.max_rows = 20 # sets how many rows can be displayed


df = pd.read_csv('data/data.csv')
# df.to_excel('data/data.xlsx')

# print(df.to_string()) # print the entire DataFrame
print(df)
print(pd.options.display.max_rows)


