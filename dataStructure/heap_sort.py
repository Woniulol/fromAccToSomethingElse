#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/8/20 00:36
@user: jiananwang
@title: heap_sort
"""
import random
import time

def heapify(ls: list, index: int, heapsize: int):
    # 某个数在index位置能否继续向下移
    bottom_left = index * 2 + 1
    while bottom_left < heapsize:
        if (ls[bottom_left + 1] > ls[bottom_left]) and (bottom_left + 1 < heapsize):
            largest_son = bottom_left + 1
        else:
            largest_son = bottom_left
        if ls[largest_son] <= ls[index]:
            break
        ls[index], ls[largest_son] = ls[largest_son], ls[index]
        index = largest_son
        bottom_left = index * 2 + 1
    return ls


def heap_insert(arr: list, index: int, heapsize: int):
    while (arr[index] > arr[int((index - 1) / 2)]) and index < heapsize:
        arr[index], arr[int((index - 1) / 2)] = arr[int((index - 1) / 2)], arr[index]
        index = int((index - 1) / 2)
    return arr


ls = [random.randint(0, 1000) for i in range(1000000)]
ls_2 = ls.copy()
heap_size = len(ls)
time1 = time.time()
for i in range(len(ls)):
    ls = heap_insert(arr=ls, index=i, heapsize=heap_size)
while heap_size > 0:
    ls[0], ls[heap_size-len(ls)-1] = ls[heap_size-len(ls)-1], ls[0]
    heap_size -= 1
    ls = heapify(ls, index=0, heapsize=heap_size)
time2 = time.time()
print(time2-time1)

time1 = time.time()
ls_2 = sorted(ls_2)
time2 = time.time()
print(time2-time1)
