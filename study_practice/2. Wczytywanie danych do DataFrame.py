import pandas as pd
# ustawienia wyświetlania
pd.set_option('display.max_columns', 50)
# szerokość DF
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 100)

read_settings = {"name":str, "prep_time":int}
indian_food = pd.read_csv('../data/indian_food.csv',
                          dtype=read_settings,
                          header=0, # which "row" is a header
                          # index_col=0
                          )

print(indian_food.shape)
print(indian_food.columns)
print(indian_food['prep_time'] + indian_food['cook_time'])

# zapisywanie do excela
# try:
#     indian_food.to_excel('../data/test.xlsx')
# except:
#     print("Ten plik jest używany")

indian_food_excel = pd.read_excel('../data/test.xlsx',
                                  sheet_name=1,
                                  header=0)
print(indian_food_excel)




