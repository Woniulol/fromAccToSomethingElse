#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/4 15:30
@user: jiananwang
@title: MP0001_session_12_practice_q6
"""


from datetime import datetime
import calendar


def print_month_calender(date):
    date = datetime(*[int(i) for i in date.split('-')])
    upper_left = date.strftime("%Y %b ")
    sep = '|'
    empty = ''
    print(f'{upper_left:=<80s}')

    for i in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']:
        print(f'{sep}{i:^10s}', end='')
    #
    print(sep)
    print(f'{empty:=^80s}')

    for week_list in calendar.monthcalendar(date.year, date.month):

        for day in week_list:
            if day == 0:
                day = ''
            print(f'{sep}{str(day):<10s}', end='')
        #
        print(f'{sep}')

        for i in range(2):

            for j in range(7):
                print(f'{sep}{empty:<10s}', end='')
            #
            print(f'{sep}')
        #
        print(f'{empty:-^80s}')
    #


def main():
    print_month_calender('2021-09-07')


if __name__ == '__main__':
    main()
