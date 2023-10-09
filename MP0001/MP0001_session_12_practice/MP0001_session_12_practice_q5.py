#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/4 12:31
@user: jiananwang
@title: MP0001_session_12_practice_q5
"""
from datetime import datetime, timedelta
import dateutil.relativedelta


def daily_rest_compounded_interest(principal, r_annual, n):
    ending_amount = principal * ((1 + (r_annual / 365 / 100)) ** n)
    return ending_amount, ending_amount - principal


def out_put_info(principal, r_annual, start_date, end_date):
    line1 = 'Principal Amount:'
    line2 = 'Interest:'
    line3 = 'Start Date:'
    line4 = 'End Date:'
    line6_1 = "Date"
    line6_2 = "Amount"
    line6_3 = "Net Interest"

    start_date_datetime = datetime(*[int(i) for i in start_date.split('-')])
    end_date_datetime = datetime(*[int(i) for i in end_date.split('-')])
    out_principal = f'$   {principal:,.2f}'
    out_r_annual = f'{r_annual:.4f}'
    out_start_date_datetime = start_date_datetime.strftime('%Y-%m-%d')
    out_end_date_datetime = end_date_datetime.strftime('%Y-%m-%d')

    print(f'{line1:<20s}{out_principal:>20s}')
    print(f'{line2:<20s}{out_r_annual:>20s}%')
    print(f'{line3:<20s}{out_start_date_datetime:>20s}')
    print(f'{line4:<20s}{out_end_date_datetime:>20s}')
    print('=' * 60)
    print(f'{line6_1:<10}{line6_2:^30}{line6_3:>20}')
    print('-' * 60)

    next_date = start_date_datetime
    rolling_principle = principal
    day_passed = 0

    while end_date_datetime - next_date >= timedelta(days=0):

        day_passed_from_last_month = (next_date - start_date_datetime).days - day_passed
        day_passed += day_passed_from_last_month

        amount, net_interest = daily_rest_compounded_interest(rolling_principle, r_annual, day_passed_from_last_month)

        rolling_principle = amount
        rolling_interest = rolling_principle-principal

        out_amount = f'$  {amount:10,.2f}'
        out_rolling_interest = f'$  {rolling_interest:8,.2f}'
        out_next_date = next_date.strftime('%Y-%m-%d')
        print(f'{out_next_date:<10s}{out_amount:^30s}{out_rolling_interest:>20s}')

        next_date = next_date + dateutil.relativedelta.relativedelta(months=1)
    #
    print('=' * 60)


def main():
    principal = float(input('please input the principle: '))
    r_annual = float(input('please input the annual interest rate: '))
    start_date = '2018-03-04'
    end_date = '2019-03-04'
    out_put_info(principal, r_annual, start_date, end_date)


if __name__ == '__main__':
    main()
