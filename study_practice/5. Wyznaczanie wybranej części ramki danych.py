import pandas as pd

pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 100)

read_settings = {'current_votes': int, 'total_votes': int, }
gov_county = pd.read_csv('../data/governors_county.csv',
                         dtype=read_settings)
print(gov_county.columns)
print(len(gov_county))

# wyznaczanie części ramki danych
print(gov_county['state'] == 'Delaware')
# wyznaczono tylko te linie, które posiadają state Delaware
only_delaware_df = gov_county[gov_county['state'] == 'Delaware']
print(only_delaware_df)

west_virginia_votes = gov_county[(gov_county['current_votes'] > 10000)
                                 & (gov_county['total_votes'] > 15000)
                                 & (gov_county['state'] == 'West Virginia')]
print(west_virginia_votes)

# wyznaczenie dwóch stanów, nawet jeżeli jeden nie istnieje
two_states = gov_county[(gov_county['state'] == 'Delaware')
                        | (gov_county['state'] == 'my_state')]
print(two_states)

# wyznaczanie części ramki na podstawie elementów z listy
# my_state = ['Delaware', 'Indiana']
# gov_county = gov_county[gov_county['state'].isin(my_state)]
# print(gov_county)
# # przykłąd z negacją
# gov_county = gov_county[~gov_county['state'].isin(my_state)]
# print(gov_county)

# # wyznaczanie dla wartości które zawierają część wybranej frazy
# gov_county = gov_county[gov_county['state'].str.contains('delaware',
#                                                          regex=False,
#                                                          case=False)]
#

# # wyznaczanie danych dla warunku gdzie dane rozpoczynają się od danej frazy
# gov_county = gov_county[gov_county['state'].str.startswith('De')]
# print('wybrana fraza')
# print(gov_county)

# wyznaczanie rzędów określonych indexem numerycznym
# iloc[index_number, column_number]

# wyznaczanie pierwszego rzędu jako pd.Series (gdy jest jeden rząd, lub [[]] jako DataFrame
# print(gov_county.iloc[0])
#
# # wyznaczanie zakrsu ramki danych w osi Y (wg indexu)
# print(gov_county.iloc[0:5])
#
# # wyznaczanie ostatnich 3 rzędów
# print(gov_county.iloc[-3:])
#
# # wyznaczanie rzędów zaczynających się od 3 dla kolumy 4
# print(gov_county.iloc[3:, 4])
#
# # wyznaczanie konkretnej wartości w określonej linii dla określonej kolumny
# col_idx = 2
# print(gov_county.iloc[3, col_idx])

# ***** loc[index_name, column_name]

df_male_female_index = pd.DataFrame({'kolumna_imie': ['Piotr', 'Adam', 'Maria', 'Michal'],
                                     'kolumna_nazwisko': ['Kowalski', 'Słon', 'Kowalska', 'Micha']},
                                    index=['male', 'male', 'female', 'male'])
print(df_male_female_index)
print(df_male_female_index.loc['male'])

df_names_index = pd.DataFrame({'kolumna_imie': ['Piotr', 'Adam', 'Maria', 'Michal'],
                                     'kolumna_nazwisko': ['Kowalski', 'Słon', 'Kowalska', 'Micha']},
                                    index=['pawel', 'adam', 'maria', 'ada'])

print(df_names_index)

# zakres indexu od wyznaczonych wartości (nazw indexu)
print(df_names_index.loc['pawel': 'maria'])

# zakres indexu od wyznaczonych wartości (nazw indexu) dla wybranej kolumny
print(df_names_index.loc['pawel': 'maria', ['kolumna_imie', 'kolumna_imie']])
print(df_names_index.loc['pawel': 'ada'][['kolumna_nazwisko', 'kolumna_imie']])
