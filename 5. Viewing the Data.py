import pandas as pd

df = pd.read_csv('data/data.csv')

print(df.head(10)) # default value prints 5
print(df.tail(10))
print(df.info())
print(df.shape)

