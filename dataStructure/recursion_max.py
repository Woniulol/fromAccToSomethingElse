#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/8/19 12:26
@user: jiananwang
@title: recursion_max
"""
import random


def process(arr, left: int, right: int):
    if len(arr[left:right]) == 1:
        return arr[left]

    mid = int(left + ((right - left) >> 1))
    left_max = process(arr, left, mid)
    right_max = process(arr, mid, right)

    if left_max > right_max:
        return left_max
    return right_max


rand_list = [random.randint(0, 1000) for i in range(10)]
print(process(rand_list, 0, len(rand_list)))
print(max(rand_list))

