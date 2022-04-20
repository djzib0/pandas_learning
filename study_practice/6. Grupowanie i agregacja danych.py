import pandas as pd

gov_county = pd.read_csv('../data/governors_county.csv')
print(gov_county.head(6))

# grupowanie danych - groupby()
# maksymalna wartość w kolumnie current votes dla każdego ze stanów.

max_current_votes_per_state_df = gov_county.groupby(['state'], as_index=False)['current_votes'].max()

# print(max_current_votes_per_state_df)

# grupowanie oraz agregacja - osobne obliczenia dla wybranych
# kolumn w wybranej grupie danych wewnątrz ramki danych

agg_gov_county_max_min_mean = gov_county.groupby('state').agg({'current_votes': 'max',
                                                               'total_votes': 'min',
                                                               'percent': 'mean'})
agg_gov_county_max_min_mean.columns = ['max_current_votes',
                                       'min_total_votes',
                                       'mean_percent']
print(agg_gov_county_max_min_mean)
agg_gov_county_max_min_mean = gov_county.groupby('state').agg(max_current_votes=('current_votes', 'max'),
                                                              min_total_votes=('total_votes', 'min'),
                                                              mean_percent=('percent', 'mean'))
print(agg_gov_county_max_min_mean)
