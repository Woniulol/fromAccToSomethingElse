#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/8/19 00:00
@user: jiananwang
@title: test_1
"""

'''
一个整形数组只有一个数字出现了奇数次
找到这个奇数

一个整形数组有两个数字出现了奇数次 (a, b)
找到这两个数
'''

ls = [1, 1, 2, 2, 4, 3, 3, 4, 5, 5, 5, 5, 3]

result = 0
for i in range(len(ls)):
    result = result ^ ls[i]

print(result)

ls_2 = [1, 1, 1, 2, 7, 2, 4, 3, 3, 4, 5, 5, 5, 5, 6, 6, 1, 6]

result2 = 0
for i in range(len(ls_2)):
    result2 = result2 ^ ls_2[i]

result3 = 0
rightone = result2 & (~result2 + 1)
print(bin(rightone)) #位置

for i in range(len(ls_2)):
    if bin(ls_2[i])[-rightone] == str(1):
        result3 = result3 ^ ls_2[i]

print(result2)
# 显然reuslt_2 = a ^ b = 6
# bin(6) = 0b110
# 因为异或操作时，两数任意一位相等，该位既为0
# 由此可知，a和b在二三位上都不相等
# 我们可以使用固定操作找到最右边为一的位数
print(result3)
# 对第二位为1的数取异或
# 所有其他第二位为1的数出现的次数为偶数次，结果仍然为0
# 由于我们分隔了a，b，得到的结果必然为a或b之一
print(result2 ^ result3)
# result2 = a ^ b
# result3 = a或b
# result2 ^ result3 = a ^ b ^ a或b = b或a

