#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/8/19 01:07
@user: jiananwang
@title: 插入排序
"""
import random
import time


def insertion_sort(ls: list):
    for i in range(len(ls)-1):
        if ls[i] < ls[i+1]:
            continue

        ls[i] = ls[i] ^ ls[i+1]
        ls[i+1] = ls[i] ^ ls[i+1]
        ls[i] = ls[i] ^ ls[i+1]

        while i != 0:
            if ls[i-1] > ls[i]:
                ls[i] = ls[i] ^ ls[i - 1]
                ls[i - 1] = ls[i] ^ ls[i - 1]
                ls[i] = ls[i] ^ ls[i - 1]
            i -= 1
        # print(ls)
    return ls


def main():
    rand_list = [random.randint(0, 1000) for i in range(10000)]
    # rand_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # print(len(rand_list))
    time1 = time.time()
    insertion_sort(rand_list)
    time2 = time.time()
    print('done', time2 - time1)


if __name__ == '__main__':
    main()
