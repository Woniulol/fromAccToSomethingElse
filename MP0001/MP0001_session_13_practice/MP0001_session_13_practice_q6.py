#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/10 16:26
@user: jiananwang
@title: MP0001_session_13_practice_q6
"""

import pandas as pd
import numpy as np
import time


def df_search_loop(df, for_value):
    for col in range(len(df.columns)):
        # print(col)
        for row in range(len(df.index)):
            # print(row)
            if df.iloc[row, col] == for_value:
                return row, col
    return -1, -1


def df_search(df, for_value):
    for col in range(len(df.columns)):
        ser = df.iloc[:, col]
        if pd.Series(ser == for_value).any():
            return ser[ser == for_value].index[0], col
    return -1, -1


def df_search_all_loop(df, for_value):
    pos = []
    for col in range(len(df.columns)):
        # print(col)
        for row in range(len(df.index)):
            # print(row)
            if df.iloc[row, col] == for_value:
                pos.append((row, col))
    return tuple(i for i in pos)


def df_search_all(df, for_value):
    pos = []
    for col in range(len(df.columns)):
        ser = df.iloc[:, col]
        for i in ser[ser == for_value].index:
            pos.append((i, col))
    return tuple(i for i in pos)


def df_search_class(df, for_value):
    df_tf = (df == for_value)
    col_sum = df_tf.sum()
    col_found = col_sum[col_sum > 0]
    row_sum = df_tf.sum(axis=1)
    row_found = row_sum[row_sum > 0]
    if (len(col_found) <= 0) or (len(row_found) <= 0):
        return -1, -1
    col = int(col_found.index[0])
    row = int(row_found.index[0])
    return row, col


def df_search_all_class(df, for_value):
    df_tf = df[df == for_value]
    df_found = df_tf.dropna(how='all', axis=1)
    col_found = df_found.columns
    row_found = df_found.index
    if (len(col_found) <= 0) or (len(row_found) <= 0):
        return ()
    tuples = tuple((i, j) for j in col_found for i in row_found)
    return tuples


# df = pd.DataFrame(np.random.randint(0, 10, (1000, 1000)))
df = pd.DataFrame(np.arange(15).reshape((3, 5)))
print(df)


value = 3
#
# time1 = time.time()
# print(df_search_loop(df, value))
# time2 = time.time()
# print("df_search_loop consume: ", time2 - time1)
#
# time1 = time.time()
# print(df_search(df, value))
# time2 = time.time()
# print("df_search consume: ", time2 - time1)
#
# time1 = time.time()
# print(df_search_all_loop(df, value))
# time2 = time.time()
# print("df_search_all_loop consume: ", time2 - time1)
#
# time1 = time.time()
# print(df_search_all(df, value))
# time2 = time.time()
# print("df_search_all consume: ", time2 - time1)

# df.iloc[1, 1] = 1
# df.iloc[0, 2] = 1
df.iloc[2, 0] = 3
# print(df)
# print(df_search_all(df, 1))
# print(df_search(df, 1))
print(df_search_class(df, value))
print(df_search_all_class(df, value))
