#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/17 19:28
@user: jiananwang
@title: MP0001_session_15_practice_q1_class
"""

import pandas as pd
import numpy as np
import os
import csv


def readCSVFile(filename='energyuse_class.csv'):
    fs = open(filename, "r", newline="")
    csvReader = csv.reader(fs)
    rows = []
    line = 0
    for row in csvReader:
        if line == 0:
            headerCol = row
            ncol  = len(headerCol)
            ncol2 = ncol // 2
        else:
            emptyCount = sum(map(lambda ss: len(str(ss))==0, row))
            if emptyCount > ncol2:
                break
            rows.append(row)
        #
        line += 1
    #
    fs.close()
    ## Now with data in rows, we can create df
    df = pd.DataFrame(rows, columns=headerCol)
    df.drop(columns=df.columns[0:2], inplace=True)
    df.set_index(df.columns[0], inplace=True, drop=True)

    n_rows, n_cols = df.shape
    for j in range(n_cols):
        df.iloc[:, j] = pd.to_numeric(df.iloc[:, j], errors='coerce')
    return df


pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 5)

file_name = 'energyuse_class.csv'
df = readCSVFile(file_name)

# q1
print('-'*10 + 'q1' + '-'*10)
n_nan = df.isna().sum().sum()
print(f'Error cells (nan) == {n_nan}')
n_rows_nan = df[df.isna().sum(axis=1) >= 15].index
print(f'rows with at least 15 = {list(n_rows_nan)}')
n_cols_nan = df.columns[df.isna().sum() / len(df.index) > 0.5]
print(f'columns with at half nan = {list(n_cols_nan)}')

# q2
print('-'*10 + 'q2' + '-'*10)
df_before_07 = df.loc[:, df.columns[df.columns < "2007"]]
max_use = df_before_07.max(axis=1).max()
max_country = df_before_07.max(axis=1)[df_before_07.max(axis=1) == max_use].index[0]
print(f'the country using the most energy before 2007 for {max_use} is {max_country}')

df_after_07 = df.loc[:, df.columns[df.columns > "2007"]]
max_use = df_after_07.max(axis=1).max()
max_country = df_after_07.max(axis=1)[df_after_07.max(axis=1) == max_use].index[0]
print(f'the country using the most energy after 2007 for {max_use} is {max_country}')

# q3
print('-'*10 + 'q3' + '-'*10)
df2 = df.drop(df.columns[df.isna().sum() / len(df.index) > 0.5], axis=1)
df2.dropna(inplace=True)

df2_before_07 = df2.loc[:, df2.columns[df2.columns < "2007"]]
max_use = df2_before_07.max(axis=1).max()
max_country = df2_before_07.max(axis=1)[df2_before_07.max(axis=1) == max_use].index[0]
print(f'the country using the most energy before 2007 for {max_use} is {max_country}')

df2_after_07 = df2.loc[:, df2.columns[df2.columns > "2007"]]
max_use = df2_after_07.max(axis=1).max()
max_country = df2_after_07.max(axis=1)[df2_after_07.max(axis=1) == max_use].index[0]
print(f'the country using the most energy after 2007 for {max_use} is {max_country}')

# q4
last_n_year = 5
n_countries = 10
df2['avg5'] = df2.iloc[:, -last_n_year:].mean(axis=1)
print([[f'{k}:{v}'] for k, v in df2['avg5'].sort_values().items()][:n_countries])
print([[f'{k}:{v}'] for k, v in df2['avg5'].sort_values().items()][-n_countries:])
