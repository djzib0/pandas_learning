import pandas as pd

df = pd.DataFrame({'kolumna_imie': ['Piotr', 'Adam', 'Maria','Michal'],
                   'kolumna_nazwisko': ['Kowalski', 'Słon', 'Kowalska', 'Micha']},
                  index=['male', 'male', 'female', 'male'],
                  )

# print(df)

df1 = pd.DataFrame(data=[
    ['Piotr', 'Kowalski'],
    ['Adam', 'Slon'],
    ['Maria', 'Kowalska'],
    ['Michał', 'Micha'],
], columns=['kolumna_name', 'kolumna_surname'])
# print(df1)

# print(df.head(2))
# print(type(df))

# Lista kolumn w Dataframe
# print(df.columns)
# konwersja do słownika
# print(df.to_dict())

my_dict = {'kolumna_imie2': {'male': 'Michal', 'female': 'Maria'},
           'kolumna_nazwisko': {'male': 'Mihal', 'female': 'Kowalska'}}
df_from_dict = pd.DataFrame.from_dict(my_dict)
# print(df_from_dict)

# df['kolumna_imie'] = 'ADAM'
# df_second = df.copy()
# df['kolumna_imie'] = 'MARIA'
# print(df)
# print(df_second)

# tworzenie pd.Series
# series = pd.Series(data=['Piotr', 'Adam', 'Maria', 'Aga'])
# print(series)
# print(type(series))
# print(series.dtypes)
# print(series.dtype)
#
my_list = ['Piotr', 'Adam', 'Maria', 'Agata']
series_from_my_list = pd.Series(my_list)
print(series_from_my_list)

# zapis do listy
print(series_from_my_list.tolist())
print(type(series_from_my_list))

# konwersja pd.Series do pd.DataFrame
df_from_series2 = pd.DataFrame(series_from_my_list)
df_from_series2['nowa_kolumna'] = 'test'
df_from_series2['nowa_kolumna'][0:2] = 'test1'
print(df_from_series2)

