#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/24 19:28
@user: jiananwang
@title: MP0001_session_17_practice_class
"""

import pandas as pd
import numpy as np


def read_data_file(file_name='population-un.csv'):
    df = pd.read_csv(file_name)

    # Delete rows and columns with many NaNs
    nrows, ncols = df.shape
    rows_with_many_NaNs = df.index[df.isna().sum(axis=1) > (ncols / 2)]
    df.drop(index=rows_with_many_NaNs, inplace=True)
    # here you need to re-check the shape of df since it has already dropped some rows
    nrows, ncols = df.shape
    cols_with_many_NaNs = df.columns[df.isna().sum() > (nrows / 2)]
    df.drop(columns=cols_with_many_NaNs, inplace=True)

    # Repalce all commas with empty string
    df = df.applymap(lambda ss: str(ss).replace(",", ""))

    # Convert LocID(0), VarID(2), Time(4) into int
    # Convert all columns from 5 till end of columns
    nrows, ncols = df.shape
    for i in [0, 2, 4] + list(range(5,ncols)):
        df.iloc[:, i] = pd.to_numeric(df.iloc[:, i], errors='coerce')

    return df


def q1(df: pd.DataFrame, out_file_name: str):
    df.to_excel(out_file_name, index=False)


def q2(df: pd.DataFrame):
    unique_locations = df.Location.unique()
    print(f'the unique location number is {len(unique_locations)}')
    print(f'the unique location are {unique_locations}')
    print('-' * 30)

    unique_years = df.Time.unique()
    print(f'the unique year number is {len(unique_years)}')
    print(f'the unique years are {unique_years}')
    print(f'the maximum year is {unique_years.max()}')
    print(f'the minimum year is {unique_years.min()}')
    year_range = unique_years.max() - unique_years.min()
    print(f'the year range is {year_range} years')
    print('-' * 30)


def q3(df: pd.DataFrame):
    # the key problem here is how to contain the result?
    # list? dict? ...
    # for simplicity, we use a dict here
    dt = {}
    for country in ['India', "Republic of Korea", "Viet Nam"]:
        pop = df.loc[df.index[
            (df.Location == country) &
            (df.Time >= 2018) &
            (df.Time <= 2024)], "PopTotal"]
        mn = pop.mean()
        dt[country] = mn
    #
    print(dt)
    return dt


def q4(df: pd.DataFrame):
    selector = (df.Time >= 2019) & (df.Time <= 2025)
    gender_ratio = df.loc[selector, "PopFemale"] / df.loc[selector, "PopMale"]
    df['Ratio'] = gender_ratio
    location = df.Location.loc[gender_ratio.index[gender_ratio >= 1.1]].unique()
    print(f'at least 10% more females than males locations are {location}')
    print(f'number that at least 10% more females than males locations are {len(location)}')


def q5(df: pd.DataFrame, file_name='pop_2022_sorted.html'):
    df2 = df[df.Time == 2022].groupby("Location").mean()
    df2 = df2.loc[:, ['PopTotal', 'PopDensity']].sort_values("PopDensity", ascending=False)
    df2.PopTotal = df2.PopTotal.astype(int)
    df2.to_html(file_name)


if __name__ == '__main__':

    print("\n\nQ1 ----------")
    df = read_data_file()
    print(df)
    # xlsx_file_name = 'population-un.xlsx'
    # q1(df, xlsx_file_name)

    print("\n\nQ2 ----------")
    q2(df)

    print("\n\nQ3 ----------")
    q3(df)

    print("\n\nQ4 ----------")
    q4(df)

    print("\n\nQ5 ----------")
    q5(df)

