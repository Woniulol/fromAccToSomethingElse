#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/2 10:25
@user: jiananwang
@title: MP0001_session_11_practice_q2
"""


def input_todo() -> tuple:
    input_date = input('please input the date (YYYY-MM-DD): ')
    input_description = input('please input the description: ')
    input_date = input_date.strip()
    input_description = input_description.strip()
    # import re
    # input_description = re.sub('\t', '', input_description)
    input_description = input_description.replace('\t', ' ')
    return input_date, input_description


def main():
    date, todo = input_todo()
    print(f'User wants to do \"{todo}\" on \"{date}\".')


if __name__ == '__main__':
    main()
