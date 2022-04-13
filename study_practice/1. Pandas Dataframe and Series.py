import pandas as pd

df = pd.DataFrame({'kolumna-imie': ['Piotr','Adam', 'Maria'],
                   'kolumna-nazwisko': ['Sabatura', 'Rdzak', 'Rokita']}, index=['male', 'male', 'female'])

# print(df)

df1 = pd.DataFrame(data=[
    ['Piotr', 'Kowalski'],
    ['Adam', 'Słoń'],
    ['Maria', 'Kowalska'],
    ['test', "1"]
])
# # print(df1)
# # print(df1.info())
# # print(type(df1))
# df1.columns = ['nazwa1', 'nazwa2']
# df1.columns = ['Imie', 'Nazwisko']
#
# my_dict = df1.to_dict()
# print(my_dict)
# df_from_dict = pd.DataFrame.from_dict(my_dict)
# print(df_from_dict)

my_list = ['Piotr', 'Adam', 'Maria', 'Agata']
series_from_my_list = pd.Series(my_list)
print('pd.Series: ')
print(series_from_my_list)

# zapis do listy
print(series_from_my_list.tolist()) # pandas function to_list()
print(type(series_from_my_list))

# konwersja pd.Series do pd.DataFrame
df_from_series = series_from_my_list.to_frame()
print(df_from_series)
df_from_series = pd.DataFrame(series_from_my_list)
print(df_from_series)
