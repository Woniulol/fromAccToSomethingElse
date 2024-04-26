#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/8/19 19:42
@user: jiananwang
@title: heap_insert
"""


def take_number():
    global ls
    num = input('input the num you want to put in:')
    try:
        num = int(num)
        ls.append(num)
        ls = heap_insert(ls, len(ls)-1)
        return ls
    except:
        return 'end of input'


def heap_insert(arr: list, index: int):
    while arr[index] > arr[int((index - 1) / 2)]:
        arr[index], arr[int((index - 1) / 2)] = arr[int((index - 1) / 2)], arr[index]
        index = int((index - 1) / 2)
    return arr


ls = [ ]
go = ''
while go != 'end of input':
    go = take_number()
