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
# import csv file
gov_county = pd.read_csv('../data/governors_county.csv')
# print(df.head(6))
# print(df.columns)
max_percent = gov_county['percent'].max()
print(max_percent)
max_gov_county = gov_county[gov_county['percent'] == max_percent]
print(max_gov_county)
min_percent = gov_county['percent'].min()
print(min_percent)
min_gov_county = gov_county[gov_county['percent'] == min_percent]
print(min_gov_county)

gov_county_mean_percent_indiana = gov_county[gov_county['state'] == 'Indiana']
gov_county_mean_percent_indiana = gov_county_mean_percent_indiana['percent'].mean().round(2)

print(gov_county_mean_percent_indiana)