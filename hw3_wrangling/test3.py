### TEST FUNCTION: test_wrangle_wide2long
# DO NOT REMOVE THE LINE ABOVE

import pandas as pd
from pandas import DataFrame
from numpy import NaN

replace_value = lambda value: NaN if int(value) == -9999 else int(value)


def handle_df(old_df):
    new_df = DataFrame(columns=['id', 'year', 'month', 'tmax', 'dmflag', 'qcflag', 'dsflag'])

    for content in old_df.iterrows():
        row = content[1]
        for month in range(1, 13):
            col = (month - 1) * 4 + 2
            value, dmflag, qcflag, dsflag = row.iloc[col:col + 4]
            value = replace_value(value)
            formatted_value = value if pd.isna(value) else value / 100
            data = {
                'id': row['id'],
                'year': row['year'],
                'month': month,
                'tmax': formatted_value,
                'dmflag': dmflag,
                'qcflag': qcflag,
                'dsflag': dsflag
            }
            new_df = new_df.append(data, ignore_index=True)
    return new_df


def test_wrangle_wide2long():
    origin_df = pd.read_csv('hw3_tmax.csv', header=0)

    new_df = handle_df(origin_df)

    ldf = new_df.sort_values(by=['year', 'month'])
    print(ldf)
