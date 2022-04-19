import pandas as pd

# ustawienia wyświetlania
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 100)

# wczytywanie danych
read_settings = {'name':str , 'prep_time': int}
indian_food = pd.read_csv('../data/indian_food.csv',
                          dtype=read_settings)
print(indian_food.head(2))
print(indian_food.dtypes)

print(indian_food.shape)
indian_food_excel = pd.read_excel('../data/data.xlsx',
                                  sheet_name=0)
# lub

xlsx = pd.ExcelFile('../data/data.xlsx')
df_xlsx = pd.read_excel(xlsx)
print(df_xlsx)

indian_food = pd.read_csv('../data/indian_food.csv',
                          usecols=['name', 'ingredients', 'diet', 'prep_time',
                                   'cook_time']) # wczytywanie wybranych kolumn z pliku

indian_food[['diet', 'ingredients']].to_excel('../data/indian_food_my_excel_list.xlsx',
                                              sheet_name='wybrane jedzenie',    # nadaje nazwę arkuszowi
                                              index=False)                      # nie zapisuje indeksów w pierwszej kolumnie



