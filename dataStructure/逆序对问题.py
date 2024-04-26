#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/8/19 15:25
@user: jiananwang
@title: 逆序对问题
"""
import random, time


def my_merge(arr1: list, arr2: list):
    len1 = len(arr1)
    len2 = len(arr2)
    help_ls = []
    i_left = 0
    i_right = 0
    while (i_left < len1) and (i_right < len2):
        if arr1[i_left] < arr2[i_right]:
            help_ls.append(arr1[i_left])
            i_left += 1
        else:
            help_ls.append(arr2[i_right])
            for i in arr1[i_left:]:
                print((i, arr2[i_right]))
            # this for loop is the only difference
            i_right += 1

    if i_left >= len1:
        help_ls = help_ls + arr2[i_right:]

    if i_right >= len2:
        help_ls = help_ls + arr1[i_left:]

    return help_ls


def process(arr: list, left: int, right: int):
    if len(arr[left:right]) == 1:
        ls = [arr[left]]
        return ls

    mid = left + ((right - left) >> 1)
    list_left = process(arr, left, mid)
    list_right = process(arr, mid, right)
    return my_merge(list_left, list_right)


def main():
    # rand_list = [random.randint(0, 1000) for i in range(10000)]
    rand_list = [3, 2, 4, 5, 0]
    time1 = time.time()
    process(rand_list, 0, len(rand_list))
    time2 = time.time()
    # print('done', time2 - time1)
    sorted(rand_list)
    # print('done')


if __name__ == '__main__':
    main()
