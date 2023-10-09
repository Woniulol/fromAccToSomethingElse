#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/12 19:46
@user: jiananwang
@title: MP0001_session_14_practice_q1_class
"""

import pandas as pd
import numpy as np
import csv


def read_csv_file(file_name='population-cn_class.csv', sourcesTF=False):
    global df
    fs = open(file_name, 'r', newline="")
    csv_reader = csv.reader(fs, delimiter=',')
    rows = []
    line = 0
    for row in csv_reader:
        if line == 0:
            header_column = row
            ncol = len(header_column)
            ncol_2 = ncol // 2  # get ready for detect NaNs
        else:
            empty_count = sum(map(lambda ss: len(str(ss)) == 0, row))
            if empty_count >= ncol_2:
                break
            else:
                rows.append(row)
        line += 1
    fs.close()
    df = pd.DataFrame(rows, columns=header_column)
    df.set_index(df.columns[0], inplace=True, drop=True)
    # df.set_index('Indicators', inplace=True, drop=True)
    # df = df.applymap(lambda x: float((int(x).replace(",", "")).replace(" ", "")))
    # you can not change the dtype when creating the DataFrame

    if sourcesTF:
        df = df.applymap(lambda fx: 10000 * fx)
    return df


def write_csv_file(df, columns=None, file_name='population3.csv'):
    if df is None or file_name == '':
        return
    fs = open(file_name, 'w', newline='')
    if columns is None:
        columns = [str(df.index.name)] + list(df.columns)
    csv_writer = csv.writer(fs)
    csv_writer.writerow(columns)
    nrow, ncol = df.shape
    for i in range(nrow):
        row = [str(df.index[i])] + list(df.iloc[i, :])
        csv_writer.writerow(row)
    fs.close()
    return


def q3(df):
    global female_pop, f1, f0, poswhere, yearFall
    if df is None: return
    # a.
    pop2016 = df.loc[df.index.str.startswith("Total"), '2016'][0]
    print(f'Total population figure in 2016: {pop2016}')
    print('-' * 30)
    female_pop = df.loc[df.index.str.startswith("Female"), :].iloc[0, :].sort_index()
    f1 = female_pop[1:].values
    f0 = female_pop[:-1].values
    diff = f1 - f0
    poswhere = np.where(diff < 0)[0][0]
    yearFall = female_pop.index[poswhere]


if __name__ == '__main__':
    df = read_csv_file()
    write_csv_file(df)
    q3(df)
