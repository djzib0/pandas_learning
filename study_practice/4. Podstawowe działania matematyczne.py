import pandas as pd

pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 100)

gov_county = pd.read_csv('../data/governors_county.csv')
print('Original data:')
print(gov_county.head())
print('DF INFO')
print(gov_county.info())

# Przypisywanie wartości z innej kolumny do nowej
gov_county['prev_votes'] = gov_county['current_votes'] # 'prev_votes' to nazwa nowej kolumny
print(gov_county['prev_votes'])
# Odejmowanie wybrane wartości
gov_county['prev_votes'] = gov_county['prev_votes'].sub(100)
# Suma dwóch kolumn
gov_county['prev_votes'] = gov_county['prev_votes'] + gov_county['total_votes']
# Mnożenie o wybraną wartość
gov_county['prev_votes'] = gov_county['prev_votes'].mul(100)
# Dzielenie o wybraną wartość
gov_county['prev_votes'] = gov_county['prev_votes'].div(100)
# pokazanie sumy wszystkich wartości w kolumnie
print(sum(gov_county['total_votes']))
# średnia wszystkich wartośc w kolumnie
print(gov_county['total_votes'].mean())
#lub
print(gov_county['total_votes'].median())

# zmiana typu danych na inny typ
gov_county['total_votes'] = gov_county['total_votes'].astype(str)


# print(gov_county['prev_votes'])
