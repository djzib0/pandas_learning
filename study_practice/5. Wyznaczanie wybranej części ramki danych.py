import pandas as pd

pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 100)

gov_county = pd.read_csv('../data/governors_county.csv')

# Wyznaczanie części ramki danych
# print(gov_county['state'] == 'Delaware')

# wyznaczenie tylko tych wierszy, dla których w kolumnie state występuje wybrana nazwa
only_delaware_df = gov_county[gov_county['state'] == 'Delaware']
print(only_delaware_df)

# wyznaczenie tylko tych wierszy, które spełniają wszystkie warunki
without_west_virginia_df = gov_county[(gov_county['current_votes'] > 1000)
                        & (gov_county['total_votes'] >15000)
                        & (gov_county['state'] != 'West Virginia')]
print(without_west_virginia_df)

# wyznaczanie wierszy, spełniających chociaż jeden warunek
at_lest_one_condition_df = gov_county[(gov_county['state'] == 'Delaware')
                                        | (gov_county['state'] == 'my_state')]
print(at_lest_one_condition_df)

# wyznaczanie części ramki danych na podstawie elementów z listy
my_states = ['Delaware', 'Indiana']
is_in_list_df = gov_county[gov_county['state'].isin(my_states)]
print(is_in_list_df)
# przykład z negacją
is_not_in_list_df = gov_county[~gov_county['state'].isin(my_states)]
print(is_not_in_list_df)

# wyznaczanie dla wartości które zawierają część wybranej frazy
gov_county_regex_df = gov_county[gov_county['state'].str.contains('delaware',
                                                                  regex=False,
                                                                  case=False)]
print(gov_county_regex_df)

# Wyznaczanie danych dla warunku gdzie dane zawierają szukaną frazę na początku
startswith_df = gov_county[gov_county['state'].str.startswith('De')]
print(startswith_df)

# Wyznaczanie danych dla warunku gdzie dane zawierają szukaną frazę na końcu
endswith_df = gov_county[gov_county['state'].str.endswith('aware')]
print(endswith_df)

# wyznaczanie rzędów określonych indeksem numerycznym
# iloc[index_number, column_number]

print("-----------------------------------")
# # wyznaczanie pierwszego rzędu jako pd.Series( gdy jest jedne rząd), lub [[]] dla DataFrame
# print(gov_county.iloc[0])
# print(gov_county.iloc[[0]])
#
# # wyznaczanie zakresu ramki danych w osi Y (wg indeksu)
# print(gov_county.iloc[0:5])
# # wyznaczanie trzech ostatnich rzędów
# print(gov_county.iloc[-3:0])
# # wyznaczanie rzędów zaczynających się od 3 dla kolumny 4
# print(gov_county.iloc[3:, 4])
# # wyznaczanie konrketnej wartości w określonym wierszu dla określonej kolumny
# col_idx = 4
# print(gov_county.iloc[4, col_idx])

# ************ loc[index_name, column_name] *********
df_male_female_index = pd.DataFrame({'kolumna_imie': ['Piotr', 'Adam', 'Maria', 'Michal'],
                                     'kolumna_nazwisko': ['Kowalski', 'Słon', 'Kowalska', 'Micha']},
                                    index=['male', 'male', 'female', 'male'])

print(df_male_female_index.loc['male'])

df_names_index = pd.DataFrame({'kolumna_imie': ['Piotr', 'Adam', 'Maria', 'Michal'],
                                     'kolumna_nazwisko': ['Kowalski', 'Słon', 'Kowalska', 'Micha']},
                                    index=['pawel', 'adam', 'maria', 'ada'])

# zakres indeksu od wyznaczonych wartości (nazw indeksu)
print(df_names_index.loc['pawel': 'maria'])
print('*****************************')
# zakres indeksu od wyznaczonych wartości (nazw indeksu)  dla danej kolumny
print(df_names_index.loc['pawel': 'maria', 'kolumna_nazwisko'])
print(df_names_index.loc['pawel': 'maria'][['kolumna_nazwisko']])
