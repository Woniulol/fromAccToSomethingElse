#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/8/18 23:03
@user: jiananwang
@title: data_structure
"""
import random


def bubble_sort(ls: list):
    times = len(ls)
    count = 1
    while count <= times - 1:
        a = 0
        while a < times - count:
            if ls[a] > ls[a + 1]:
                ls[a] = ls[a] ^ ls[a+1]
                ls[a+1] = ls[a] ^ ls[a+1]
                ls[a] = ls[a] ^ ls[a+1]
                # ls[a], ls[a + 1] = ls[a + 1], ls[a]
            a += 1
        # print(ls)
        count += 1
    return ls


def main():
    count = 1
    for j in range(5000):
        rand_list = [random.randint(0, 1000) for i in range(1000)]
        rand_list_copy = rand_list.copy()
        bubble_result = bubble_sort(rand_list)
        buildin_result = sorted(rand_list_copy)
        if bubble_result == buildin_result:
            print('pass', count)
            count += 1
        else:
            print('error', count, bubble_result, buildin_result)
            break


if __name__ == '__main__':
    main()
