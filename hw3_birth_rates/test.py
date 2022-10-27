import pandas as pd
nations = pd.read_csv('nations.csv')
nations.head(3)

# Using pandas.DataFrame.dropna(), please drop records that have missing value in any of the columns.
# Please create an integer variable called num_countries_dropped that contains the number of countries dropped from this operation.
# Reassign the result to df_pivot_sans_na.

missing_value_df = nations.dropna()
before_countires = nations['country'].unique().tolist()
after_countires = missing_value_df['country'].unique().tolist()

dropped_countries = set(before_countires) - set(after_countires)
num_countries_dropped = len(dropped_countries)
tx = (pd.isnull(missing_value_df['country']))

df_pivot_sans_na = missing_value_df.pivot(index='country')
print(df_pivot_sans_na)
