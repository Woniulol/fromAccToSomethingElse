#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/8/19 15:54
@user: jiananwang
@title: 荷兰国旗问题_1
"""


def put_left_or_right(arr: list, num: int):
    small_area_count = -1
    count_num = 0
    for i in range(len(arr)):
        if arr[i] <= num:
            small_area_count += 1
            arr[i], arr[small_area_count] = arr[small_area_count], arr[i]
            if arr[small_area_count] == num:
                count_num += 1
            if arr[small_area_count] < arr[max(small_area_count-1, 0)]:
                arr[small_area_count], arr[max(small_area_count-count_num, 0)] = arr[max(small_area_count-count_num, 0)], arr[small_area_count]
    return arr


print(put_left_or_right([10,10,3,3,3,3,3,2,2,2,2,1,1,1,3,2,3,2,1,10], 3))
