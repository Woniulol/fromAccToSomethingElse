#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/4 12:30
@user: jiananwang
@title: MP0001_session_12_practice_q2
"""
from datetime import datetime


def input_date():
    date_input = input('please input the date (YYYY-MM-DD): ')
    if not ((len(date_input) == 10) and
            (date_input[4] == '-') and (date_input[7] == '-') and
            (date_input[0].isdigit()) and (date_input[1].isdigit()) and
            (date_input[2].isdigit()) and (date_input[3].isdigit())):
        return None
    try:
        # date_datetime = datetime(*[int(i) for i in date_input.split('-')])
        date_datetime = datetime.strptime(date_input, '%Y-%m-%d')
        dt = date_datetime
    except:
        dt = None
    return dt


def main():
    date = input_date()
    if date is None:
        print("you have entered an invalied date")
    else:
        print(date)


if __name__ == '__main__':
    main()
