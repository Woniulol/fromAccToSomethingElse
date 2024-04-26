#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/8/19 20:26
@user: jiananwang
@title: heap_insert_reverse
"""

# 去掉大根堆的根节点，重新获得一个大根堆

def heap_insert_reverse(ls):
    ls[0] = ls[-1]
    # 将最后一个放到第一个的位置
    ls = ls[:-1]
    # heapsize - 1模拟取出了第一个
    ls = heapify(ls, 0, len(ls))
    return ls


def heapify(ls: list, index: int, heapsize: int):
    # 某个数在index位置能否继续向下移
    bottom_left = index * 2 + 1
    while bottom_left < heapsize:
        if (ls[bottom_left + 1] > ls[bottom_left]) and (bottom_left + 1 < heapsize):
            largest_son = bottom_left + 1
        else:
            largest_son = bottom_left

        if ls[largest_son] == ls[index]:
            break

        ls[index], ls[largest_son] = ls[largest_son], ls[index]
        index = largest_son
        bottom_left = index * 2 + 1
    return ls

my_ls = [23, 7, 4, 6, 6, 4, 3, 4, 5, 5, 2, 3, 3, 2, 3, 1, 2, 2, 4, 2]
print(heap_insert_reverse(my_ls))
