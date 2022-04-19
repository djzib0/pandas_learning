import pandas as pd

pd.set_option('display.max_columns', 50)
# szerokość DF (wyświetlanie)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 100)

gov_county = pd.read_csv('../data/governors_county.csv')
print('Original data:')
print(gov_county.head())
print('DF info')
# print(gov_county.info())
print('______________________')

# gov_county['current_total_votes_sum'] = gov_county['']

# przypisywanie wartości z innej kolumny do nowej
gov_county['prev_votes'] = gov_county['current_votes']
# print(gov_county['prev_votes'])

# odejmowanie wybranej wartości
gov_county['prev_votes'] = gov_county['prev_votes'].sub(100)
print(gov_county['prev_votes'])

# suma dwóch kolumn
gov_county['prev_votes'] = gov_county['prev_votes'] + gov_county['total_votes']
print(gov_county['prev_votes'])

# mnożenie przez wybraną wartość
gov_county['prev_votes'] = gov_county['prev_votes'].mul(100)
print(gov_county['prev_votes'])

# dzielenie
gov_county['prev_votes'] = gov_county['prev_votes'].div(25)
print(gov_county['prev_votes'])

# wartość minimalna w danej kolumnie
# gov_county['prev_votes'] = gov_county['prev_votes'].min()
print(gov_county['prev_votes'])
print(gov_county['prev_votes'].min())

# pokazanie sumy wszystkich wartości w kolumnie
print(sum(gov_county['total_votes']))

# średnia wszystkich wartości w kolumnie
print(gov_county['total_votes'].mean())
print(gov_county['total_votes'].median())

# zmiana typu danych na inny typ jako astype()
gov_county['total_votes'] = gov_county['total_votes'].astype(str)
gov_county['total_votes'] = gov_county['total_votes'] * 3
print(gov_county['total_votes'])
