#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/6/24 22:39
@user: jiananwang
@title: MP0001_session_9_practice_q4
"""


def convert_three_digits_int(three_digits_int):
    hundred_int = three_digits_int // 100
    if hundred_int > 0:
        words.append(char[hundred_int])
        words.append('hundred')

    two_decimal_int = three_digits_int - (hundred_int * 100)
    if two_decimal_int == 0:
        return

    if hundred_int != 0 and two_decimal_int != 0:
        words.append('and')

    if two_decimal_int <= 20:
        words.append(char[two_decimal_int])
    else:
        decimal_int = two_decimal_int // 10
        digit_int = two_decimal_int - decimal_int * 10
        words.append(char[decimal_int * 10] + '-' + char[digit_int])


char = {
    1: "One", 11: "Eleven", 2: "Two", 12: "Twelve", 3: "Three", 13: "Thirteen",
    4: "Four", 14: "Fourteen", 5: "Five", 15: "Fifteen", 6: "Six", 16: "Sixteen",
    7: "Seven", 17: "Seventeen", 8: "Eight", 18: "Eighteen", 9: "Nine",
    19: "Nineteen", 10: "Ten", 20: "Twenty", 30: "thirty", 40: "forty",
    50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
}

amt = '0' * 7 + str(input("please input to non-negative integer amount: "))
hundred, thousand, million = int(amt[-3:]), int(amt[-6:-3]), int(amt[-7:-6])
words = []

if million > 0:
    words.append(char[million])
    words.append('million')

convert_three_digits_int(thousand)

if thousand > 0:
    words.append('thousand')

if hundred < 100 and hundred != 0:
    words.append('and')

convert_three_digits_int(hundred)

if amt == '0' * 8:
    print('Zero')
else:
    print(' '.join(words).capitalize())
