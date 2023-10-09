#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/6/24 22:26
@user: jiananwang
@title: MP0001_session_9_practice_q1
"""
import string

punctuations_dict = {}
txt = input("please input the string: ")
txt_list = txt.strip().split()

# save index of punctuation
for index, word in enumerate(txt_list):
    if word[-1] in string.punctuation.replace("-", ""):
        txt_list[index] = word[:-1]  # remove punctuations from the word
        punctuations_dict[index] = word[-1]  # save punctuation index to to dict

# reverse and insert punctuation
txt_reversed_list = txt_list[::-1]
for index, punctuation in punctuations_dict.items():
    txt_reversed_list[index] = txt_reversed_list[index] + punctuation  # recombine the punctuation

print(' '.join(txt_reversed_list).capitalize())
