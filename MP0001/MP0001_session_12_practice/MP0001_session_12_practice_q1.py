#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/4 12:30
@user: jiananwang
@title: MP0001_session_12_practice_q1
"""
from datetime import datetime
from datetime import timedelta


def transfer_to_english_spelling(year, month, day):
    date = datetime(year, month, day)
    # the year, month, day should be valid to create the datetime object
    print("date = ", date)
    print(date.strftime('%A'))
    print(date.strptime('Saturday', '%A'))


def main():
    print('enter the year, month, day and i will tell you the week day.')
    year = int(input("please input the year: "))
    month = int(input("please input the month: "))
    day = int(input("please input the day: "))
    transfer_to_english_spelling(year, month, day)


if __name__ == '__main__':
    main()
