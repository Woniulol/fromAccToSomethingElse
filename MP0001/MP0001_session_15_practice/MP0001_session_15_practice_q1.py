#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/17 12:53
@user: jiananwang
@title: MP0001_session_15_practice_q1
"""
from MP0001_session_14_practice.MP0001_session_14_practice_q1_class import read_csv_file
from MP0001_session_14_practice.MP0001_session_14_practice_q1_class import write_csv_file
import pandas as pd
import numpy as np


df = pd.read_csv('energyuse.csv', nrows=217)
df.drop(df.columns[[0, 1, 3, -1]], axis=1, inplace=True)

df.set_index(df.columns[0], inplace=True)

df.columns = [i[:4] for i in df.columns]

df = df.applymap(lambda x: np.nan if x == '..' else x)

df = df.astype(float)


# q1
n_nan = df.isna().sum().sum()

n_rows = df[df.isna().sum(axis=1) >= 0].index

n_cols = df.columns[df.isna().sum() / len(df.index) > 0.5]

# q2
df_before_07 = df.loc[:, :'2007']
print(df_before_07.idxmax())
df_after_07 = df.loc[:, '2008':]
print(df_after_07.idxmax())

# q3
df2 = df.drop(df.columns[df.isna().sum() / len(df.index) > 0.5], axis=1)
df2.dropna(inplace=True)
df2_before_07 = df2.loc[:, :'2007']
df2_after_07 = df2.loc[:, '2008':]
print(df2_before_07.idxmax())
print(df2_after_07.idxmax())

# q4
last_n_year = 5
n_countries = 10
df2['avg5'] = df2.iloc[:, -last_n_year:].sum(axis=1) / last_n_year
print([[f'{k}:{v}'] for k, v in df2['avg5'].sort_values().items()][:n_countries])
print([[f'{k}:{v}'] for k, v in df2['avg5'].sort_values().items()][-n_countries:])

# q5
df2 = pd.concat([df2, pd.DataFrame(df2.sum() / len(df2.index), columns=['GlobalAvg']).T])
print(df2.T.GlobalAvg[df2.T.GlobalAvg == df2.T.GlobalAvg.max()].index[0])
print(df2.T.GlobalAvg[df2.T.GlobalAvg == df2.T.GlobalAvg.min()].index[0])

# q6
df3 = df2.applymap(lambda x: round(x * 11.63, 2))





