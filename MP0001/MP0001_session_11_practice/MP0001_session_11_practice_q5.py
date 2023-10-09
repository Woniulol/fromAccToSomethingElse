#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/6/26 22:00
@user: jiananwang
@title: MP0001_session_11_practice_q5
"""
import csv
import re
import string


def read_population():
    fl = open('MP0001_S11_DATA_population_un.csv', "r", newline='')
    csv_reader = csv.reader(fl, delimiter=',')
    population_data = [row for row in csv_reader]
    fl.close()
    return population_data


def unique_items_at_columns(lst: list, column):
    unique_items_at_columns_list = []
    index = lst[0].index(column)
    for item in lst:
        unique_items_at_columns_list.append(item[index])
    return set(unique_items_at_columns_list)


def main():
    columns = ['Location', 'Time']
    data_list = read_population()
    for column in columns:
        print(unique_items_at_columns(data_list, column))


if __name__ == '__main__':
    main()
