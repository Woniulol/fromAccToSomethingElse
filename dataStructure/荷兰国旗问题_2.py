#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/8/19 15:54
@user: jiananwang
@title: 荷兰国旗问题_1
"""


def put_left_or_right(arr: list, left, right):
    small_area_position = left - 1
    large_area_position = right
    i = 0
    num = arr[-1]

    while i < len(arr):
        if i == large_area_position:
            break

        if arr[i] < num:
            arr[i], arr[small_area_position + 1] = arr[small_area_position + 1], arr[i]
            small_area_position += 1
            i += 1
            continue

        if arr[i] == num:
            i += 1
            continue

        if arr[i] > num:
            arr[i], arr[large_area_position - 1] = arr[large_area_position - 1], arr[i]
            large_area_position -= 1

    if small_area_position != 0:
        put_left_or_right(arr, left=0, right=small_area_position)
    if large_area_position != len(ls):
        put_left_or_right(arr, left=large_area_position, right=len(ls))

    return arr


ls = [10,5,2,3,6,3,4,2,1,10,4,2,5]
print(put_left_or_right(ls, left=0, right=len(ls)))
