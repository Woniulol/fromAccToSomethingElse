#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/9/23 13:47
@user: jiananwang
@title: my_array
"""


def my_insert(nums: list[int], num: int, index: int):
    # insert int num to index of nums
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    nums[index] = num
    return nums


def my_del(nums: list[int], index: int):
    # delete the element in index
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]
    return nums


def my_find(nums: list[int], target: int):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


def main():
    global my_list
    my_list = [1, 2, 3, 4, 5]


if __name__ == '__main__':
    main()
