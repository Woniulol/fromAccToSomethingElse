#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/12 13:34
@user: jiananwang
@title: MP0001_session_14_practice_q1
"""
import csv

import pandas as pd


def read_csv_file(file_name):
    fl = open(file_name, 'r', newline='')
    csv_reader = csv.reader(fl, delimiter=',')
    population_data = [row for row in csv_reader]
    fl.close()

    population_data_df = pd.DataFrame([i[1:] for i in population_data[1:]],
                                      columns=population_data[0][1:],
                                      index=[i[0] for i in population_data[1:]],
                                      dtype=float)
    population_data_df.index.name = population_data[0][0]
    return population_data_df.T


def write_csv_file(df: pd.DataFrame, filename, columns=None):
    if columns is not None:
        df = df[columns]

    tf_ser = df.columns.map(lambda x: "(10000 persons)" in x)
    if pd.Series(tf_ser).sum() > 0:
        df[df.columns[tf_ser]] = df[df.columns[tf_ser]].applymap(lambda x: x * 10000)


if __name__ == '__main__':
    df = read_csv_file('population-cn.csv',)
    write_csv_file(df, "a")