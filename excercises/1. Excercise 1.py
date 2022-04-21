"""
zad 1. Nazwy hrabstw z najwiekszą i najmniejszą ilością ukończonych liczeń głosów [%]
zad 2. Sprawdzenie średniej procentowej dla stanu Indiana
zad 3. Stworzenie ramki danych ze średnią wartość w kolumnie percent,
 ORAZ minimalna wartość aktualnych głosów dla każdego stanu
zad 4. Zmiana nazw stanów na duże litery
zad 5. Zapisanie wyników zadania nr.3 jako plik csv
"""

import pandas as pd

"""Pkt 1"""
# load data from csv file
gov_county = pd.read_csv('../data/governors_county.csv')
# print(gov_county.head(2))
max_votes = gov_county['percent'].max()
min_votes = gov_county['percent'].min()
counties_with_max_votes = gov_county[gov_county['percent'] == max_votes]
# print(counties_with_max_votes[['state', 'percent']])

"""Pkt 2"""
# sprawdzenie średniej procentowej dla stanu Indiana
mean_percent_indiana = gov_county[gov_county['state'] == 'Indiana']['percent'].mean().round(2)

# alternatywna wersja
mean_percent_indiana2 = gov_county[gov_county['state'] == 'Indiana']
mean_percent_indiana2 = mean_percent_indiana2['percent'].mean().round(2)

print(mean_percent_indiana)
print(mean_percent_indiana2)

"""Pkt 3"""


mean_min_states = gov_county.groupby('state').agg(mean_percent=('percent', 'mean'),
                                                  min_votes=('current_votes', 'min'))
mean_min_states['mean_percent'] = mean_min_states['mean_percent'].round(2)
# print(mean_min_states)

"""zad 4. Zmiana nazw stanów na duże litery"""
counties_upper_case_name = gov_county.copy()
counties_upper_case_name['state'] = counties_upper_case_name['state'].str.upper()
print(counties_upper_case_name)

"""Pkt 5"""
mean_min_states = mean_min_states.to_csv('../data/excercise_1.csv')

