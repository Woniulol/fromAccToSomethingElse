#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/4 12:31
@user: jiananwang
@title: MP0001_session_12_practice_q4
"""
from datetime import datetime

def daily_rest_compounded_interest(principal, r_annual, n):
    num_days_per_year = 365  # this is defined by bank / industry
    ending_amount = principal * ((1 + (r_annual / num_days_per_year / 100)) ** (num_days_per_year * n))
    return ending_amount, ending_amount - principal


def main():
    principal = float(input('please input the principle: '))
    r_annual = float(input('please input the annual interest rate'))
    n = int(input('please input the number of years: '))
    print(daily_rest_compounded_interest(principal, r_annual, n))


if __name__ == '__main__':
    main()
