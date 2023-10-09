#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/2 14:42
@user: jiananwang
@title: MP0001_session_11_practice_q4
"""
import csv, os


def change_file_extension(filename: str, ) -> str:
    return filename.split('.')[0] + '.csv'


def read_text(filename):
    fl = open(filename, 'r', newline='')
    csv_reader = csv.reader(fl, delimiter='\t')
    rows = [row for row in csv_reader]
    fl.close()
    print(rows)
    return rows


def convert_to_csv(filename, col_names=None, overwrite=True):
    data_rows = read_text(filename)
    data_row_len = len(data_rows[0])  # 获取一行有多少列

    if col_names is None:
        col_names = [f'C{i}' for i in range(1, data_row_len + 1)]

    if len(col_names) != data_row_len:  # input的col_names长度与列数不一样
        return Exception("Length of col_names mismatches")

    output_file = change_file_extension(filename)

    if os.path.exists(output_file):
        print("already exist")
        if overwrite is False:
            return False
        print("continuing since overwrite")

    fl = open(output_file, 'w', newline='')
    csvwriter = csv.writer(fl)
    csvwriter.writerow(col_names)
    csvwriter.writerows(data_rows)
    fl.close()


def main():
    filename = "todo.txt"
    convert_to_csv(filename)
    print('done')


if __name__ == '__main__':
    main()
