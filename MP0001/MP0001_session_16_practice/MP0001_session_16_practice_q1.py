#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/19 13:06
@user: jiananwang
@title: MP0001_session_16_practice_q1
"""

from sklearn import linear_model
import numpy as np
import pandas as pd
import csv

def readCSVFile(filename='gdp.csv',
                startRow=0, startCol=None,
                endRow=0, endCol=None, header=None):
    fs = open(filename, "r", newline="")
    csvReader = csv.reader(fs)
    rows = []
    line = 0
    for row in csvReader:
        if ((header is not None) and (line == header)) or ((header is None) and (line == 0)):
            headerCol = row
            ncol  = len(headerCol)
            ncol2 = ncol // 2
        elif (header is not None) and (line < header):
            pass
        else:
            emptyCount = sum(map(lambda ss: len(str(ss))==0, row))
            if emptyCount > ncol2:    break
            if startRow <= line <= endRow:
                if startCol is None:    startCol = 0
                if endCol is None:    endCol = len(headerCol) - 1
                rows.append(row[startCol: (endCol+1)])
            #
        #
        line += 1
    #
    fs.close()
    ## Now with data in rows, we can create df
    df = pd.DataFrame(rows, columns=headerCol)
    # drop first, second and third columns
    df.drop(columns=df.columns[1:4], inplace=True)
    df.set_index(df.columns[0], inplace=True, drop=True)
    # Replace all commas with empty string
    df = df.applymap(lambda x: str(x).replace(',', ''))

    df = df.T
    df.index = df.index.astype(int)

    n_rows, n_cols = df.shape
    for j in range(n_cols):
        df.iloc[:, j] = pd.to_numeric(df.iloc[:, j], errors='coerce')
    return df

# q1
df = readCSVFile(filename='gdp.csv', header=6, startRow=7, endRow=25, startCol=None, endCol=None)
old_cols = df.columns
df.columns = list(chr(i) for i in range(65, 65 + len(df.columns)))
dt = {k: v for k, v in zip(df.columns, old_cols)}
# q2
year_F = list(df['F'][df['F'] < 0].index)
# q3
reg = linear_model.LinearRegression()
x = np.array(df.index.values).reshape((-1, 1))
y = np.array(df.B)
reg.fit(x, y)
print(reg.score(x, y))
grad = reg.coef_
intercept = reg.intercept_
print(reg.predict(np.array(2022).reshape(1, -1)))
# q4
df0 = df.copy()
df.drop(columns='A', inplace=True)
df.drop(columns=df.columns[8:], inplace=True)
dfcor = df.corr()

nrows, ncols = dfcor.shape
for i in range(nrows):
    for j in range(i, ncols):
        dfcor.iat[i, j] = 0
