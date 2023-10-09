#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/6/25 16:27
@user: jiananwang
@title: MP0001_session_9_practice_q1
"""
import math


def is_prime(n):
    stopping = int(math.sqrt(n)) + 1  # 能被开方之后的数肯定都不是prime了
    for i in range(2, stopping):
        if n % i == 0:
            return False
    return True


def main():
    for k in range(2, 99999):
        yn = is_prime(k)
        s = "prime" if yn else "not prime"
        print(f'{k:10d} is {s}')


if __name__ == '__main__':
    main()
