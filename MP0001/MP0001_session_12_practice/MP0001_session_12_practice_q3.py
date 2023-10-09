#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/4 12:30
@user: jiananwang
@title: MP0001_session_12_practice_q3
"""
from datetime import datetime
from datetime import timedelta


def days_off(begin_date, end_date):
    if (begin_date is not None) and (end_date is not None):
        return end_date - begin_date  # the result is a timedelta object
    return None

#
# def main():
#     date1 = datetime(2023, 7, 5)
#     date2 = datetime(2025, 5, 19)
#     diff = days_off(date1, date2)
#     print(diff)


if __name__ == '__main__':
    # main()
    date1 = datetime(2023, 7, 5, 15, 17, 19)
    date2 = datetime(2025, 5, 19, 19, 58, 37)
    diff = days_off(date1, date2)
    print(diff)
    print(diff.days)