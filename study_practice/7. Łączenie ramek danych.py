import glob
import pandas as pd

pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 100)

df1 = pd.DataFrame({'kolumna_imie': ['Karol', 'Adam', 'Maria', 'Michał'],
                   'kolumna_nazwisko': ['Kowalski', 'Słowik', 'Kowalska', 'Micha'],})

df2 = pd.DataFrame({'imie': ['Piotr', 'Adam', 'Maria', 'Michał'],
                    'nazwisko': ['Kowalski', 'Słowik', 'Kowalska', 'Micha'],
                    'wiek': [22, 12, 23, 54]})

print(df1)
print(df2)

# łączenie za pomocą funkcji merge(), używając części wspólnych

merge_df1_df2 = pd.merge(df1,
                         df2,
                         left_on='kolumna_imie', # kolumna z df1
                         right_on='imie',        # kolumna z df2
                         # on='', #string, lub lista wspólna kolumna nazywająza się tak samo w obu df'ach
                         # left_index=True, <- do zapoznania się, używa indeksu z lewej df
                         how='outer') # domyślnie jest inner (jak inner join)

print(merge_df1_df2)

# *** łączenie ramek danych o różnych rozmiarach przy pomocy concat()
df3 = pd.DataFrame({'kolumna_imie': ['Piotr2', 'Adam', 'Maria', 'Michał'],
                   'kolumna_nazwisko': ['Kowalski', 'Słowik', 'Kowalska', 'Micha']})

df4 = pd.DataFrame({'kolumna_imie': ['Piotr', 'Adam', 'Maria', 'Michał'],
                    'kolumna_nazwisko': ['Kowalski', 'Słowik', 'Kowalska', 'Micha'],
                    'wiek': [22, 12, 23, 54]})

concat_df3_df4 = pd.concat([df3, df4])
print(concat_df3_df4)
# łączenie ramek danych po indexie
concat_df3_df4 = pd.concat([df3, df4], axis='index')
# resetowanie wartości w indexie
concat_df3_df4 = concat_df3_df4.reset_index(drop=True)
print(concat_df3_df4)
